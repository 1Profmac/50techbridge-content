---
name: LMTMovieStudio
description: >
  Complete video production pipeline for Learn More Technologies.
  Three tools: workforce article videos, YouTube Shorts, and training lesson movies.
  Includes Galaxy AI clip creation, ElevenLabs voiceover, FFmpeg GPU rendering,
  YouTube upload package, and LinkedIn cross-post generation.
  Trigger this skill for ANY video production task at LMT.
---

# LMTMovieStudio — Video Production Skill
## Learn More Technologies | 50+TechBridge
### One pipeline. Three formats. All automated.

---

## WHAT THIS SKILL DOES

Takes raw inputs (HeyGen video, Galaxy clips, article text) and produces finished,
branded, platform-ready videos with text overlays, voiceover, and upload packages.

---

## THREE FORMATS

| Format | Tool | Use Case | Output |
|---|---|---|---|
| Landscape | `lmt-video-overlay.py` | Workforce article videos | 1920x1080 YouTube/LinkedIn |
| Lesson | `lmt-video-overlay.py` | Course lesson videos with Galaxy B-roll | 1920x1080 landscape, Brian PIP + clips |
| Short | `lmt-video-overlay.py` | YouTube Shorts, Reels, TikTok | 1080x1920 vertical, under 60s |
| Training | `lmt-movie-studio.py` | LearnDash course lessons (vertical) | 1080x1920 vertical, 2-10 min |

---

## TRIGGER PHRASES

- "New full video — here's my HeyGen recording [path] and my Canva clips [paths]. Use TEMPLATE-FULL-VIDEO."
- "New Short — here's my HeyGen recording [path]. Use TEMPLATE-SHORT-VIDEO."
- "Re-render [config name] — nothing has changed."
- "Make a video for article X"
- "Build a YouTube Short"
- "Create a training movie for lesson X"
- "Build a workforce video"

---

## REQUIREMENTS

| Tool | Location | Purpose |
|---|---|---|
| Python 3.10+ | System | Runs scripts |
| FFmpeg + NVIDIA NVENC | System PATH | GPU video rendering |
| ElevenLabs API | `.env` file (ELEVENLABS_API_KEY) | Brian's voice clone |
| Galaxy AI | Samsung device or Galaxy app | AI video clip generation |
| HeyGen | app.heygen.com | Brian talking head recordings |

---

## RULE — MANDATORY PRE-RENDER CHECKLIST (NEVER SKIP)

**This checklist runs EVERY TIME a render is requested. No exceptions.**
**Do NOT generate a config or run a render until every item is confirmed.**

### Step 1: Check Git
Run `git log --oneline -10` in `50techbridge-content/`
Find the last approved config. Copy it. Swap inputs. Never reinvent.

### Step 2: Confirm Standard Render Specs
Every config MUST use these values unless Brian explicitly overrides:

**Brian Talking Head:**
| Setting | Standard Value |
|---------|---------------|
| HeyGen background | **FULL GREEN SCREEN** — never navy, never white, never partial |
| Brian PIP width | `1920` |
| Brian PIP height | `1080` |
| Brian PIP position | `x: 0, y: 0` (full frame) |
| Brian PIP margin | `0` |
| Brian PIP border | `0` |
| Chromakey | `true` (green 0x00FF00) |
| Brian show_start | `0` (always visible) |
| Brian show_end | Full duration (always visible) |

**Text Overlays:**
| Setting | Standard Value |
|---------|---------------|
| Text color | `#FFFFFF` (white) — NEVER gold on video |
| Font size (content) | `70pt` |
| Font size (title/end card) | `84pt` |
| Justify | Left, `x: 80` |
| Center | `false` |
| y position (content) | `280` |
| y position (title/end) | `300` |
| Line spacing | `font_size + 16` |
| no_bullet | `true` |

**Layers and Chrome:**
| Setting | Standard Value |
|---------|---------------|
| bg_image | `layers/base/navy-1920x1080.png` |
| chrome_image | `layers/chrome/header-footer-1920x1080.png` |
| Show header | `true` (chrome PNG handles it — drawtext header auto-skips) |
| Show lower third | `true` (chrome PNG handles it) |

**B-Roll Clips:**
| Setting | Standard Value |
|---------|---------------|
| Clip source | `broll-clips/` only — NEVER use `stat-clips/` (text baked in) |
| Clip position | Full screen, BEHIND Brian (Brian is keyed on top) |
| Clip timing | Between text slides, no overlap |
| Brian visibility | ALWAYS visible — clips play behind him, never replace him |

