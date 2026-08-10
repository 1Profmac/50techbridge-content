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



### #5 — FIX-008: SEOMachine Missing Config Files (Analytics Dead)
- **Impact:** All research, GA4, and Google Search Console scripts fail silently
- **Missing files:** `seomachine/config/competitors.json` ✅ (created 2026-08-10) · `credentials/ga4-credentials.json` · `credentials/gsc-credentials.json`
- **Blank .env fields:** `GA4_PROPERTY_ID` · `DATAFORSEO_LOGIN` · `DATAFORSEO_PASSWORD`
- **Fix:**
  1. Google Cloud Console → IAM → Service Accounts → create account for seomachine
  2. Download JSON key → save as `seomachine/credentials/ga4-credentials.json`
  3. In GA4 Admin → Property Access Management → add service account as Viewer
  4. Enable Search Console API → save key as `seomachine/credentials/gsc-credentials.json`
  5. Fill in `GA4_PROPERTY_ID` in `seomachine/data_sources/config/.env`
- **Priority:** MEDIUM — /write and /publish still work; only analytics/research blocked

---

### #6 — Buzzsprout Podcast Trial Expiring
- **Impact:** Podcast episodes disappear if not paid
- **Fix:** Pay $19/mo at buzzsprout.com
- **Priority:** MEDIUM — pay before trial ends

---

## COMPLETED FIXES

| Fix | Date | Notes |
|---|---|---|
| Homepage video showing "unavailable" | 2026-08-08 | Updated embed to new WHAT IF video ID |
| Deleted duplicate WHAT IF video | 2026-08-08 | Kept revised version |
| FIX-004: /join-now/ 404 — 17 broken CTAs | 2026-08-10 | Replaced with /start-free-lesson/ in 4 HTML files. WP 301 redirect confirmed live. |
| FIX-007: Course pages 404 | 2026-08-10 | Added 301 redirects in Yoast: /courses/tech-essentials-for-50-plus/ and /50-plus-tech-bridge/ both → /start-free-lesson/. Verified live. |
| FIX-005: Dead Mailchimp form on join-now page | 2026-08-10 | Replaced with MailerLite embed. Account: 2466946 · Form ID: sK7Nea · Group: Agentic50+. File: BRAND/pages/join-now-page-FIXED.html. Deploy to WP when ready. |
| FIX-006: wp-publish.py 401 Unauthorized | 2026-08-10 | New WP App Password generated (name: "Claude Tools"). Updated tools/.env. User: brian. Verified 200 OK. |

---

## HOW TO USE THIS LIST
- Open this file at the start of any session where something feels broken
- Tell Claude "check fix list" and we work through it
- Mark items complete with date when done
