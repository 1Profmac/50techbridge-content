---
name: KeynotePipeline
description: >
  Master strategy for getting Professor Brian McKinney from article to keynote stage.
  End-to-end content production + distribution + booking pipeline.
  Updated April 13, 2026 after podcast launch and video series completion.
---

# Get to the Front of the Stage — Master Strategy
## Professor Brian McKinney · Learn More Technologies · #AGENTIC50
### Updated: April 13, 2026

---

## BRAND ARCHITECTURE

```
LEARN MORE TECHNOLOGIES (parent company, MBE Certified)
├── 50+TechBridge (B2B — workforce training for organizations)
│   └── learnmoretechnologies.com/workforce
│
├── #AGENTIC50 (B2C — individuals building businesses after 50)
│   ├── #AGENTIC50 — The Pioneers Podcast (Buzzsprout → all platforms)
│   ├── YouTube @LearnMoreTechnologies (videos + podcast)
│   ├── LinkedIn /brianmckinneylmt (articles + posts)
│   └── learnmoretechnologies.com/speak (booking page)
│
└── The $850 Billion Series (flagship content — 4 parts complete)
```

---

## THE PIPELINE — Book to Keynote Stage

### Stage 1: WRITE
```
Source: Book chapter OR new topic from Content Calendar
  ↓
Output: LinkedIn long-form article (~1000-1500 words)
Tool: Claude Code
File: ARTICLES/[topic-name]/article.md
```

### Stage 2: VOICE
```
Source: Article text
  ↓
Output: ElevenLabs voiceover chunks (MP3)
Tool: ElevenLabs (Brian McKinney voice clone)
Settings: Multilingual v2, Stability 50%, Similarity 75%, Style 0
File: Elevenlabs/[episode-name]/CHUNK-X-of-Y.txt
```

### Stage 3: VIDEO — Talking Head
```
Source: Voiceover or live recording
  ↓
Output: Green screen talking head (1920x1080, H.264)
Tool: HeyGen (Brian avatar) OR live recording
File: [series]/B-Roll/[name]-fullGreen.mp4
```

### Stage 4: VIDEO — B-Roll
```
Source: B-Roll prompts (matched to voiceover timestamps)
  ↓
Output: 5-9 clips, 20 sec each, 1920x1080
Tool: Canva Magic Media
File: [series]/B-Roll/clip-01-[name].mp4 through clip-09-[name].mp4
```

### Stage 5: RENDER
```
Source: Talking head + B-Roll + render config JSON
  ↓
Output: Branded video with text overlays, header, lower third
Tool: lmt-video-overlay.py (NVIDIA GPU rendering)
File: [series]/ALL-FORMATS/[name]-FINISHED.mp4
```

### Stage 6: RESIZE
```
Source: Finished landscape video
  ↓
Output: 4 formats + thumbnail
Tool: auto_resize() in lmt-video-overlay.py
Files:
  - FINISHED-LANDSCAPE-1920x1080.mp4 (YouTube, LinkedIn)
  - FINISHED-VERTICAL-1080x1920.mp4 (Shorts, Reels, TikTok)
  - FINISHED-SQUARE-1080x1080.mp4 (Instagram, Facebook)
  - FINISHED-THUMBNAIL-1280x720.png (YouTube thumbnail)
```

### Stage 7: DISTRIBUTE
```
Use: /repurpose-content skill

Platform          | Format              | When
YouTube Long      | Landscape MP4       | Tuesday AM
YouTube Short     | Vertical MP4        | Thursday AM
LinkedIn Article  | Text + video embed  | Tuesday AM
LinkedIn Post     | Short + video link  | Thursday AM
Podcast (Buzzsprout) | MP3 audio        | Tuesday (auto-distributes)
  → Spotify       | Auto via RSS
  → Apple         | Auto via RSS
  → Amazon        | Auto via RSS
  → iHeartRadio   | Auto via RSS
  → YouTube Pod   | Auto via RSS
Facebook          | Square MP4 + post   | Tuesday PM
Instagram         | Square + Reel       | Thursday PM
Email Newsletter  | Mailchimp           | Wednesday
Blog Post         | WordPress /blog     | Tuesday (SEO)
```

---

## WHAT'S DONE (as of April 13, 2026)

### Content
- [x] Book Draft 1 — 11 chapters, 20,200 words
- [x] 10 articles written (Content Calendar has full list)
- [x] 8 LinkedIn short posts written (Overlooked Workforce series)
- [x] Content Calendar — 30 articles planned with publishing schedule
- [x] WIOA Mandate article — written and in git

### Video
- [x] $850 Billion Series — 4 parts rendered, all formats
- [x] How to Start a Business Online After 50 — rendered, all formats
- [x] Bridge: It's About the People — rendered, all formats
- [x] Part 4 re-rendered with fixed B-Roll/text timing
- [x] Part 1 missing formats (vertical + square) — generated

### Podcast
- [x] #AGENTIC50 — The Pioneers Podcast — live on Buzzsprout
- [x] 4 episodes published (audio from $850B videos)
- [x] Distributed to: Spotify, Apple, Amazon, iHeartRadio, YouTube
- [x] 3 full-length episode scripts written (EP5-7)
- [x] ElevenLabs chunks ready for EP5-7 (10 + 9 + 14 chunks)
- [x] Podcast cover art — #AGENTIC50 logo (3000x3000, 1400x1400)

