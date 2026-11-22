#!/usr/bin/env python3
"""Publish the next queued SQL Flow post if the 2-day interval has passed.

Reads posts/queue/queue.json. Uses ONE of these repo secrets:
  FB_PAGE_TOKEN    - Facebook Page access token (posts via Graph API, returns post id)
  ZAPIER_HOOK_URL  - Zapier "Catch Hook" URL whose Zap posts {image_url, message} to the page
Set FORCE=1 to ignore the interval (manual run).
"""
import datetime as dt, json, os, pathlib, sys, urllib.error, urllib.parse, urllib.request

ROOT = pathlib.Path(__file__).resolve().parent
QUEUE = ROOT / "queue.json"
LOG = ROOT.parent.parent / "content-log.md"
RAW = "https://raw.githubusercontent.com/{repo}/main/posts/queue/{file}.png"

def out(k, v):
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            f.write(f"{k}={v}\n")

state = json.loads(QUEUE.read_text(encoding="utf-8"))
today = dt.datetime.now(dt.timezone(dt.timedelta(hours=8))).date()  # Malaysia time
last = dt.date.fromisoformat(state["last_published"])
if (today - last).days < state["interval_days"] and os.environ.get("FORCE") != "1":
    print(f"Not due: last post {last}, next due {last + dt.timedelta(days=state['interval_days'])}.")
    out("published", "0"); sys.exit(0)

item = next((q for q in state["queue"] if q["status"] == "queued"), None)
if not item:
    print("::warning::Queue is empty - add more posts to posts/queue/queue.json")
    out("published", "0"); sys.exit(0)

if not (ROOT / f"{item['file']}.png").exists():
    sys.exit(f"PNG for {item['file']} not rendered yet; check the 'Render SVG to PNG' workflow.")

image_url = RAW.format(repo=os.environ["GITHUB_REPOSITORY"], file=item["file"])
token, hook = os.environ.get("FB_PAGE_TOKEN"), os.environ.get("ZAPIER_HOOK_URL")

if token:
    data = urllib.parse.urlencode({"url": image_url, "caption": item["caption"],
                                   "access_token": token}).encode()
    req = urllib.request.Request(f"https://graph.facebook.com/v21.0/{state['page_id']}/photos", data=data)
    try:
        resp = json.load(urllib.request.urlopen(req, timeout=60))
    except urllib.error.HTTPError as e:
        sys.exit(f"Facebook error {e.code}: {e.read().decode()}")
    post_id = resp.get("post_id") or resp.get("id")
    if not post_id:
        sys.exit(f"Facebook did not return a post id: {resp}")
    status = "published"
elif hook:
    body = json.dumps({"image_url": image_url, "message": item["caption"], "id": item["id"]}).encode()
    req = urllib.request.Request(hook, data=body, headers={"Content-Type": "application/json"})
    resp = json.load(urllib.request.urlopen(req, timeout=60))
    if resp.get("status") != "success":
        sys.exit(f"Zapier hook did not accept the post: {resp}")
    post_id, status = f"zapier:{resp.get('request_id', '?')}", "sent-to-zapier"
else:
    sys.exit("No FB_PAGE_TOKEN or ZAPIER_HOOK_URL secret configured - nothing was posted.")

item.update(status=status, published_date=today.isoformat(), fb_post_id=post_id)
state["last_published"] = today.isoformat()
QUEUE.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

week = f"{today.isocalendar().year}-W{today.isocalendar().week:02d}"
row = f"| {today} | {week} | {item['id']} | {item['pillar']} | {item['format']} | {status} | {post_id} |\n"
log = LOG.read_text(encoding="utf-8")
lines = [l for l in log.splitlines(keepends=True) if not l.startswith("Next post due:")]
log = "".join(lines).rstrip("\n") + "\n" + row
log += f"\nNext post due: {today + dt.timedelta(days=state['interval_days'])}\n"
LOG.write_text(log, encoding="utf-8")

left = sum(q["status"] == "queued" for q in state["queue"])
print(f"Posted {item['id']} ({item['file']}) -> {post_id}. {left} post(s) left in queue.")
if left <= 2:
    print(f"::warning::Only {left} post(s) left in the queue - ask the agent to add more.")
out("published", "1")
