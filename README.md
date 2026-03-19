# 50+TechBridge Content System
**LearnMoreTechnologies / 50+TechBridge**
**Mission:** Close the gap between the $76 trillion 50+ opportunity and the 5% of ad spend that reaches them.

---

## Repository Structure

```
50techbridge-content/
│
├── youtube-shorts/
│   ├── scripts/          ← V2 opportunity-tone scripts (active)
│   └── assets/           ← HTML backgrounds for recording
│
├── book/
│   └── book-architecture.md  ← Full outline: The Overlooked Trillion
│
├── skills/
│   └── yt-short-opportunity.md  ← Reusable Claude skill
│
├── archive/
│   └── scripts-v1-indictment-tone/  ← Original fighter-tone scripts
│
└── README.md
```

---

## YouTube Shorts — V2 Series (Opportunity Tone)

| Part | File | Theme | Closing line |
|---|---|---|---|
| 1 | part-1-the-number.md | The $76T stat | *"Now you can't say you didn't know."* |
| 2 | part-2-the-blind-spot.md | How the gap happened | *"Are you?"* |
| 3 | part-3-the-people.md | Real Pioneer stories | *"The opportunity is real."* |
| 4 | part-4-the-playbook.md | How to reach this market | *"Come learn it."* |
| 5 | part-5-the-invitation.md | The close | *"Come be part of what happens next."* |

---

## Book

**Title:** THE OVERLOOKED TRILLION
**Subtitle:** Why the World's Most Experienced Generation Is the Biggest Missed Opportunity of Our Time
**Full outline:** `book/book-architecture.md`
**Target:** ~83,000 words | 3 parts | 12 chapters
**TED angle:** "The $76 Trillion Opportunity the World Keeps Walking Past"

---

## Assets

| File | Use |
|---|---|
| `youtube-shorts/assets/ticker-bg.html` | News-ticker background — open in Chrome, record with OBS |
| `youtube-shorts/assets/animated-bg.html` | Scene-by-scene animated background |

---

## Reusable Skills

| Skill file | Command | Use |
|---|---|---|
| `skills/yt-short-opportunity.md` | `/yt-short-opportunity` | Generate full Short package, opportunity tone |
| `~/.claude/commands/yt-short.md` | `/yt-short` | Generate full Short package, fighter tone |

---

## Archive

`archive/scripts-v1-indictment-tone/` — Original 5-part series, fighter/indictment tone.
Still valid for community-facing social content and rally contexts.

---

## Production Workflow

```
1. Open ticker-bg.html in Chrome (1080x1920)
2. Record background — OBS or Windows Game Bar (Win+G)
3. Export HeyGen avatar — talking head, green screen, 1080p
4. Canva (1080x1920):
   a. Layer recorded background
   b. Upload HeyGen MP4 → remove BG → place lower third
   c. Add timed caption text overlays (see script files)
   d. Export MP4 1080p
5. Upload to YouTube as Short
6. Post cross-platform per script file
```

---

## Brand Constants

| Element | Value |
|---|---|
| Gold primary | `#F0D060` / `#C8A028` |
| Background | `#080F1F` |
| Font | Montserrat Black |
| Pioneers | 347+ trained |
| Partners | 45 organizations |
| CTA | learnmoretechnologies.com/join-now/ |

---

## Push to GitHub

```bash
git remote add origin https://github.com/1Profmac/50techbridge-content.git
git push -u origin master
```
*(Create repo at github.com/new first — recommended: private)*
