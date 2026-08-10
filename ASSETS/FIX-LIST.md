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

### #3 — FIX-006: wp-publish.py Returns 401 Unauthorized
- **Impact:** Blog publishing tool broken — can't push articles to WordPress from CLI
- **Cause:** WP credentials in `tools/.env` are wrong (username `brian` not resolving, password may be revoked)
- **Fix:**
  1. Log into learnmoretechnologies.com/wp-admin
  2. Users → Profile → note exact username at top of page
  3. Scroll to Application Passwords → Add New → name it "Claude Tools"
  4. Copy the generated password immediately
  5. Tell Claude — will update `Desktop/LMT/tools/.env` with new credentials
- **Priority:** MEDIUM — blog publishing tool dead

---

### #4 — FIX-007: Course/Class Signup Pages Return 404
- **Impact:** LearnDash enrollment path broken — visitors can't sign up for courses
- **Cause:** Course pages deleted, unpublished, or slugs changed in WordPress
- **Broken URLs:** `/courses/tech-essentials-for-50-plus/` · `/50-plus-tech-bridge/`
- **Working URLs:** `/courses/` (index) · `/start-free-lesson/` · `50plustechbridge.com/register/`
- **Fix:**
  1. WP Admin → LearnDash → Courses — check published status and actual slugs
  2. WP Admin → Pages — search "50 Plus Tech Bridge", check if draft/trashed
  3. Add 301 redirects from broken slugs to working pages (Yoast → Redirects)
  4. Tell Claude — will update HTML templates with correct URLs
- **Priority:** HIGH — enrollment path broken

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
| FIX-004: /join-now/ 404 — 17 broken CTAs | 2026-08-10 | Replaced with /start-free-lesson/ in LMT-Homepage.html, contact-us-page-FIXED.html, LMT_Train_Page_FIXED.html, lmt-pages/train/index.html. WP redirect still needed for published articles. |
| FIX-005: Dead Mailchimp form on join-now page | 2026-08-10 | Replaced with MailerLite embed. Account: 2466946 · Form ID: sK7Nea · Group: Agentic50+. File: BRAND/pages/join-now-page-FIXED.html. Deploy to WP when ready. |

---

## HOW TO USE THIS LIST
- Open this file at the start of any session where something feels broken
- Tell Claude "check fix list" and we work through it
- Mark items complete with date when done
