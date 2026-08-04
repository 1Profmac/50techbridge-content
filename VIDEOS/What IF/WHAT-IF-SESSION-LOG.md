# What If — Production Session Log
## Learn More Technologies | 50+TechBridge
## Session: 2026-08-04

---

## WHAT WAS DONE THIS SESSION

### 1. Project Map Built
- Created `BRAND-FILM-PROJECT-MAP.md` — full 10-stage production pipeline
- Maps PSA assets to brand film needs
- Identifies all file types in production order (.md → .txt → .png → .mp4 → .mp3 → .json → .srt)
- Gap analysis: what exists vs what still needs to be generated

### 2. PSA B-Roll Renamed and Matched to Script
All B-Roll clips in `Desktop/what-if-psa/PSA/B-Roll/` renamed from informal names to script clip names:

| Old Name | New Name | Script Clip |
|---|---|---|
| `Marcus walking sceen1.mp4` | `clip-01-the-march.mp4` | CLIP 01 |
| `carol jobInterview.mp4` | `clip-02-algorithm-interview-carol.mp4` | CLIP 02 |
| `ROSA bank sceen.mp4` | `clip-03-kiosk-fail.mp4` | CLIP 03 |
| `Tom Boardroom.mp4` | `clip-04-boardroom-screen.mp4` | CLIP 04 |
| `3 50+adults at desk.mp4` | `clip-06-three-workers.mp4` | CLIP 06 |
| `Black Lady.mp4` | `clip-08-real-smile.mp4` | CLIP 08 |
| `Blank Screen Transition.mp4` (from slides/) | `clip-07-the-break.mp4` | CLIP 07 |

- `clip-05-headcount-reduction.mp4` copied from LMT animated to PSA B-Roll
- `Carol Hands.mp4` → `carol-hands-closeup-EXTRA.mp4` (extra, not in 10-clip script)

### 3. LMT Animated Folder Cleaned
All raw OpenArt download files (unnamed UUID filenames) renamed:
- Identified 8 duplicate files — renamed with `DUPE-` prefix
- Identified 2 potentially wrong files — renamed with `FLAG-VERIFY-` prefix
- `dr-linda-chen-openart-01/02.mp4` flagged — same byte size as carol clip, may be wrong footage

### 4. Carol Interview Identified
- `carol jobInterview.mp4` is CLIP 02 (Algorithm Interview) with Carol as the character
- Script originally wrote CLIP 02 with a Black male character — production shifted to Carol Smith (54, white woman)
- VO line "judged by the color of your hair" lands harder with silver-haired Carol — age discrimination made literal
- Renamed accordingly across both folders

### 5. Redundant Folder Deleted
- `Desktop/LMT/VIDEOS/what-if-psa/` — all subfolders were empty, deleted cleanly
- Only `Desktop/LMT/VIDEOS/What IF/` remains as brand film folder

### 6. ElevenLabs Script — Episode 1 Written
- `ELEVENLABS-SCRIPT-EP1.txt` created
- Covers all Marcus voiceover lines for Ep1: "The Replacement"
- Includes pause/timing notations for natural ElevenLabs delivery
- Estimated runtime: 55–65 seconds
- Saved to: `Desktop/what-if-psa/Scripts/`

### 7. Character Dialogue Script Written
- `CHARACTER-DIALOGUE-SCRIPT.md` created — all 8 characters with spoken lines
- Covers: Marcus, Carol, Dorothy, James, Rosa, Tom, Linda Chen, HR System Voice, Brian
- Each line tagged: off-camera (no lip sync) vs on-camera (HeyGen required)
- ElevenLabs voice assignments documented per character

---

## PSA B-ROLL STATUS — END OF SESSION

| Clip | File | Status |
|---|---|---|
| 01 | `clip-01-the-march.mp4` | ✅ |
| 02 | `clip-02-algorithm-interview-carol.mp4` | ✅ Carol version |
| 03 | `clip-03-kiosk-fail.mp4` | ✅ |
| 04 | `clip-04-boardroom-screen.mp4` | ✅ |
| 05 | `clip-05-headcount-reduction.mp4` | ✅ |
| 06 | `clip-06-three-workers.mp4` | ✅ |
| 07 | `clip-07-the-break.mp4` | ✅ Black transition slate |
| 08 | `clip-08-real-smile.mp4` | ✅ |
| 09 | `clip-09-pioneer-presenting.mp4` | ❌ Generate — full film only |
| 10 | `clip-10-reversed-interview.mp4` | ❌ Generate — full film only |

---

## BRAND FILM — NEXT PRODUCTION STEPS

1. Paste `ELEVENLABS-SCRIPT-EP1.txt` into ElevenLabs → generate `brand-film-ep1-voiceover.mp3`
2. Generate 5 Veo scene clips for Episode 1 using prompts in `WHAT-IF-AI-STORY-FILM.md`
3. Generate character voice clips in ElevenLabs per `CHARACTER-DIALOGUE-SCRIPT.md`
4. Build Ep1 title card in Canva
5. Assemble in Canva video editor: clips + VO + Denis Pavlov piano track
6. Export → `Desktop/LMT/VIDEOS/What IF/exports/WHAT-IF-BRAND-FILM-EP1-FINAL.mp4`

---

## KEY DECISIONS MADE

- **Canva replaces CapCut** — already owned, same capability for this production
- **Denis Pavlov piano track** covers all 3 episodes — no Suno AI needed
- **Additional cost to complete brand film: $0** — all tools already paid for
- **Dialogue adds realism** — 7 characters with lines, 3 require HeyGen lip sync (Carol, Marcus Ep3, Linda Chen)
- **Clip 07 solved** — Blank Screen Transition from slides/ folder serves as the break/turn moment

---

*What If Brand Film Production Log*
*Learn More Technologies | 50+TechBridge*
*2026-08-04*
