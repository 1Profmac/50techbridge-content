# WHAT IF — Brand Film Project Map
## Learn More Technologies | 50+TechBridge
## Maps PSA folder assets → Brand Film production pipeline
## Updated: 2026-08-04

---

## TWO PROJECTS, ONE UNIVERSE

| Project | Runtime | Status | Location |
|---|---|---|---|
| **What If PSA** | 60 seconds | COMPLETE (3 versions) | `Desktop/what-if-psa/FINISHED/` |
| **What If Brand Film** (AI Story) | 3-part series ~4 min each | IN PRODUCTION | `Desktop/LMT/VIDEOS/What IF/` |

The PSA is the trailer. The Brand Film is the movie.

---

## FILE TYPES — ORDERED BY PRODUCTION STAGE

Files are listed in the order you create/need them. Each stage depends on the one before it.

---

### STAGE 1 — STORY & SCRIPT
*Build before touching any tool*

| Order | File Type | Filename | Status |
|---|---|---|---|
| 1 | `.md` | `WHAT-IF-AI-STORY-FILM.md` — 3-episode structure + full scene breakdowns | ✅ EXISTS |
| 2 | `.md` | `what-if-4min50sec-film.md` — original brand film script (Brian VO) | ✅ EXISTS |
| 3 | `.xlsx` | `WHAT-IF-CHARACTER-BIBLE.xlsx` — all characters, ages, look, role | ✅ EXISTS |
| 4 | `.txt` | `ELEVENLABS-SCRIPT-PSA-FINAL.txt` — PSA voiceover (60s, done) | ✅ EXISTS (PSA) |
| 5 | `.txt` | `ELEVENLABS-SCRIPT-EP1.txt` — Episode 1 voiceover lines for ElevenLabs | ❌ NEEDED |
| 6 | `.txt` | `ELEVENLABS-SCRIPT-EP2.txt` — Episode 2 voiceover lines | ❌ NEEDED |
| 7 | `.txt` | `ELEVENLABS-SCRIPT-EP3.txt` — Episode 3 voiceover lines | ❌ NEEDED |

---

### STAGE 2 — CHARACTER REFERENCE IMAGES
*Lock each character's face before generating video*

| Order | File Type | Filename | Status |
|---|---|---|---|
| 8 | `.md` | `CHARACTER-REFERENCE-PROMPTS.md` — Midjourney/Gemini prompts per character | ✅ EXISTS |
| 9 | `.md` | `CHARACTER-GENERATION-LOG.md` — which tools, which versions, accepted images | ✅ EXISTS |
| 10 | `.png` | `marcus-reference-front.png` — approved face, front angle | ✅ EXISTS (`characters/Marcus/`) |
| 11 | `.png` | `marcus-reference-45deg.png` | ✅ EXISTS |
| 12 | `.png` | `marcus-reference-90deg.png` | ✅ EXISTS |
| 13 | `.png` | `carol-reference-front.png` | ✅ EXISTS (`characters/Carol/`) |
| 14 | `.png` | `dorothy-reference-front.png` | ⚠️ CHECK `characters/Dorthy/` |
| 15 | `.png` | `dr-linda-chen-reference-front.png` | ⚠️ CHECK `characters/Dr-Linda-Chen/` |
| 16 | `.png` | `james-reference-front.png` | ⚠️ CHECK `characters/James/` |
| 17 | `.png` | `rosa-reference-front.png` | ⚠️ CHECK `characters/Rosa/` |
| 18 | `.png` | `tom-briggs-reference-front.png` | ⚠️ CHECK `characters/Tom-Briggs/` |
| 19 | `.jpg` | Start-frame stills for each scene (Veo seeding) | ⚠️ PARTIAL — 4 of 5 scenes exist |

---

### STAGE 3 — AI VIDEO PROMPTS
*Written prompts that generate the clips*

