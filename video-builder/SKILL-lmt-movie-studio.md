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
| Short | `lmt-video-overlay.py` | YouTube Shorts, Reels, TikTok | 1080x1920 vertical, under 60s |
| Training | `lmt-movie-studio.py` | LearnDash course lessons | 1080x1920 vertical, 2-10 min |

---

## TRIGGER PHRASES

- "Make a video for article X"
- "Build a YouTube Short"
- "Create a training movie for lesson X"
- "Generate Galaxy clips for lesson X"
- "Build a workforce video"
- "Make a lesson video"

---

## REQUIREMENTS

| Tool | Location | Purpose |
|---|---|---|
| Python 3.10+ | System | Runs scripts |
| FFmpeg + Intel QSV | `C:/tools/ffmpeg-8.1-essentials_build/bin/` | GPU video rendering |
| ElevenLabs API | `.env` file (ELEVENLABS_API_KEY) | Brian's voice clone |
| Galaxy AI | Samsung device or Galaxy app | AI video clip generation |
| HeyGen | app.heygen.com | Brian talking head recordings |

---

## FILES

| File | What It Does |
|---|---|
| `lmt-video-overlay.py` | Workforce article videos + Shorts |
| `lmt-movie-studio.py` | Training lesson movies |
| `example-config.json` | Template config (copy for each new video) |
| `workforce-article-1-config.json` | Tested config for Article 1 |
| `workforce-short-1-config.json` | Tested config for Short 1 |
| `galaxy-prompts/GALAXY-PROMPTS-LESSON-1.md` | Galaxy AI scene prompts for Lesson 1 |

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
- All text: `#FFFFFF` white (ADA readable)
- Font size: `46pt` for content
- Title slide: `48pt`, `no_bullet: true`
- End card: last 30 seconds, `no_bullet: true`, contact info
- No percent symbol — spell out "percent"
- x: 80, y: 250 for landscape

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

## WORKFLOW 3: TRAINING LESSON MOVIE

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

All renders use Intel QSV GPU acceleration via FFmpeg.
Falls back to CPU (libx264) if QSV unavailable — 10-15x slower.

---

*LMTMovieStudio — Learn More Technologies*
*Build. Test. Commit.*