**Rendering:**
| Setting | Standard Value |
|---------|---------------|
| GPU | NVIDIA NVENC |
| Pipeline | PIP mode (green screen Brian over navy bg + clips) |

### Step 3: Confirm with Brian
Show the config summary and get approval BEFORE running the render.

### Why This Exists
Brian had to correct render settings multiple times because specs drifted from the approved lesson configs. This checklist prevents that. These are the proven, approved values from commit `9b0130a` (lesson configs) updated with Brian's font size preference (70pt).

---

## FILES

| File | What It Does |
|---|---|
| `TEMPLATE-FULL-VIDEO.json` | **START HERE for full videos** — proven pattern, fill in REPLACE fields |
| `TEMPLATE-SHORT-VIDEO.json` | **START HERE for Shorts** — proven pattern, fill in REPLACE fields |
| `lmt-video-overlay.py` | All video rendering — lessons, LinkedIn, Shorts |
| `lmt-movie-studio.py` | Training lesson movies (vertical format) |
| `lesson1-config.json` | Lesson 1 config — tested and approved reference |
| `linkedin-ai-article-config.json` | LinkedIn AI article video — tested and approved |
| `workforce-article-1-config.json` | Workforce Article 1 config |
| `workforce-short-1-config.json` | Workforce Short 1 config |
| `galaxy-prompts/GALAXY-PROMPTS-ALL-LESSONS.md` | Canva/Galaxy scene prompts for all 3 lessons |

### Layer Assets (Photoshop-style)

| Layer | File | Purpose |
|---|---|---|
| Base | `layers/base/navy-1920x1080.png` | Navy background — never changes |
| Chrome | `layers/chrome/header-footer-1920x1080.png` | Solid navy bars + outlined gold text — never changes |
| Brian | `layers/brian/lesson-X-brian-nobg.mp4` | HeyGen talking head with GREEN SCREEN — per video |
| Clips | `layers/clips/lesson-X/` | B-roll clips (Canva Magic Media or Pexels) — per video |

### B-Roll Sources (ranked by preference)

| Source | Cost | Quality | Best For |
|---|---|---|---|
| Canva Magic Media | Free (Pro plan) | Good — modern, AI-generated | Custom scenes, 50+ adults in modern settings |
| Pexels API | Free | Good — real footage | Workforce/office scenes when Canva quality isn't enough |
| Galaxy AI (Sora 2 Pro) | $20/batch | Excellent | Only when budget allows, best quality |

### Key Technical Decisions (Proven — Do Not Change)

- **Brian: FULL GREEN SCREEN from HeyGen** — no navy, no white, no partial green. Full green keys cleanly.
- **HeyGen layout: ORIGINAL** (not Circle — Circle makes him a small avatar)
- **HeyGen content: NO titles, NO text baked in** — all branding comes from chrome PNG + text overlays
- **Chromakey:** `chromakey=color=0x00FF00:similarity=0.30:blend=0.08` — green screen removal
- **Brian PIP for full video:** `width:1920, height:1080, margin:0` — full frame, keyed over clips + navy bg
- **Brian ALWAYS visible** — show_start=0, show_end=full duration. Never hidden.
- **Clips play BEHIND Brian** — layer order: navy bg → clips (timed) → Brian (keyed) → chrome → text
- **B-roll clips only** — NEVER use stat-clips (they have text baked in that conflicts with our overlays)
- **Brian PIP for Short:** Brian IS the main video (no PIP), text slides overlay at y=200
- **Text:** Left justified x=80, font_size 70 (content) / 84 (titles), white #FFFFFF, y=280 / y=300
- **Line spacing:** font_size + 16
- **Chrome PNG:** `layers/chrome/header-footer-1920x1080.png` — contains header + footer. When chrome is used, drawtext header/footer auto-skips (no double header).
- **Clips trimmed:** To exact duration, no frozen frames
- **Audio:** Brian's HeyGen audio only — clip audio is ignored
- **GPU:** NVIDIA NVENC

---

## WORKFLOW 1: WORKFORCE ARTICLE VIDEO

### Input
- Clean HeyGen video of Brian talking (no text overlays, navy background)
- Article PLAINTEXT.txt (from TRACK-1 or TRACK-2 folder)

### Steps
1. Brian records in HeyGen — clean, landscape 1920x1080, no text
2. Export MP4 to `_NEW-SESSION-TEMPLATE/heygen-workforce/`
3. Write config.json — map article sections to timed slides
4. Run: `python lmt-video-overlay.py config.json`
5. Output: finished video + YouTube package + LinkedIn post

