# LMT Social Accounts — Single Source of Truth
## Last Updated: 2026-03-23

---

## Active Business Accounts

| Platform | Account Name | Handle/URL | Followers | Email Connected | Status |
|----------|-------------|------------|-----------|-----------------|--------|
| LinkedIn (Company) | Learn More Technologies, LLC | linkedin.com/company/learn-more-technologies-llc | 2 | brian@learnmoretechnologies.com | Done — page set up, branded, all details filled |
| LinkedIn (Personal) | Brian McKinney | linkedin.com/in/brianmckinneylmt | 164 connections, 164 followers | brian@learnmo.com | Done — privacy locked, ad data off, "Open to work" removed |
| Facebook (Business) | Learn More Technologies | facebook.com/learnmoretechnologies | 859 | brian@learnmoretechnologies.com | Done — branded, bio correct, contact info verified |
| Facebook (Personal) | Brian McKinney | facebook.com/mckinneymedia1 | 62 friends | brian@learnmo.com | Done — banner updated, bio updated, privacy locked |
| Facebook (Page 2) | 50Plustechbridge | TBD | TBD | TBD | Needs audit |
| Instagram | 50+TechBridge | instagram.com/50plustechbridge | 10 | brian@learnmo.com | Done — renamed, logo set, bio added |
| YouTube | Learn More Technologies | youtube.com/c/LearnMoreTechnologies (@LearnMoreTechnologies) | 517 subs, 9 videos | hello@learnmoretechnologies.com | Done — fully branded, all links updated |
| X / Twitter | TBD | TBD | 0 | brian@learnmoretechnologies.com (planned) | Signup stuck — retry later |

---

## Accounts to Delete

| Platform | Account | Reason |
|----------|---------|--------|
| Instagram | @smallbusinessonlinesalescoach | Old branding, 67 followers, 0 posts |
| Instagram | @mckinney_media | Old branding (if it still exists) |

---

## Email Structure

| Email | Role | Gmail Labels/Filters |
|-------|------|---------------------|
| brian@learnmoretechnologies.com | Business only — clients, partners, social accounts | → LMT-Business (starred, never spam) |
| hello@learnmoretechnologies.com | Public-facing contact, YouTube channel | → LMT-Hello (starred, never spam) |
| consult@learnmoretechnologies.com | Consulting inquiries | → LMT-Consult (starred, never spam) |
| brian@learnmo.com | Personal + admin (all above forward here) | Primary inbox |
| b@learnmo.com | Kill — forward to brian@learnmo.com | To be deactivated |

---

## Gmail Filters Active

| Filter | Action |
|--------|--------|
| To: brian@learnmoretechnologies.com | Label: LMT-Business, Star, Never Spam |
| To: hello@learnmoretechnologies.com | Label: LMT-Hello, Star, Never Spam |
| To: consult@learnmoretechnologies.com | Label: LMT-Consult, Star, Never Spam |
| From: mail.mailchimp.com | Label: LMT-Mailchimp, Never Spam |
| 30+ existing spam/junk filters | Skip inbox / Delete |

---

## Brand Assets in Git

| Asset | Path | Size |
|-------|------|------|
| FB Group Cover | assets/banners/lmt-fb-group-cover.png | 1640x856 |
| FB Personal Header | assets/banners/LMT_FB_Personal_Header.png | 2560x1440 |
| LinkedIn Personal Banner | assets/banners/LMT_LinkedIn_Banner_2026.png | 1128x191 |
| LinkedIn Company Banner | assets/banners/LMT_LinkedIn_Banner_business_page.png | 1128x191 |
| 50+TechBridge Logo | assets/logos/lmt-fb-group-icon.png | Circle badge |
| LMT White Logo | assets/logos/LMT_Logo_White.png | White on transparent |
| Podcast Cover | assets/logos/lmt-podcast-cover.png | Podcast artwork |

---

## Publishing & Content Stack — Consolidated August 2026

| Tool | Purpose | Status |
|------|---------|--------|
| **Claude CLI** | Write all content — articles, captions, scripts, emails | Active |
| **Git (LMT repo)** | Version control for all content and strategy docs | Active |
| **tools/wp-publish.py** | Push markdown articles to WordPress via REST API | Active — creds in tools/.env |
| **Metricool** | Schedule FB + IG + YouTube. Analytics all platforms. | Connected. **Activate scheduling — primary tool going forward.** |
| **LinkedIn (native)** | Post video + articles directly — algorithm favors native uploads | Manual only — do NOT route through Metricool |
| **Canva** | Slide design, video assembly, graphics | Active |
| **ElevenLabs** | Voiceover generation (Voice ID: uAs0vN0GLLpz7FM7JVkz) | Active |
| **ffmpeg** | Video assembly, audio mixing, caption burn-in | Active via Claude CLI |
| Buffer | Originally planned for scheduling | **DROPPED — never connected. Metricool replaces it.** |
| Brand24 | Mention monitoring | Deferred |

### Metricool Free Plan — Status & Max Strategy (Aug 1, 2026)
| Platform | Connected | Followers | Action Needed |
|----------|-----------|-----------|---------------|
| Facebook | ✅ | 855 | Post 3-4x/week — currently 1 post/30 days |
| YouTube | ✅ | — | Schedule via Metricool |
| Instagram | ✅ | 10 | Connected via Facebook page link — 2026-08-01 |
| LinkedIn | ❌ | — | Requires $20/mo paid plan — post natively only |
| TikTok | ❌ | — | Skip — not our audience |

- Track hashtags: `#50PlusTechBridge` and `#WorkforceMath`
- Add 2-3 competitors under Competitors tab
- Check best time to post per platform before scheduling
- **Do NOT upgrade until posting 20+ pieces/month**

### Platform Posting Rules
| Platform | Method | Tool |
|----------|--------|------|
| LinkedIn video + articles | Native upload only | Manual |
| Facebook | Schedule ahead | Metricool |
| Instagram | Schedule ahead | Metricool |
| YouTube | Schedule ahead | Metricool |
| WordPress / Blog | CLI push | tools/wp-publish.py |

---

## Privacy Lockdown Status

| Platform | Privacy | Ad Tracking | Discoverability | Friend/Follow Requests |
|----------|---------|-------------|-----------------|----------------------|
| LinkedIn | Locked | All OFF | Email: restricted, Phone: nobody | Email-only invitations |
| Facebook | Locked | All OFF | Email: only me, Phone: only me, Search engines: no | Friends of friends |
| Instagram | TBD | TBD | TBD | TBD |
| YouTube | TBD | N/A | N/A | N/A |
| Gmail/Google | Pending | Pending | Pending | N/A |
