# LMT Site Health Monitor

## Daily Check (run every morning before content work)
```
python Desktop/LMT/ops/site-health-check.py
```

## What it checks
1. **SSL certificate** — valid? expiring soon?
2. **Critical pages** — homepage, courses, /startfreetoday, /train, /workforce, /speak, /contact
3. **Mailchimp API** — key still active? signups syncing?
4. **WordPress REST API** — site responding?

## Weekly Manual Checks (every Monday)
- [ ] Log into LearnDash — are course enrollments tracking?
- [ ] Check Mailchimp audience — new subscribers appearing?
- [ ] Check Bluehost — any billing alerts or renewal notices?
- [ ] Check WP Plugins page — any updates pending? (red badge count)
- [ ] Check error_log via Bluehost File Manager — any new errors?

## To-Do This Week (by 2026-05-02)
- [ ] Clean bot accounts from WP Users (random string usernames) — delete all content
- [ ] Verify LearnDash participants list matches after bot cleanup
- [ ] Create `/startfreetoday` page or redirect to `/courses/50techbridge/`
- [ ] Update landing page: change "six free modules" to "three free lessons"
- [ ] Delete test@learnmo.com from Mailchimp and WP Users
- [ ] Launch content: YouTube video, Short, WP article, LinkedIn post, FB post
- [ ] Activate hCaptcha plugin to prevent future bot signups
- [ ] Update BuddyBoss Platform (2.21.0 → 2.21.1) and Pro (2.13.1 → 2.13.2)

## Known Issues Log
| Date | Issue | Status |
|------|-------|--------|
| 2026-04-27 | SSL certificate broken — Bluehost investigating | Was fine — false alarm |
| 2026-04-27 | Mailchimp API key disabled — needs new key | FIXED — new key active |
| 2026-04-27 | LMT Join Now Form debug logging spamming error_log | FIXED — line removed |
| 2026-04-27 | Yoast redirect loop /courses/ ↔ /our-courses/ | FIXED — redirect deleted |
| 2026-04-27 | BuddyBoss registration disabled | FIXED — enabled |
