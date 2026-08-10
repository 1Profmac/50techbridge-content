# LMT FIX LIST
## Broken things that cost money or contracts until fixed
### Last Updated: August 2026

---

## OPEN FIXES

### #1 — Google Workspace Email Not Receiving
- **Impact:** brian@learnmoretechnologies.com not getting inbound mail
- **Cause:** MX records changed months ago, config broke
- **Fix:**
  1. Go to admin.google.com → Domains → confirm learnmoretechnologies.com shows "Verified"
  2. Go to Apps → Google Workspace → Gmail → confirm Gmail is ON
  3. Go to Bluehost → DNS → confirm MX records point to Google (aspmx.l.google.com etc.)
  4. If MX records wrong, reset them to Google's MX values
- **Priority:** URGENT — missing inbound contracts

---

### #2 — digitalpioneer.ai Application Form Broken
- **Impact:** Every application submitted disappears — nobody gets it
- **Cause:** Form action points to /submit.php which doesn't exist on static host
- **Fix:**
  1. Sign up at formspree.io with brian@learnmo.com
  2. Create form called "Digital Pioneer Applications"
  3. Copy endpoint (https://formspree.io/f/xxxxxxxx)
  4. Tell Claude — will swap into digitalpioneer-index.html in 30 seconds
  5. Upload updated file to Bluehost File Manager → public_html/digitalpioneer.ai/index.html
- **Priority:** HIGH — program applications going nowhere

---

### #3 — Buzzsprout Podcast Trial Expiring
- **Impact:** Podcast episodes disappear if not paid
- **Fix:** Pay $19/mo at buzzsprout.com
- **Priority:** MEDIUM — pay before trial ends

---

## COMPLETED FIXES

| Fix | Date | Notes |
|---|---|---|
| Homepage video showing "unavailable" | 2026-08-08 | Updated embed to new WHAT IF video ID |
| Deleted duplicate WHAT IF video | 2026-08-08 | Kept revised version |

---

## HOW TO USE THIS LIST
- Open this file at the start of any session where something feels broken
- Tell Claude "check fix list" and we work through it
- Mark items complete with date when done