### Config Settings
```json
{
  "format": "landscape",
  "input_video": "path/to/heygen-clean.mp4",
  "output_video": "path/to/FINISHED/video.mp4",
  "show_header": true,
  "show_lower_third": true
}
```

### Slide Rules
- All text: `#FFFFFF` white — NEVER gold over video (unreadable)
- Font size: `70pt` for content, `84pt` for title and end card
- Left justified: `"center": false, "x": 80`
- y position: `280` (content) / `300` (title/end)
- Line spacing: `font_size + 16`
- Slide timing: NEVER overlap — each slide must end before the next begins
- Slide timing: NEVER overlap with clip timing — slides show between or during clips, not conflicting
- End card: last 20 seconds, `no_bullet: true`, contact info + CTA
- No percent symbol — spell out "percent"
- Blank `""` entries in bullets are ignored (not rendered, no spacing impact)
- NEVER use stat-clips — they have text baked in that conflicts with overlay text

### Output Package
```
FINISHED/YOUTUBE/
├── video.mp4
├── THUMBNAIL.png (1280x720)
├── YOUTUBE-TITLE.txt
├── YOUTUBE-DESCRIPTION.txt (with chapters)
├── YOUTUBE-TAGS.txt
└── LINKEDIN-POST.txt
```

### Publishing
1. YouTube: Upload to studio.youtube.com, paste from .txt files
2. LinkedIn: Upload same MP4 natively (never paste YouTube link — native gets 3-5x more reach)

---

## WORKFLOW 2: YOUTUBE SHORT

### Input
- Clean HeyGen video of Brian (vertical 1080x1920, 50 seconds)
- Short script from `youtube-shorts/scripts/`

### Steps
1. Brian records in HeyGen — clean, vertical 1080x1920, 50 seconds
2. Export MP4
3. Write config.json with `"format": "short"`
4. Run: `python lmt-video-overlay.py config.json`

### Config Settings
```json
{
  "format": "short",
  "show_header": true,
  "show_lower_third": true
}
```

### Slide Rules
- Font size: `42pt`
- x: 60, y: 200
- 5-8 slides max
- Under 60 seconds total

---

## WORKFLOW 3: LESSON VIDEO (with Galaxy B-roll)

### Layer System (Photoshop-style)
Assets are separated into layers — swap any file to change the look without code changes.

```
layers/
├── base/                              LAYER 0 — Background
│   └── navy-1920x1080.png             Solid navy #0E1C2F
│
├── chrome/                            LAYER 1 — Header + Footer
│   └── header-footer-1920x1080.png    Transparent PNG, gold titles + subscribe bar
│
├── brian/                             LAYER 2 — Talking Head Video
│   └── lesson-1-brian-nobg.mp4        Brian from HeyGen, NO background (white/transparent)
│   └── lesson-2-brian-nobg.mp4
│   └── lesson-3-brian-nobg.mp4
│
├── clips/                             LAYER 3+ — B-Roll Video Clips
│   ├── lesson-1/                      Galaxy AI clips, ~1.5 min each
│   │   ├── clip-01-videocall-grandkids.mp4
│   │   ├── clip-02-couple-tablet.mp4
│   │   └── ...
│   ├── lesson-2/
│   └── lesson-3/
```

### Layout (1920x1080 landscape)
```
┌──────────────────────────────────────────┐
│  ──── LEARN MORE TECHNOLOGIES ────       │  CHROME layer (top)
│           50+TechBridge                  │
│──────────────────────────────────────────│
│                                          │
│   [Text overlays]              [Brian]   │  BRIAN layer (always visible,
│   Center-justified, 84pt      [talking]  │  lower right, no background)
│   Full opacity, no fade       [ head ]   │
│                                          │
│   [Galaxy clips play FULL SCREEN]        │  CLIPS layer (timed)
│   [on top of BASE, behind Brian]         │
│                                          │
│  Subscribe   |   Like   |   Share        │  CHROME layer (bottom)
└──────────────────────────────────────────┘

BASE layer: navy-1920x1080.png (always, underneath everything)
```

### How It Works
1. **Base** (`layers/base/`) — Navy background, always visible
2. **Clips** (`layers/clips/lesson-X/`) — Galaxy B-roll, full screen at timed moments
3. **Brian** (`layers/brian/`) — Talking head with no background, lower right, always visible
4. **Chrome** (`layers/chrome/`) — Header + footer baked into transparent PNG, always on top
5. **Text** (config.json) — Center-justified overlays rendered at runtime

