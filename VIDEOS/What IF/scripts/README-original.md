# "What If" PSA — Production Folder
## Learn More Technologies | 50+TechBridge
## Visual Reference: Apple 1984 (Ridley Scott)
## Created: 2026-07-28

---

## STATUS: PRE-PRODUCTION — AWAITING B-ROLL + HEYGEN RECORDING

---

## FOLDER STRUCTURE

```
what-if-psa/
├── README.md                          ← This file
├── GALAXY-PROMPTS-WHAT-IF-PSA.md      ← 10 Galaxy AI prompts, ready to generate
├── ELEVENLABS-SCRIPT-60S-PSA.txt      ← Voiceover script for ElevenLabs
├── what-if-psa-60s-config.json        ← Video config — render when assets ready
│
├── B-Roll/                            ← DROP GALAXY CLIPS HERE
│   ├── clip-01-the-march.mp4          (generate first)
│   ├── clip-02-algorithm-interview.mp4
│   ├── clip-03-kiosk-fail.mp4
│   ├── clip-04-boardroom-screen.mp4
│   ├── clip-05-headcount-reduction.mp4
│   ├── clip-06-three-workers.mp4
│   ├── clip-07-the-break.mp4
│   └── clip-08-real-smile.mp4
│
├── voiceover/
│   └── psa-60s-voiceover.mp3          ← Generate from ElevenLabs script
│
├── canva-assets/                      ← Build these in Canva
│   ├── opening-data-card.mp4          (PROCESSING... animation)
│   └── final-title-card.mp4           (Navy/gold logo card)
│
└── FINISHED/
    └── YOUTUBE/
        └── WHAT-IF-PSA-60S-FINISHED.mp4
```

---

## STEP-BY-STEP PRODUCTION ORDER

### STEP 1 — Generate Galaxy B-Roll (do first, takes longest)
1. Open `GALAXY-PROMPTS-WHAT-IF-PSA.md`
2. Generate clips 01–08 in Galaxy AI
3. Settings: 8–12 seconds, 16:9 landscape, 1080p
4. Save each clip to `B-Roll/` with exact filename

### STEP 2 — Generate ElevenLabs Voiceover
1. Open `ELEVENLABS-SCRIPT-60S-PSA.txt`
2. Paste voiceover text into ElevenLabs
3. Voice ID: `uAs0vN0GLLpz7FM7JVkz` (Brian)
4. Save MP3 to `voiceover/psa-60s-voiceover.mp3`

### STEP 3 — Build Canva Assets
1. Opening data card: Black bg, white Eurostile/OCR-A font
   - "PROCESSING..." → pause → "WORKERS AGE 50+: FLAGGED FOR REVIEW"
   - Export as 3-second MP4
2. (Optional: final title card if not using text overlay)

### STEP 4 — Record Brian in HeyGen
- Duration: ~75 seconds (to cover the full PSA including end card section)
- Background: FULL GREEN SCREEN
- Brian appears on-camera only from 45s onward in final video
- Script: the full PSA voiceover text (lip sync to ElevenLabs if using that audio)
- HeyGen layout: ORIGINAL (not Circle)
- No baked-in text

### STEP 5 — Update Config + Render
1. Open `what-if-psa-60s-config.json`
2. Replace REPLACE fields:
   - `input_video`: path to HeyGen MP4
   - `audio_override`: path to ElevenLabs MP3 (if script supports it)
3. Run from `video-builder/` directory:
   ```
   python lmt-video-overlay.py C:/Users/USER/Desktop/LMT/VIDEOS/what-if-psa/what-if-psa-60s-config.json
   ```
4. Review output at `FINISHED/YOUTUBE/WHAT-IF-PSA-60S-FINISHED.mp4`

---

## VISUAL SYSTEM — TWO WORLDS

**Machine World (0:00–1:12):** Cold steel blue, harsh white, desaturated
- B-Roll clips 01–06 tell the story without words
- Text slides in white — simple, declarative
- Sound design: low hum, data processing tones (add in post)

**THE TURN (1:12–1:15):** Clip 07 — one warm amber light on black

**Human World (1:15–end):** Navy warming to gold
- B-Roll clip 08 — the real smile
- Text slides switch to gold (#C8942E)
- Brian appears on camera at 1:45
- Music enters here (commission or Artlist minimal piano)

---

## SOURCE DOCUMENTS

| Document | Location |
|----------|----------|
| Full treatment (futuristic) | `marketing/drafts/WHAT-IF-PSA-FUTURISTIC-TREATMENT.md` |
| PSA script (60s version) | `marketing/drafts/what-if-psa-and-commercial.md` |
| 4:50 brand film script | `marketing/drafts/what-if-4min50sec-film.md` |
| Tech stack skill | `video-builder/SKILL-lmt-movie-studio.md` |

---

*What If PSA Production Folder | Learn More Technologies*
*Build next: 4:50 full film config after 60s PSA is approved*
