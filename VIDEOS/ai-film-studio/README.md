# LMT AI Film Studio
## Learn More Technologies | 50+TechBridge
## Created: 2026-07-31

---

## PURPOSE

This folder is the production home for all LMT AI narrative films.
Visual storytelling used to promote LMT programs, the What If PSA,
"I'm Not Done Yet" campaign, and future AI story series.

Style reference: AI narrative storytelling (Maid & Billionaire method)
Brand reference: Apple "1984" (Ridley Scott) — same energy, LMT message

---

## FOLDER STRUCTURE

```
ai-film-studio/
│
├── README.md                        ← This file
├── AI-VIDEO-TOOLS-FAQ.md            ← Full tools reference (copy from VIDEOS/)
│
├── scripts/                         ← All story scripts and voiceover copy
│   ├── what-if-ep1-replacement.md
│   ├── what-if-ep2-the-room.md
│   └── what-if-ep3-not-done-yet.md
│
├── characters/                      ← Character reference sheets + prompts
│   ├── marcus-reference.png         ← BASE IMAGE — lock this first
│   ├── pioneer-woman-reference.png
│   └── CHARACTER-PROMPTS.md
│
├── storyboards/                     ← Scene-by-scene visual plans
│   └── what-if-storyboard.md
│
├── scenes/                          ← Generated scene images by episode
│   ├── ep1/                         ← Episode 1: The Replacement
│   ├── ep2/                         ← Episode 2: The Room
│   └── ep3/                         ← Episode 3: Not Done Yet
│
├── B-Roll/
│   ├── raw/                         ← Still images from Nano Banana / Leonardo
│   └── animated/                    ← Animated clips from Kling / Runway
│
├── voiceover/                       ← ElevenLabs MP3 files
│   ├── ep1-voiceover.mp3
│   ├── ep2-voiceover.mp3
│   └── ep3-voiceover.mp3
│
├── music/                           ← Background scores from Soundraw / Suno
│   ├── machine-world-hum.mp3        ← Cold, low, no music — sound design
│   ├── the-turn-silence.mp3         ← 2 seconds silence marker
│   └── human-world-piano.mp3        ← Sparse piano → full warmth
│
├── canva-assets/                    ← Title cards, data cards, end cards
│   ├── opening-data-card.mp4        ← PROCESSING... animation
│   ├── ep1-end-card.mp4
│   ├── ep2-end-card.mp4
│   ├── ep3-end-card.mp4
│   └── final-title-card.mp4
│
├── exports/                         ← Finished videos
│   ├── youtube/                     ← Full 1080p exports for YouTube
│   ├── social/                      ← Cut-down versions for LinkedIn/Shorts
│   └── archive/                     ← Raw renders, work in progress
│
├── resources/                       ← Learning materials + references
│   └── LEARNING-RESOURCES.md
│
└── configs/                         ← JSON configs for lmt-video-overlay.py
    ├── what-if-ep1-config.json
    ├── what-if-ep2-config.json
    └── what-if-ep3-config.json
```

---

## ACTIVE PROJECTS

| Project | Status | Episodes | Folder |
|---|---|---|---|
| What If — AI Story Film | IN PRODUCTION | 3 | `scenes/ep1-3/` |
| I'm Not Done Yet | PLANNED | TBD | TBD |

---

## PRODUCTION PIPELINE (Every Film)

### Step 1 — Script
- Write scene-by-scene story in `scripts/`
- Include voiceover copy per scene
- Tool: Claude CLI

### Step 2 — Characters
- Generate base character sheet in Nano Banana
- Save reference image to `characters/`
- Lock seed / reference before any scene generation

### Step 3 — Storyboard
- Map every scene visually in `storyboards/`
- Include: shot type, mood, color tone, duration

### Step 4 — Scene Images
- Generate each scene in Nano Banana using character reference
- Save raw images to `B-Roll/raw/`
- Name format: `ep[#]-scene[#]-[description].png`

