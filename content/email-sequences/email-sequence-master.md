# 50+TechBridge Welcome Series — Email Sequence Master

**Platform:** MailerLite
**Account:** brian@learnmo.com · Group: 50+TechBridge
**Status:** ✅ LIVE (migrated from Mailchimp June 2026 — Mailchimp locked account)
**Plan:** Free

---

## Sequence Overview

| # | File | Subject | Trigger | Delay |
|---|---|---|---|---|
| 1 | email-1-welcome.md | You're in. Your first lesson is waiting. | Course Signup tag | Immediate |
| 2 | email-2-nudge.md | Still with us, *\|FNAME\|*? | Did not click Email 1 | Day 3 |
| 3 | email-3-milestone.md | A week in, *\|FNAME\|* — here's what's next. | All contacts | Day 7 |
| 4 | email-4-pioneer-story.md | She was 62 and thought she was too late. | All contacts | Day 14 |
| 5 | email-5-upgrade.md | You're not done yet, *\|FNAME\|*. | All contacts | Day 21 |

---

## Automation Logic

```
Contact tagged "Course Signup"
        ↓
Email 1 — Welcome (immediate)
        ↓
Wait 3 days
        ↓
IF/ELSE — Email engagement: Did not click Email 1
        ↓                    ↓
      YES                   NO
  Send Email 2          Do nothing
        ↓
Wait 1 week (Day 7)
        ↓
Email 3 — Milestone
        ↓
Wait 1 week (Day 14)
        ↓
Email 4 — Pioneer Story
        ↓
Wait 2 weeks (Day 21)
        ↓
Email 5 — Upgrade
        ↓
Contact exits
```

---

## Brand Standards Applied

- **From Name:** Prof. McKinney
- **From Email:** hello@learnmoretechnologies.com
- **Header:** Navy #0E1C2F
- **Accent:** Gold #C8942E
- **Button:** Green #109F35
- **Stats:** 347+ Pioneers · 3X completion rate · 74% more confident
- **Primary CTA URL:** https://learnmoretechnologies.com/courses/50techbridge/
- **Upgrade URL:** https://learnmoretechnologies.com/join-now/
- **Consult URL:** https://learnmoretechnologies.com/consult/

---

## Agent Assignment

**Owner:** Alex — EA Agent
**Supervised by:** Maya — COO Agent
**Skill file:** SKILL-lmt-mailerlite-email-sequence.md

---

*Built: March 22, 2026*
*Last updated: July 21, 2026 — platform migrated to MailerLite*
