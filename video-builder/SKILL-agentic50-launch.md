---
name: Agentic50Launch
description: >
  Step-by-step launch skill for the Agentic 50 brand — domain, course,
  podcast, paywall, content series, and social setup. Uses existing
  LearnDash/BuddyBoss/WordPress stack. No new tools required.
  Trigger this skill for ANY Agentic 50 setup or launch task.
---

# Agentic50Launch — Brand Launch Skill
## Learn More Technologies | Agentic 50
### From domain purchase to first paid enrollment.

---

## WHAT THIS SKILL DOES

Launches the Agentic 50 brand: domain, WordPress setup, LearnDash course,
payment processing, podcast submission, LinkedIn article series, and
cross-platform social distribution. All on the existing tech stack.

---

## BRAND ARCHITECTURE

```
LEARN MORE TECHNOLOGIES (parent company)
├── 50+TechBridge (B2B — workforce training for organizations)
│   └── learnmoretechnologies.com/workforce
│
└── Agentic 50 (B2C — individuals building businesses after 50)
    ├── agentic50.com (course + gated content)
    ├── The Agentic 50 Podcast (Spotify, Apple, Amazon, YouTube)
    ├── The Agentic 50 Series (8 LinkedIn articles)
    ├── #Agentic50 (all platforms)
    └── YouTube Shorts → Agentic 50 playlist
```

---

## PREREQUISITES (What Brian Already Has)

| Tool | Status | Cost |
|---|---|---|
| WordPress hosting | Active | $20-30/mo (already paying) |
| LearnDash | Active — unlimited courses | $18.67/mo (already paying) |
| BuddyBoss | Active | $16.67/mo (already paying) |
| Bunny.net (video CDN) | Active | Already paying |
| HeyGen | Active | $24/mo (already paying) |
| ElevenLabs | Active | $18.33/mo (already paying) |
| Canva Pro | Active | $13/mo (already paying) |
| Claude Code | Active | $100/mo (already paying) |
| Mailchimp | Active | $13/mo (already paying) |
| Metricool | Active (analytics only) | Free tier |

**New costs for launch: ~$15-20/mo** (3 domains + optional hosting bump)

---

## PHASE 1 — FOUNDATION (Week 1)

### Step 1: Buy Domains
- [ ] Purchase agentic50.com (primary)
- [ ] Purchase theagenticpioneer.com (protect)
- [ ] Purchase agentic50plus.com (protect)
- [ ] All three redirect to agentic50.com
- **Who:** Brian
- **Time:** 5 min
- **Cost:** ~$10-12/year each

### Step 2: Point DNS
- [ ] Add agentic50.com as addon domain on existing WordPress hosting
- [ ] OR create a redirect: agentic50.com → learnmoretechnologies.com/agentic50/
- [ ] Verify SSL certificate is active (most hosts auto-provision)
- **Who:** Brian (Claude walks through if needed)
- **Time:** 15 min

### Step 3: Create Stripe Account
- [ ] Go to stripe.com → Create account
- [ ] Add bank account for payouts
- [ ] Verify identity (takes 1-2 business days)
- **Who:** Brian
- **Time:** 10 min
- **Cost:** Free (Stripe charges 2.9% + $0.30 per transaction — no monthly fee)

### Step 4: Connect Stripe to LearnDash
- [ ] WordPress Admin → LearnDash → Payments
- [ ] Enable Stripe (LearnDash has built-in Stripe integration — no WooCommerce needed)
- [ ] Test with a $1 transaction
- **Who:** Brian (Claude verifies)
- **Time:** 15 min

---

## PHASE 2 — COURSE BUILD (Week 1-2)

### Step 5: Create Course in LearnDash

**Course Name:** Agentic 50: Build Your Business After 50 with AI
**Pricing:** Free Tier (email gate) + $99 Paid Tier

#### Free Tier (Lead Magnet)
| Lesson | Content | Purpose |
|---|---|---|
| Welcome | Video (HeyGen 2 min) + text | Set expectations, build trust |
| Lesson 1: The Agentic Age | Article 1 content as video + text | Educate, hook |
| Agentic 50 Starter Checklist | PDF download | Capture email via Mailchimp |

