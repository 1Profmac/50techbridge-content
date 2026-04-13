# LMT Desktop Folder — Map & Download Protocol

**Owner:** Brian McKinney
**Last cleanup:** 2026-04-08
**Why this file exists:** Brian uses files in this folder to create content. When files are missing or in the wrong place, his flow breaks. This README is the canonical map.

---

## 🗂 Folder Map

```
Desktop/LMT/
├── README.md                       ← THIS FILE — canonical folder map
├── DOWNLOADS-LOG.md                ← chronological log of every new download
├── LINKEDIN-CONTENT-INDEX.md       ← every LinkedIn file across folders + git, by type
├── Canva-Cheat-Sheet.md            ← Premiere → Canva translation + 6-layer architecture + shortcuts (open on 2nd monitor while building)
│
├── marketing/                      ← LOCAL SNAPSHOT of all marketing files from git
│   ├── README.md                   ← editing rules + sync instructions
│   ├── (29 marketing strategy + content + dossier files mirrored from git)
│   └── prospects/                  ← all prospect dossiers (Alan, Carly, Jessica, Jason, David)
│
├── 04-ASSETS/                      ← Raw source assets (images, b-roll, screenshots)
│   ├── CHUNK1 broll-clips/
│   ├── CHUNK2 broll-clips/
│   ├── content-drafts/
│   ├── screenshots/
│   ├── stat-clips/
│   └── youtube-shorts/
│
├── 850-Billion-Article/            ← THE manifesto article + companion content
│   ├── article-its-not-about-the-data.md           ← MARKDOWN MASTER
│   ├── article-its-not-about-the-data-plaintext.txt
│   ├── linkedin-article-version.md
│   ├── linkedin-short-post-show-a-friend.md
│   ├── 850-Billion-Article-LinkedIn.md             ← OLD draft (predates today's article)
│   ├── REFERENCES.txt
│   ├── Valuing 50+ Workforce.pdf
│   ├── images/                                     ← LittleMissMatched + future article images
│   │   ├── littleMisMatch.png
│   │   └── littlemissmatched-alt.png
│   └── Bridge-Episode/                             ← All bridge video build files
│       ├── bridge-video-script.md                  ← HeyGen narration (paste-ready)
│       ├── bridge-video-canva-broll-script.md     ← 14-segment b-roll spec
│       ├── bridge-video-canva-broll-plaintext.txt ← plain text version
│       ├── bridge-video-canva-build-guide.md      ← step-by-step Canva build
│       ├── bridge-video-motion-map.md             ← pre-decided motion choices
│       └── lmt-broll-production-recipe.md         ← REUSABLE recipe for ALL future LMT videos
│
├── 850-Billion-Series/             ← Video production assets (the 4-part YouTube series)
│   │
│   │   🎬 SELF-CONTAINED PROJECT FOLDERS (final cleanup 2026-04-09)
│   │      Every video project has the SAME 4-subfolder structure:
│   │        ALL-FORMATS/  ← master MP4 + landscape/square/vertical + thumbnails
│   │        B-Roll/        ← HeyGen fullGreen source + all b-roll clips this part uses
│   │        LINKEDIN/      ← LinkedIn post caption
│   │        Youtube/       ← title, description, tags, pinned-comment, Shorts/ subfolder
│   │
│   ├── Part-1/                     ← The $850 Billion Problem Nobody Sees
│   │   ├── ALL-FORMATS/            (FINISHED.mp4, LANDSCAPE-1920x1080, THUMBNAIL-1280x720, master thumbnail)
│   │   ├── B-Roll/                 (Chap1 fullGreen + CHUNK-1-fullGreen-ALTERNATE + 5 clip-XX files)
│   │   ├── LINKEDIN/               (PART-1-LINKEDIN-POST.txt)
│   │   └── Youtube/                (4 metadata files: title, description, tags, pinned-comment)
│   │
│   ├── Part-2/                     ← What You're Really Losing
│   │   ├── ALL-FORMATS/            (FINISHED + 4 variant exports + thumbnails)
│   │   ├── B-Roll/                 (CHUNK-2 fullGreen + 2 SHORT-retention sources + 5 Video X files)
│   │   ├── LINKEDIN/               (PART-2-LINKEDIN-POST.txt)
│   │   └── Youtube/                (4 metadata files + Shorts/ subfolder with PART-2-SHORT-FINISHED.mp4)
│   │
│   ├── Part-3/                     ← What Winning Organizations Do Differently (master/model)
│   │   ├── ALL-FORMATS/            (FINISHED + 4 variant exports + thumbnails)
│   │   ├── B-Roll/                 (CHUNK-3 fullGreen + 4 SEGMENT files + B-ROLL WITH CAPTIONS)
│   │   ├── LINKEDIN/               (LINKEDIN-POST.txt)
│   │   └── Youtube/                (6 metadata files)
│   │
│   ├── Part-4/                     ← The Decision on Your Desk Right Now
│   │   ├── ALL-FORMATS/            (FINISHED + LANDSCAPE + thumbnails)
│   │   ├── B-Roll/                 (CHUNK-4 fullGreen + 5 clip-XX files — copies of Part 1's set)
│   │   ├── LINKEDIN/               (PART-4-LINKEDIN-POST.txt)
│   │   └── Youtube/                (3 metadata files)
│   │
│   ├── BRIDGE/                     ← Legacy folder, has the wrong-script HeyGen render
│   │   └── NEEDS-RERENDER_*.mp4    ← Re-render and replace when ready
│   │
│   ├── B-Roll/                     ← Global library (Prompts/Scripts only — no source clips here)
│   │   ├── Prompts-and-Scripts/    ← Reference docs (BROLL-PROMPTS-CHUNK-1..4.md, Manus-2026-04-06/, etc)
│   │   └── 850-BILLION-MARKETING-PLAYBOOK.md
│   │
│   ├── FINAL/                      ← Existing folder
│   └── PRODUCTION-PLAN.md
│   ├── BRIDGE/                     ← Bridge episode (between Parts 3 and 4)
│   │   └── NEEDS-RERENDER_*.mp4    ← HeyGen render with WRONG SCRIPT — must re-render
│   ├── FINAL/                      ← Final exports
│   ├── YOUTUBE/                    ← Per-part folders with FINISHED + ALL-FORMATS
│   │   ├── PART-1/, PART-2/, PART-3/, PART-4/
│   │   └── ALL-FORMATS/
│   ├── PART-2-FINISHED-OLD-recycled-broll-20260405.mp4
│   ├── PART-2-SHORT-FINISHED.mp4
│   ├── PRODUCTION-PLAN.md
│   └── The $850 Billion Cost of Ignoring Experienced Workers Chap1 fullGreen_1080p.mp4
│
├── Elevenlabs/                     ← ElevenLabs audio + chunk source scripts
│   ├── CHUNK-1-of-4.txt … CHUNK-4-of-4.txt
│   ├── ELEVENLABS-RENDER-READY.txt
│   ├── ELEVENLABS-SETTINGS.txt
│   └── ElevenLabs_*.mp3
│
├── Research/                       ← External research PDFs + source documents
│   └── AARP-Valuing-the-Invaluable-2026.pdf        ← Downloaded 2026-04-08
│
├── html/                           ← WordPress block HTML (paste into WP Code Editor)
│   ├── article-its-not-about-the-data-wp.html
│   ├── LMT-Workforce-Page-v2-template.html
│   ├── LMT_Train_Page_FIXED.html
│   ├── train-hero-video-fix-snippet.html
│   └── workforce-hero-video-snippet.html
│
├── ops-misc/                       ← Operations docs (not content)
│   ├── COO-Maya-system-prompt-UPDATED.md
│   └── CREDENTIAL-ROTATION-CHECKLIST.md
│
├── 20260406Manus B-Roll/           ← B-Roll generated by Manus 2026-04-06 (legacy)
│
└── _INBOX/                         ← Temporary holding for new downloads — empty by Friday each week
```