### Brand Assets
- [x] #AGENTIC50 circular logo stamp (SVG + PNG + HTML variants)
- [x] RCA 77-DX microphone icon
- [x] Business card v3 — print-ready PNGs + print package
- [x] QR code → /speak (real, scannable)
- [x] YouTube banner — 2560x1440

### Platforms
- [x] YouTube — 15 videos, podcast tab, banner updated
- [x] LinkedIn — Premium active, articles posted, 603 impressions
- [x] Buzzsprout — hosting, auto-distributes to all podcast platforms
- [x] Facebook — page set up: /learnmoretechnologies
- [x] Instagram — @50plustechbridge
- [x] Website — /workforce (SEO block), /speak (SEO block), /courses

### Tools
- [x] lmt-video-overlay.py — GPU rendering pipeline
- [x] LMTMovieStudio skill — 3 video formats
- [x] RepurposeContent skill — 7 outputs per content
- [x] Agentic50Launch skill — course + launch checklist
- [x] ElevenLabs voice clone — Brian McKinney, settings locked
- [x] HeyGen — talking head pipeline

### SEO
- [x] /workforce indexed on Google, SEO block added
- [x] /speak SEO block added, indexing requested
- [x] 51 broken 404s fixed via .htaccess redirects
- [x] Yoast SEO Premium active

### Booking
- [x] Business card with QR → /speak
- [x] Decision-Maker Access Playbook — 16 channels documented
- [x] Prospects pipeline started (AARP, Jessica Lemann, etc.)

---

## WHAT'S NOT DONE (Priority Order)

### Critical — Do This Week
- [ ] **Speaking sizzle reel** — 2 min cut from Parts 1-4 best moments
- [ ] **Post Article #2** on LinkedIn (Untapped Asset) — Tuesday
- [ ] **Post Overlooked Workforce Post 1** — Thursday
- [ ] **Record EP5 "Is It Too Late?"** via ElevenLabs (chunks ready)
- [ ] **Upload YouTube Shorts** — vertical videos exist, not posted yet

### High — Do This Month
- [ ] **Post remaining 8 written articles** — 2x/week for 4 weeks
- [ ] **Record EP6-7** via ElevenLabs
- [ ] **Add sizzle reel to /speak page**
- [ ] **Add sizzle reel to LinkedIn featured section**
- [ ] **First email newsletter** via Mailchimp
- [ ] **First FB + IG posts** — square videos from existing content
- [ ] **Publish articles as WordPress blog posts** — SEO value
- [ ] **Part 4 — generate remaining 8 B-Roll clips** in Canva Magic Media
- [ ] **Apply mobile-fix.css** to website

### Medium — Do Next Month
- [ ] **Agentic 50 course** — build Module 1 in LearnDash (skill exists)
- [ ] **Stripe payment** — connect to LearnDash
- [ ] **Buy agentic50.com** domain
- [ ] **Metricool upgrade** — auto-scheduling across platforms
- [ ] **LinkedIn Newsletter** setup
- [ ] **LinkedIn carousel templates** in Canva
- [ ] **Attend first workforce board meeting** (per Decision-Maker Playbook)

### Low — Future
- [ ] **LinkedIn Live** Q&A session
- [ ] **X/Twitter** account setup (stuck, retry)
- [ ] **TikTok** account
- [ ] **Book publication** — Draft 1 complete, needs editing
- [ ] **Buzzsprout upgrade** — before July 11 trial expiry

---

## WEEKLY RHYTHM

| Day | Action |
|-----|--------|
| **Monday** | Write/review next article. Prep ElevenLabs chunks. |
| **Tuesday** | Post LinkedIn article + YouTube long video + podcast episode |
| **Wednesday** | Email newsletter. Respond to LinkedIn comments. |
| **Thursday** | Post LinkedIn short post + YouTube Short + IG Reel |
| **Friday** | Review analytics. One Decision-Maker Playbook action. |
| **Weekend** | Record HeyGen talking head. Generate Canva B-Roll. |

---

## THE KEYNOTE BOOKING FUNNEL

```
STRANGER → sees you on 1 platform
  ↓
AWARE → sees you 3+ times (YouTube + LinkedIn + podcast)
  ↓
INTERESTED → visits /speak or clicks LinkedIn profile
  ↓
ENGAGED → watches sizzle reel, reads credentials
  ↓
BOOKED → fills out form or scans QR → calendly
  ↓
KEYNOTE STAGE → you deliver, they share, cycle repeats
```

**The strategy is simple: be everywhere with the same message, backed by data, until they can't ignore you.**

---

## FILES IN GIT

| File | What |
|------|------|
| `skills/MASTER-STRATEGY-KEYNOTE-PIPELINE.md` | This file — master strategy |
| `skills/repurpose-content.md` | Auto-repurpose skill |
| `skills/yt-short-opportunity.md` | YouTube Short generation |
| `video-builder/SKILL-lmt-movie-studio.md` | Video production pipeline |
| `video-builder/SKILL-agentic50-launch.md` | Course + brand launch |
| `marketing/DECISION-MAKER-ACCESS-PLAYBOOK.md` | 16 channels to reach decision makers |
| `marketing/PROSPECTS-INDEX.md` | Active prospect pipeline |
| `content/CONTENT-CALENDAR.md` | 30 articles planned + schedule |
| `podcast/BUZZSPROUT-FREE-TRIAL-STRATEGY.md` | Podcast hosting plan |
| `brand-constants.md` | Master brand rules |
| `book/CONTENTS.md` | Book table of contents |

---

*One pipeline. Every platform. Every week. Until you're on stage.*
*#AGENTIC50 — You're not done yet.*