| Order | File Type | Filename | Status |
|---|---|---|---|
| 20 | `.md` | `GALAXY-PROMPTS-WHAT-IF-PSA.md` — Samsung Galaxy prompts for PSA clips | ✅ EXISTS (PSA) |
| 21 | `.md` | `MARCUS-SCENE1-VEO-PROMPT.md` — Veo 3.1 prompt, Ep1 Scene 1 | ✅ EXISTS |
| 22 | `.md` | `SCENE-3-CAROL-KLING-PROMPT.md` — Carol scene prompt | ✅ EXISTS |
| 23 | `.md` | `SCENE-3-WHITE-WOMAN-50PLUS.md` — alternate character prompt | ✅ EXISTS |
| 24 | `.md` | `NANO-BANANA-PROMPTS.md` — character face-lock prompts (deprecated tool) | ✅ EXISTS |
| 25 | `.md` | `VEO-PROMPTS-EP1-ALL-SCENES.md` — all Ep1 prompts in one file | ❌ NEEDED |
| 26 | `.md` | `VEO-PROMPTS-EP2-ALL-SCENES.md` | ❌ NEEDED |
| 27 | `.md` | `VEO-PROMPTS-EP3-ALL-SCENES.md` | ❌ NEEDED |

---

### STAGE 4 — RAW VIDEO CLIPS (B-Roll & Scenes)
*Generated from AI tools — not yet edited*

| Order | File Type | Filename Pattern | Status |
|---|---|---|---|
| 28 | `.mp4` | `clip-01-the-march.mp4` | ✅ EXISTS (`B-Roll/animated/`) |
| 29 | `.mp4` | `clip-03-kiosk-fail.mp4` | ✅ EXISTS |
| 30 | `.mp4` | `clip-04-boardroom-screen.mp4` | ✅ EXISTS |
| 31 | `.mp4` | `clip-05-headcount-reduction.mp4` | ✅ EXISTS |
| 32 | `.mp4` | `clip-08-real-smile.mp4` | ✅ EXISTS |
| 33 | `.mp4` | `carol-openart-01.mp4` | ✅ EXISTS |
| 34 | `.mp4` | `dr-linda-chen-openart-01.mp4` | ✅ EXISTS |
| 35 | `.mp4` | `dr-linda-chen-openart-02.mp4` | ✅ EXISTS |
| 36 | `.mp4` | `clip-02-algorithm-interview.mp4` | ❌ NEEDED (in PSA script, not generated) |
| 37 | `.mp4` | `clip-06-[scene].mp4` | ❌ NEEDED |
| 38 | `.mp4` | `clip-07-[scene].mp4` | ❌ NEEDED |
| 39 | `.mp4` | `ep1-scene-01.mp4` through `ep1-scene-[N].mp4` | ❌ NEEDED (Ep1 full set) |
| 40 | `.mp4` | `ep2-scene-01.mp4` through `ep2-scene-[N].mp4` | ❌ NEEDED |
| 41 | `.mp4` | `ep3-scene-01.mp4` through `ep3-scene-[N].mp4` | ❌ NEEDED |
| — | `.mp4` | PSA scenes (scene-1 through scene-5, with/without audio) | ✅ EXISTS (`what-if-psa/PSA/scenes/`) |

---

### STAGE 5 — VOICEOVER AUDIO
*ElevenLabs renders — one file per episode*

| Order | File Type | Filename | Status |
|---|---|---|---|
| 42 | `.mp3` | `psa-final-voiceover.mp3` — PSA voiceover (done) | ✅ EXISTS (`what-if-psa/PSA/voiceover/`) |
| 43 | `.mp3` | `brand-film-ep1-voiceover.mp3` — full Ep1 VO | ❌ NEEDED |
| 44 | `.mp3` | `brand-film-ep2-voiceover.mp3` | ❌ NEEDED |
| 45 | `.mp3` | `brand-film-ep3-voiceover.mp3` | ❌ NEEDED |

---

### STAGE 6 — MUSIC
*Background score — one track or segmented by act*