### Step 5 — Animation
- Upload each image to Kling
- Settings: 10–16 seconds, subtle motion, 1080p 16:9
- Save clips to `B-Roll/animated/`
- Name format: `ep[#]-scene[#]-animated.mp4`

### Step 6 — Voiceover
- Record narration in ElevenLabs
- Voice ID: `uAs0vN0GLLpz7FM7JVkz` (Brian)
- Save to `voiceover/`

### Step 7 — Canva Assets
- Build title cards, data cards, end cards
- Export as MP4
- Save to `canva-assets/`

### Step 8 — Music
- Generate score in Soundraw or Suno AI
- Machine world: no music, low hum only
- Human world: sparse piano → warm swell
- Save to `music/`

### Step 9 — Assembly in CapCut
1. Import all animated clips
2. Sync to voiceover
3. Add Canva cards
4. Add music bed
5. Add captions
6. Color grade: cold blue (ep1) → warm gold (ep3)
7. Export 1080p H.264

### Step 10 — Export + Publish
- Save to `exports/youtube/`
- Upload as playlist: "What If — The Story"
- Title format: `"WHAT IF" | Ep [#]: [Title] #aimovies #50plus`

---

## BRAND RULES (Non-Negotiable)

- NEVER use green screen / chromakey
- NEVER auto-crop landscape to vertical for Shorts
- NEVER use stat "1,200 people trained" — always "347+ Pioneers"
- NEVER say "seniors" "elderly" "students" — always "adults 50+" or "Pioneers"
- Navy background: `#1B2A4A`
- Gold accent: `#C8942E`
- Always "B-Roll" — never "Broll"

---

## TOOL STACK

| Step | Tool | Cost |
|---|---|---|
| Script | Claude CLI | Already paid |
| Characters | Nano Banana | Free–low cost |
| Scene images | Nano Banana / Leonardo AI | $0–$24/mo |
| Animation | Kling v3 Pro | $10–$35/mo |
| Voiceover | ElevenLabs | $5–$22/mo |
| Music | Soundraw / Suno AI | Free–$16/mo |
| Editing | CapCut | Free |
| Title cards | Canva | Free–$13/mo |
| Avatar | HeyGen (Brian) | $29–$89/mo |

Full reference: `../AI-VIDEO-TOOLS-FAQ.md`

---

## LEARNING RESOURCES

| Resource | Link | Type |
|---|---|---|
| Curious Refuge Free Intro | curiousrefuge.com/start-here | Free course |
| Curious Refuge AI Filmmaking | curiousrefuge.com/ai-filmmaking | $749 or membership |
| Curious Refuge Membership | curiousrefuge.com/curious-refuge-membership | $149/mo |
| InVideo AI Filmmaking Guide | invideo.io/blog/ai-filmmaking | Free guide |
| AI Visual Stories Guide | smartaiedits.com/guides | Free guide |

Full reference: `resources/LEARNING-RESOURCES.md`

---

## KEY FILES (Cross-Reference)

| File | Location |
|---|---|
| What If AI Story Film plan | `../what-if-psa/WHAT-IF-AI-STORY-FILM.md` |
| Nano Banana prompts | `../what-if-psa/NANO-BANANA-PROMPTS.md` |
| Character reference prompts | `../what-if-psa/CHARACTER-REFERENCE-PROMPTS.md` |
| ElevenLabs script (60s) | `../what-if-psa/ELEVENLABS-SCRIPT-60S-PSA.txt` |
| Futuristic treatment | `../../marketing/drafts/WHAT-IF-PSA-FUTURISTIC-TREATMENT.md` |
| Full 4:50 film script | `../../marketing/drafts/what-if-4min50sec-film.md` |
| AI Video Tools FAQ | `../AI-VIDEO-TOOLS-FAQ.md` |

---

*LMT AI Film Studio | Learn More Technologies*
*First film: "What If" — 3-Episode AI Story Series*
*Created: 2026-07-31*