#### $99 Paid Tier
| Module | Lessons | Format |
|---|---|---|
| **1: Mindset** | 10 mindset shifts, internalized ageism, myth-busting | HeyGen video + text |
| **2: The Stack** | Tool-by-tool setup (Claude, Canva, Metricool), live walkthroughs | HeyGen video + screenshots |
| **3: Your First Offer** | Pick your model, build with AI in real time | HeyGen video + templates |
| **4: Your First Audience** | LinkedIn optimization, first 5 posts, comment strategy | HeyGen video + templates |
| **5: Your First Dollar** | Pricing, proposals, closing, Stripe/PayPal | HeyGen video + templates |
| **6: Scale with Agents** | Solo to agent-powered, automating the business | HeyGen video + live demo |

#### LearnDash Setup Steps
- [ ] WordPress Admin → LearnDash → Courses → Add New
- [ ] Course title: "Agentic 50: Build Your Business After 50 with AI"
- [ ] Set course price: $99 (Stripe checkout)
- [ ] Create "Free Preview" lessons (open enrollment, email required)
- [ ] Create 6 modules with placeholder lessons
- [ ] Set drip content: Module 1 immediately, then 1 module/week
- [ ] Add completion certificate
- **Who:** Claude builds structure, Brian reviews
- **Time:** 1-2 hours

### Step 6: Record Module 1 Videos
- [ ] Record 3-4 HeyGen videos (landscape, 3-5 min each) covering mindset shifts
- [ ] Claude renders with lmt-video-overlay.py
- [ ] Upload to Bunny.net (not YouTube — protected content)
- [ ] Embed in LearnDash lessons
- **Who:** Brian records, Claude renders + embeds
- **Time:** 2-3 hours

---

## PHASE 3 — PODCAST LAUNCH (Week 2-3)

### Step 7: Update Podcast Branding
- [ ] Rename from "AI After 50 — The Pioneers Podcast" to "The Agentic 50 Podcast"
- [ ] Update podcast-concept.md
- [ ] Update podcast-submission-package.md (show name, descriptions)
- [ ] Update podcast-cover-canva-spec.md
- [ ] Regenerate cover art in Canva (3000x3000, navy/gold, new name)
- **Who:** Claude updates docs, Brian regenerates cover in Canva
- **Time:** 30 min

### Step 8: Record Episode 1
- [ ] Script ready: "Is It Too Late?" (podcast-concept.md, Episode 1 outline)
- [ ] Record in HeyGen (landscape) OR real microphone
- [ ] Claude renders video version with lmt-video-overlay.py
- [ ] Claude extracts MP3 audio for podcast platforms
- **Who:** Brian records, Claude processes
- **Time:** 1-2 hours

### Step 9: Submit to Podcast Platforms
- [ ] Spotify for Podcasters (podcasters.spotify.com) — free account
  - Upload cover art, show description (from submission package), Episode 1 MP3
- [ ] Apple Podcasts Connect (podcastsconnect.apple.com) — free, needs Apple ID
  - Same assets, may take 1-5 days for review
- [ ] Amazon Music for Podcasters — free
  - Same assets
- [ ] Upload video version to YouTube as regular video (not Short)
- **Who:** Brian (copy/paste from submission package in git)
- **Time:** 1 hour
- **Cost:** $0

---

## PHASE 4 — CONTENT SERIES (Week 2-4)

### Step 10: Publish LinkedIn Article Series

8 articles over 8 weeks. Full research, hooks, and data cards in:
`Desktop\LMT\AGENTIC-AGE-ARTICLE-SERIES-RESEARCH.md`

| Week | Article | Companion Content |
|---|---|---|
| 1 | The Agentic Age Is Here | YouTube Short (2.8X stat) |
| 2 | You Don't Need to Code | IG carousel (tool vs. agentic era) |
| 3 | The $200/Month Team | YouTube Short (cost comparison) |
| 4 | You're Not Too Late | IG carousel (10 founders after 50) |
| 5 | The $8.3 Trillion Market | YouTube Short ($8.3T hook) |
| 6 | 10 Lies You're Telling Yourself | LinkedIn poll |
| 7 | Week 1 Playbook | YouTube Short (Day 1-5 rapid) |
| 8 | The Future Belongs to the Experienced | LinkedIn Live Q&A |

#### Per Article Workflow
- [ ] Claude drafts article from research doc
- [ ] Brian reviews and approves
- [ ] Publish to LinkedIn as Article (not post)
- [ ] Cross-post to: Facebook (native), email newsletter, agentic50.com/blog
- [ ] Record YouTube Short companion (Brian in HeyGen vertical)
- [ ] Claude renders Short, uploads to YouTube + IG Reels + FB Reels via Metricool
- **Who:** Claude writes, Brian approves + records Shorts
- **Time:** 1-2 hours per article