| Order | File Type | Filename | Status |
|---|---|---|---|
| 46 | `.mp3` | `denis-pavlov-music-piano-melancholic-beautiful-thoughtful-cinematic-music-215507.mp3` — licensed piano track | ✅ EXISTS (`what-if-psa/Music/`) |
| 47 | `.txt` | `Music for What if short.txt` — music notes/source | ✅ EXISTS |
| 48 | `.mp3` | `brand-film-ep1-music.mp3` — Suno AI score, Movement 1+2 | ❌ NEEDED |
| 49 | `.mp3` | `brand-film-ep2-music.mp3` — Movement 3 | ❌ NEEDED |
| 50 | `.mp3` | `brand-film-ep3-music.mp3` — Movement 4 | ❌ NEEDED |

---

### STAGE 7 — TITLE CARDS & SLIDES
*Canva exports + text overlays*

| Order | File Type | Filename | Status |
|---|---|---|---|
| 51 | `.mp4` | `opening-what-if-we.mp4` — PSA opening slide | ✅ EXISTS (`what-if-psa/PSA/slides/`) |
| 52 | `.md` | `WHAT-IF-SLIDE-SEQUENCE.md` — slide order + timing plan | ✅ EXISTS |
| 53 | `.mp4` | `ep1-title-card.mp4` — "Episode 1: The Replacement" | ❌ NEEDED |
| 54 | `.mp4` | `ep2-title-card.mp4` — "Episode 2: The Room" | ❌ NEEDED |
| 55 | `.mp4` | `ep3-title-card.mp4` — "Episode 3: Not Done Yet" | ❌ NEEDED |
| 56 | `.mp4` | `end-card-lmt.mp4` — LMT CTA / learn more | ❌ NEEDED |

---

### STAGE 8 — RENDER CONFIG
*lmt-video-overlay.py JSON config per episode*

| Order | File Type | Filename | Status |
|---|---|---|---|
| 57 | `.json` | `what-if-psa-60s-config.json` — PSA render config (reference) | ✅ EXISTS |
| 58 | `.json` | `brand-film-ep1-config.json` — Episode 1 render config | ❌ NEEDED |
| 59 | `.json` | `brand-film-ep2-config.json` | ❌ NEEDED |
| 60 | `.json` | `brand-film-ep3-config.json` | ❌ NEEDED |

---

### STAGE 9 — CAPTIONS
*Auto-generated then corrected*

| Order | File Type | Filename | Status |
|---|---|---|---|
| 61 | `.md` | `what-if-psa-captions.md` — PSA caption file | ✅ EXISTS (`LMT/content/captions/`) |
| 62 | `.srt` | `brand-film-ep1-captions.srt` — Episode 1 caption file | ❌ NEEDED |
| 63 | `.srt` | `brand-film-ep2-captions.srt` | ❌ NEEDED |
| 64 | `.srt` | `brand-film-ep3-captions.srt` | ❌ NEEDED |

---

### STAGE 10 — FINISHED EXPORTS
*Final renders ready to publish*

| Order | File Type | Filename | Status |
|---|---|---|---|
| 65 | `.mp4` | `WHAT-IF-PSA-FINAL.mp4` — PSA, no captions | ✅ EXISTS |
| 66 | `.mp4` | `WHAT-IF-PSA-FINAL-CAPTIONS.mp4` — PSA, captions burned in | ✅ EXISTS |
| 67 | `.mp4` | `WHAT-IF-PSA-VERSION-B.mp4` — PSA alternate cut | ✅ EXISTS |
| 68 | `.mp4` | `WHAT-IF-BRAND-FILM-EP1-FINAL.mp4` | ❌ NEEDED |
| 69 | `.mp4` | `WHAT-IF-BRAND-FILM-EP1-CAPTIONS.mp4` | ❌ NEEDED |
| 70 | `.mp4` | `WHAT-IF-BRAND-FILM-EP2-FINAL.mp4` | ❌ NEEDED |
| 71 | `.mp4` | `WHAT-IF-BRAND-FILM-EP2-CAPTIONS.mp4` | ❌ NEEDED |
| 72 | `.mp4` | `WHAT-IF-BRAND-FILM-EP3-FINAL.mp4` | ❌ NEEDED |
| 73 | `.mp4` | `WHAT-IF-BRAND-FILM-EP3-CAPTIONS.mp4` | ❌ NEEDED |

