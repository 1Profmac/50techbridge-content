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

### #2 — digitalpioneer.ai Application Form ✅ FIXED 2026-08-11
- **Fix applied:** MailerLite API wired directly into form JavaScript
- **API key stored:** `Desktop/LMT/tools/.env` → MAILERLITE_API_KEY
- **Group:** Agentic50+ (ID: 191122765174015605)
- **Repo:** github.com/1Profmac/digitalpioneer-pages (local: Documents/digitalpioneer-pages)

---

## DEPLOY PROCESS — digitalpioneer.ai
**Use this every time a fix is made to the site:**
1. Edit `Desktop/LMT/BRAND/web/digitalpioneer-index.html` locally
2. Copy to `Documents/digitalpioneer-pages/index.html`
3. `cd /c/Users/USER/Documents/digitalpioneer-pages`
4. `git add index.html && git commit -m "description" && git push origin master`
5. Go to Bluehost cPanel → Git Version Control → digitalpioneer-pages → Manage → Pull or Deploy tab
6. Click **Update from Remote** → then **Deploy HEAD Commit**
7. Verify live at digitalpioneer.ai

**Never upload manually via File Manager again.**

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
| FIX-009: start-free-lesson image slow (4MB cross-domain) | 2026-08-10 | Compressed 3.97MB → 49KB. Uploaded to LMT domain. Swapped image + replaced Mailchimp form with MailerLite. Verified live. |
| FIX-008: SEOMachine analytics dead | 2026-08-10 | GCP project: gen-lang-client-0793609136. Service account: seomachine@gen-lang-client-0793609136.iam.gserviceaccount.com. GA4 property: 249114191. Credentials saved to seomachine/credentials/. GA4 + GSC access granted. |
| FIX-002: digitalpioneer.ai form broken | 2026-08-11 | Wired to MailerLite API. Key in tools/.env. Group: Agentic50+ (191122765174015605). Nav button fixed to open modal. Deployed via digitalpioneer-pages git repo. |

---

## HOW TO USE THIS LIST
- Open this file at the start of any session where something feels broken
- Tell Claude "check fix list" and we work through it
- Mark items complete with date when done