---

## PHASE 5 — SOCIAL + SCHEDULING (Week 3-4)

### Step 11: Upgrade Metricool
- [ ] Upgrade to Metricool Advanced ($54/mo)
- [ ] Connect all platforms: LinkedIn, YouTube, Facebook, Instagram, X
- [ ] Enable auto-publishing
- **Who:** Brian
- **Time:** 30 min

### Step 12: First Posts on New Platforms
- [ ] Facebook: Post Part 1 landscape video natively
- [ ] Instagram: Switch to Business account, post square video, post first Reel
- [ ] X/Twitter: Retry signup, post first tweet with $850B stat
- **Who:** Brian
- **Time:** 30 min per platform

### Step 13: Schedule First 2 Weeks
- [ ] Load Article 1 + companion Short into Metricool
- [ ] Schedule: Tue/Wed 9 AM CT (LinkedIn), Thu 9 AM CT (YouTube Short + Reels)
- [ ] Set up recurring Friday analytics review
- **Who:** Brian (Claude helps draft copy)
- **Time:** 1 hour

---

## PHASE 6 — LINKEDIN POWER FEATURES (Month 2)

### Step 14: LinkedIn Newsletter
- [ ] Create newsletter from LinkedIn Company page
- [ ] Name: "The Agentic 50" or "Agentic 50 Weekly"
- [ ] Repurpose article series as first issues
- **Who:** Brian
- **Time:** 30 min setup

### Step 15: LinkedIn Carousel Template
- [ ] Build 1 Canva template (5 slides, navy #0E1C2F / gold #C8942E)
- [ ] Create first carousel from Article 4 stats (10 founders after 50)
- **Who:** Brian in Canva
- **Time:** 1 hour

### Step 16: LinkedIn Live (optional)
- [ ] Riverside.fm ($24/mo) OR free LinkedIn Live
- [ ] Schedule for Article 8 launch: "The Future Belongs to the Experienced" Q&A
- **Who:** Brian
- **Time:** 30 min setup

---

## LAUNCH CHECKLIST — MINIMUM VIABLE LAUNCH

The absolute minimum to go live with paid content:

- [ ] Domain purchased and pointing
- [ ] Stripe connected to LearnDash
- [ ] Free tier: 2 lessons + email gate live
- [ ] Paid tier: Module 1 (3-4 lessons) live, Modules 2-6 marked "Coming Soon"
- [ ] Article 1 published on LinkedIn with CTA to agentic50.com
- [ ] Podcast Episode 1 submitted (can be simultaneous)

**Everything else is growth, not launch.** Ship the minimum, then build in public.

---

## COST SUMMARY

| Item | Cost | Frequency |
|---|---|---|
| 3 domains | ~$36 | Annual |
| Metricool Advanced | $54 | Monthly |
| Stripe fees | 2.9% + $0.30 | Per transaction |
| Riverside.fm (optional) | $24 | Monthly |
| **Everything else** | **$0** | **Already in your stack** |

**Total new monthly cost: $54-78/mo**
**First $99 enrollment pays for 1-2 months of new costs.**

---

## FILES

| File | Purpose |
|---|---|
| `SKILL-agentic50-launch.md` | This skill — launch checklist |
| `Desktop\LMT\AGENTIC-AGE-ARTICLE-SERIES-RESEARCH.md` | Full research + 8-article plan |
| `Desktop\LMT\SOCIAL-SETUP-STRATEGY-2026-04.md` | Social platform setup strategy |
| `Desktop\LMT\850-Billion-Series\PART-1-4-CONSOLIDATED-SCRIPT.md` | Video script reference |
| `podcast/podcast-concept.md` | Podcast concept (rename pending) |
| `podcast/podcast-submission-package.md` | Podcast platform submission package |
| `brand-constants.md` | Master brand rules |
| `video-builder/TEMPLATE-SHORT-VIDEO.json` | YouTube Short config template |
| `video-builder/TEMPLATE-FULL-VIDEO.json` | Full video config template |

---

## TRIGGER PHRASES

- "Set up agentic50"
- "Launch the Agentic 50 course"
- "Connect Stripe to LearnDash"
- "Submit podcast to Spotify"
- "Draft Article 1 for LinkedIn"
- "Build Module 1"
- "Schedule social posts for Agentic 50"

---

*Agentic50Launch — Learn More Technologies*
*Ship the minimum. Build in public. #Agentic50*