---

## GAP SUMMARY — WHAT'S MISSING

| File Type | Count Needed | Priority |
|---|---|---|
| `.txt` (ElevenLabs scripts) | 3 (one per episode) | HIGH — voiceover unlocks everything downstream |
| `.md` (Veo prompt sets) | 3 (one per episode) | HIGH — needed to generate video clips |
| `.mp4` (raw scene clips) | ~30–40 clips across 3 episodes | HIGH |
| `.mp3` (voiceover audio) | 3 episodes | HIGH |
| `.mp3` (music) | 3 episodes | MEDIUM — can temp with existing piano track |
| `.json` (render configs) | 3 episodes | MEDIUM — built at edit stage |
| `.mp4` (title cards) | 4 (3 episode titles + end card) | MEDIUM |
| `.srt` (caption files) | 3 episodes | LOW — last step before publish |
| `.mp4` (final exports) | 6 (final + captions × 3) | LOW — output, not input |

---

## TOOL STACK (Current as of 2026-08-04)

| File Type | Tool |
|---|---|
| `.txt` scripts | Claude CLI |
| `.md` prompts | Claude CLI |
| `.png` character images | Google Gemini / Midjourney |
| `.mp4` AI scenes | Google Vids — Veo 3.1 |
| `.mp4` avatar (Brian) | Google Vids AI Avatar |
| `.mp3` voiceover | ElevenLabs (Voice ID: `uAs0vN0GLLpz7FM7JVkz`) |
| `.mp3` music | Suno AI |
| `.mp4` title cards | Canva → export |
| `.json` render config | Claude CLI |
| `.srt` captions | CapCut auto-caption → export |
| `.mp4` final render | `lmt-video-overlay.py` |

---

## FOLDER STRUCTURE (Brand Film)

```
Desktop/LMT/VIDEOS/What IF/
├── scripts/                    ← Stage 1–3 (all .md, .txt, .xlsx, .json prompts)
├── characters/                 ← Stage 2 (.png reference images, one subfolder per character)
│   ├── Marcus/
│   ├── Carol/
│   ├── Dorthy/
│   ├── Dr-Linda-Chen/
│   ├── James/
│   ├── Rosa/
│   ├── Tom-Briggs/
│   └── stills/
├── B-Roll/
│   └── animated/               ← Stage 4 (raw .mp4 clips from Veo)
├── voiceover/                  ← Stage 5 (.mp3 per episode)
├── music/                      ← Stage 6 (.mp3 score tracks)
├── scenes/                     ← Stage 4 assembled scenes (pre-render)
├── storyboards/                ← Reference visuals
├── canva-assets/               ← Stage 7 (.mp4 title cards, .png overlays)
├── configs/                    ← Stage 8 (.json render configs)
├── captions/                   ← Stage 9 (.srt files)
├── exports/                    ← Stage 10 (FINAL .mp4 outputs)
└── resources/                  ← PDF guides (Veo, Midjourney, Kling, Minimax)

Desktop/what-if-psa/            ← PSA project (COMPLETE — reference only)
├── FINISHED/                   ← 3 final .mp4 versions
├── Scripts/                    ← PSA scripts + config
├── PSA/
│   ├── scenes/                 ← 5 PSA scenes (with audio)
│   ├── scenes-no-audio/        ← 5 PSA scenes (no audio, for VO overlay)
│   ├── voiceover/              ← psa-final-voiceover.mp3
│   ├── slides/                 ← opening title .mp4
│   ├── start-frames/           ← .jpg stills (used as Veo seed frames)
│   └── B-Roll/                 ← (empty — PSA used Veo directly)
├── characters/                 ← character .png images
├── Music/                      ← .mp3 + music notes
└── Resources/                  ← PDF guides (shared with brand film)
```

---

*Next step: write ELEVENLABS-SCRIPT-EP1.txt and VEO-PROMPTS-EP1-ALL-SCENES.md to unlock Episode 1 production.*