### Input
- Brian talking head with NO background (`layers/brian/lesson-X-brian-nobg.mp4`)
- Galaxy AI clips (`layers/clips/lesson-X/`)
- Layer assets (`layers/base/`, `layers/chrome/`)

### Steps
1. Drop Brian's no-bg video into `layers/brian/`
2. Drop Galaxy clips into `layers/clips/lesson-X/`
3. Copy `lesson1-config.json` and set clip timing + text slides
4. Run: `python lmt-video-overlay.py lesson-X-config.json`
5. Output: finished video + YouTube package + all platform formats

### Config Format
```json
{
  "format": "landscape",
  "input_video": "layers/brian/lesson-1-brian-nobg.mp4",
  "output_video": "path/to/FINISHED/lesson-1.mp4",
  "bg_image": "layers/base/navy-1920x1080.png",
  "show_header": false,
  "show_lower_third": false,
  "clips": [
    {"file": "layers/clips/lesson-1/clip-01-videocall-grandkids.mp4", "start": 14, "end": 104}
  ],
  "slides": [
    {
      "start": 0, "end": 10,
      "y": 250, "font_size": 84,
      "color": "#FFFFFF", "fade": 0, "center": true,
      "no_bullet": true,
      "bullets": ["Line 1", "Line 2"]
    }
  ]
}
```

### Slide Rules for Lessons
- Font size: `84pt` (doubled for readability)
- Center-justified: `"center": true`
- Full opacity: `"fade": 0`
- No bullets for statements: `"no_bullet": true`
- CTA end card in gold: `"color": "#C8942E"`
- Galaxy clips are ~1.5 min each, fill gaps between text slides

---

## WORKFLOW 4: TRAINING LESSON MOVIE

### Input
- HeyGen lesson video of Brian talking (from `heygen-lessons/`)
- Galaxy AI clips (from `galaxy-clips/lesson-X/`)
- OR stock images from organized image library
- Voiceover from ElevenLabs (or use HeyGen audio)

### Steps
1. Write Galaxy prompts (or use existing from `galaxy-prompts/`)
2. Create clips in Galaxy AI (8-10 seconds each, landscape)
3. Save clips to `galaxy-clips/lesson-X/`
4. Write config.json mapping clips to scenes
5. Run: `python lmt-movie-studio.py config.json`

### Layout (1080x1920 vertical)
```
┌─────────────────────────┐
│    LEARN MORE            │
│    TECHNOLOGIES          │  Top — Header (90pt, gold)
│    50+TechBridge         │         (52pt, orange)
│─────────────────────────│
│                          │
│   Galaxy Clip            │  Middle — content area
│   or                     │  Image/clip first half
│   Text Bullet Points     │  Text second half
│                          │  (alternating)
│                          │
│──────────────────────────│
│                          │
│   Brian Talking Head     │  Bottom 1/3 — persistent
│                          │
│  Subscribe | Like | Share│
└─────────────────────────┘
```

### Config Settings
```json
{
  "output_video": "path/to/LESSON-1.mp4",
  "brian_image": "path/to/brian-talking-head.png",
  "scenes": [
    {
      "image": "path/to/slide.jpg",
      "clip": "path/to/galaxy-clip.mp4",
      "audio": "path/to/voiceover.mp3",
      "text": ["Point 1", "Point 2"],
      "font_size": 56,
      "no_bullet": true
    }
  ]
}
```

### Scene Rules
- Use `"image"` for still images, `"clip"` for video clips
- Image/clip shows first half of scene
- Text shows second half (no overlap)
- Font size: `52-60pt` (ADA readable for 50+ adults)
- Brian stays on screen entire video

---

## GALAXY AI CLIP CREATION

### How to Create Clips
1. Open Galaxy AI on Samsung device
2. Select Video Generation
3. Paste scene description from `galaxy-prompts/` folder
4. Set: 8-10 seconds, 16:9 landscape, 1080p
5. Generate, review, download MP4
6. Save to `galaxy-clips/lesson-X/` with exact filename

### "Close Friend" Morph Concept
The core visual concept: the device morphs into a close friend.
Technology is not cold or foreign — it is a warm companion.

**Prompt Pattern:**
```
A [ethnicity] [gender] in their [60s/70s] in their [setting]
using a [device]. They speak to the [device] warmly as if
speaking to a close friend. The [device] screen softly glows
and dissolves into a warm friendly face that [responds/smiles/
nods]. The person relaxes and smiles. Warm [lighting type].
The technology feels human, not mechanical.
```