---

## 📥 OFFICIAL DOWNLOAD PROTOCOL (effective 2026-04-08)

**Every new file Brian downloads or saves to the LMT folder follows this protocol:**

### Step 1 — Save to the right subfolder (NOT root)
| Type of file | Where it goes |
|---|---|
| Research PDFs / external reports | `Research/` |
| Article markdown / drafts | `850-Billion-Article/` |
| Bridge video build files | `850-Billion-Article/Bridge-Episode/` |
| HeyGen video renders | `850-Billion-Series/BRIDGE/` (or appropriate part folder) |
| WordPress HTML | `html/` |
| Reference images for articles | `850-Billion-Article/images/` |
| Source b-roll clips | `850-Billion-Series/B-Roll/` |
| ElevenLabs audio | `Elevenlabs/` |
| Brand/operations docs | `ops-misc/` |
| Anything else (temporary) | `_INBOX/` (clean up by Friday) |

**🛑 NOTHING goes in `Desktop/LMT/` root except this README and the DOWNLOADS-LOG.**

### Step 2 — Log it
Append a row to `DOWNLOADS-LOG.md` with:
- Date/time
- Filename
- Source (URL or "manually created")
- Destination subfolder
- Why it was saved

### Step 3 — Mirror to git when applicable
| File type | Git destination |
|---|---|
| Research PDFs | `50techbridge-content/marketing/research/` (only if licensing permits) |
| Article markdown / scripts | `50techbridge-content/marketing/` |
| Brand docs / configs | `lmt-claude-brain/` |
| WordPress HTML | `lmt-claude-brain/pages/` |
| Video renders | **Local only — too large for git** |
| Raw b-roll clips | **Local only — too large for git** |

### Step 4 — When Claude downloads something for Brian
**Claude MUST do all 4 steps automatically** — save to the right subfolder, log it, mirror to git, and tell Brian where it went. No more "I can't find it" moments.

---

## 🚫 What's NOT in the LMT folder

These live elsewhere:
- **Git repos:** `C:\Users\USER\Documents\lmt-claude-brain\` and `C:\Users\USER\Documents\50techbridge-content\`
- **Memory:** `C:\Users\USER\.claude\projects\C--Users-USER\memory\`
- **Browser downloads (default):** `C:\Users\USER\Downloads\` (move them to LMT subfolders ASAP)

---

## 🔄 Last cleanup actions (2026-04-08 PM)

1. Created `850-Billion-Article/Bridge-Episode/` and moved 6 bridge video files into it (out of root)
2. Created `850-Billion-Article/images/` and moved 2 LittleMissMatched images into it (out of root)
3. Created `850-Billion-Series/BRIDGE/` and moved the wrong-script HeyGen render into it (renamed `NEEDS-RERENDER_*`)
4. Created `Research/` (already done earlier today) and copied AARP Valuing the Invaluable 2026 PDF into it
5. Removed 2 duplicate bridge files from `850-Billion-Article/` root
6. Wrote this README

**Result:** `Desktop/LMT/` root went from **8 stray files + 9 folders** → **0 stray files + 9 folders + this README**.

---

## Maintenance

- **Weekly (Friday):** Empty `_INBOX/` — every file in there gets moved to the right subfolder OR deleted
- **Monthly:** Re-read this README, update if folders have shifted
- **Anytime files start dumping in root:** RUN THE CLEANUP. The root is sacred.
