# SQL Flow – Content Bank & Post Log
Rule: never reuse an ID marked as posted. Use a different pillar and format for each post in the week. New ideas may be added (next free ID per pillar) based on sqlaccountingapi.com features/assistant/docs.

Formats: Problem→Fix · Chat demo · Code snippet · Before/After · Myth vs Fact · Checklist · Mini case study · Poll/Question · Stat card · Flow diagram

| ID | Pillar | Use case (hook) | Feature |
|----|--------|-----------------|---------|
| A01 | Assistant | "Who owes us the most?" answered in seconds | Q&A, outstanding/aging |
| A02 | Assistant | Snap a supplier bill → drafted purchase invoice | Bill reading, supplier by TIN/BRN |
| A03 | Assistant | Collect payment on the road via WhatsApp, post with PIN | WhatsApp, roles, PIN, knock-off |
| A04 | Assistant | Staff post up to RM X; above that goes to an approver | Roles, approvers |
| A05 | Assistant | Rule in plain words: "repairs go to project HQ" | Rules, tested on recent docs |
| A06 | Assistant | Upload your SOP and it follows it | Knowledge upload |
| A07 | Assistant | Your data, your model: Claude key or local Ollama | Privacy, model choice |
| A08 | Assistant | Stock check before quoting, on WhatsApp | Stock Q&A |
| A09 | Assistant | Duplicate bill caught before posting | Not-entered-before check |
| W01 | Webhooks | Payment received → auto WhatsApp thank-you | HMAC webhooks |
| W02 | Webhooks | Stop polling: changes in seconds | Webhooks vs polling |
| W03 | Webhooks | Stock movement → alert purchaser | Stock webhooks |
| P01 | API | Shopee/Shopify order → sales invoice | POST /salesinvoice |
| P02 | API | Email invoice PDFs from your own app | ?format=pdf |
| P03 | API | Booking deposit → invoice + knock-off | Payments, knock-offs |
| P04 | API | Read every company in one call | X-Company: * |
| P05 | API | /changes: sync only what moved | Changes endpoint |
| P06 | API | Same 69 official resource names | Official format |
| S01 | Safety | Retry without double-posting | Idempotency-Key |
| S02 | Safety | Import 100 invoices: dry run first | Batch dry run |
| S03 | Safety | Who posted this, when, from where? | Audit trail |
| S04 | Safety | A token that can only read, from one IP | Token limits |
| S05 | Safety | Internet down? Integration keeps running | Local, offline licence |
| S06 | Safety | 0 bytes of your accounts leave the office | Local architecture |
| R01 | Reports | FIFO stock aging in 30-day bands: find dead stock | Stock aging |
| R02 | Reports | Customer statements on demand | Statements API |
| R03 | Reports | MyInvois e-Invoice status of every document | e-Invoice status |
| R04 | Reports | Month-end stock balance without Excel | Stock reports |
| I01 | Industry | Restaurant: POS outlets → daily sales posting | POS sync |
| I02 | Industry | Clinic/spa: booking → invoice → payment | Booking integration |
| I03 | Industry | Accounting firm: 5 companies, one licence | Enterprise plan |
| I04 | Industry | Distributor: salesmen check balances before visits | Assistant + outstanding |
| D01 | Dev tips | First API call in an afternoon (4 steps) | Install → token → call |
| D02 | Dev tips | Expose safely with your Cloudflare tunnel | Tunnel + IP limits |
| D03 | Dev tips | Test every endpoint in the console explorer | API explorer |
| D04 | Dev tips | Windows on ARM? Supported | x64 + ARM64 builds |

## Post log
| Week | ID | Pillar | Format | Status | FB post ID |
|------|----|--------|--------|--------|-----------|
| 2026-W47 | A03 | Assistant | Chat demo | published | 1367858506420728_122106831339549035 |
| 2026-W47 | S01 | Safety | Before/After | draft | 1367858506420728_122106831507549035 |