**Scenarios to create:**
- Phone morphs to doctor (telehealth)
- Tablet morphs to friend (shopping/recipes)
- Blood pressure monitor morphs to caring companion (health)
- Smart speaker morphs to helpful friend (daily tasks)
- Laptop morphs to patient teacher (learning)
- Video call expands to real presence (family connection)

### Image Rules for All Clips
- Adults must look 60+ (grey hair, mature faces)
- Diverse: Black, Latino, Asian, White — men and women equally
- Real domestic settings: kitchen, living room, doctor office
- Warm golden lighting — never cold, harsh, or clinical
- People look confident and in control — never confused
- Devices are natural parts of life — not foreign objects
- Never use: "senior", "elderly", condescending expressions

---

## ELEVENLABS VOICEOVER

### API Setup
- Key stored in `.env` file: `ELEVENLABS_API_KEY=sk_...`
- Brian's voice clone ID: `uAs0vN0GLLpz7FM7JVkz`
- Model: `eleven_multilingual_v2`

### Generate Voiceover
```python
import urllib.request, json

api_key = "your-key"
voice_id = "uAs0vN0GLLpz7FM7JVkz"

data = json.dumps({
    "text": "Your script text here",
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}
}).encode()

req = urllib.request.Request(
    f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}",
    data=data,
    headers={"xi-api-key": api_key, "Content-Type": "application/json"}
)
resp = urllib.request.urlopen(req)
with open("output.mp3", "wb") as f:
    f.write(resp.read())
```

---

## BRAND CONSTANTS

| Element | Value |
|---|---|
| Navy background | #0E1C2F |
| Gold header | #C8942E |
| Orange subheading | #E8733A |
| White content text | #FFFFFF |
| Muted source text | #A8B8CC |
| Green badges | #109F35 |
| Navy mid (lower third) | #162640 |
| Heading font | Georgia Bold (C:/Windows/Fonts/georgiab.ttf) |
| Body font | Arial (C:/Windows/Fonts/arial.ttf) |

---

## FILE LOCATIONS

```
_NEW-SESSION-TEMPLATE/
├── heygen-lessons/
│   ├── Lesson-Intro-HeyGen-Brian.mp4
│   ├── Lesson-1-HeyGen-Brian.mp4
│   ├── Lesson-2-HeyGen-Brian.mp4
│   └── Lesson-3-HeyGen-Brian.mp4
├── heygen-workforce/
│   ├── Workforce-1-HeyGen-Clean.mp4
│   └── Workforce-2-HeyGen.mp4
├── galaxy-clips/
│   ├── lesson-1/  (Galaxy AI clips for Lesson 1)
│   ├── lesson-2/
│   └── lesson-3/
├── podcast/
└── skills/

ASSETS/03-video/
├── video-builder/
│   ├── lmt-video-overlay.py
│   ├── lmt-movie-studio.py
│   └── configs...
├── TRACK-1-WORKFORCE/  (article videos)
└── TRACK-2-BOOK/  (book post videos)
```

---

## 30 VIDEOS IN 30 DAYS CHECKLIST

### Week 1-4: Book Posts (TRACK-2)
- [ ] Record 8 HeyGen Shorts (vertical, 50 sec each)
- [ ] Create configs from post scripts
- [ ] Run lmt-video-overlay.py for each
- [ ] Upload to YouTube + LinkedIn native

### Week 5-9: Workforce Articles (TRACK-1)
- [ ] Record 5 HeyGen videos (landscape, 4-5 min each)
- [ ] Create configs from article PLAINTEXTs
- [ ] Run lmt-video-overlay.py for each
- [ ] Upload to YouTube + LinkedIn native

### Ongoing: Training Lessons
- [ ] Create Galaxy clips per lesson (8 clips each)
- [ ] Generate ElevenLabs voiceover per section
- [ ] Run lmt-movie-studio.py for each lesson
- [ ] Upload to YouTube + embed in LearnDash

---

## RENDER TIMES

| Format | Duration | Render Time |
|---|---|---|
| Landscape (4-5 min) | ~288 seconds | Under 2 minutes |
| Short (50 sec) | ~50 seconds | Under 30 seconds |
| Training (3 min) | ~170 seconds | Under 2 minutes |

All renders use NVIDIA NVENC GPU acceleration via FFmpeg.
Falls back to CPU (libx264) if NVENC unavailable — 10-15x slower.

---

*LMTMovieStudio — Learn More Technologies*
*Build. Test. Commit.*
