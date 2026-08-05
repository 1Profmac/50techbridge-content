# HeyGen Lip Sync Tutorial
## What If Brand Film | Learn More Technologies
## How to create a talking character from a photo + ElevenLabs audio
## Created: 2026-08-05

---

## What This Tutorial Covers

How to take a still character image and an ElevenLabs voice MP3 and turn them
into a realistic talking video using HeyGen Talking Photo.

Demonstrated with Marcus Johnson — applies identically to Carol Smith and Dr. Linda Chen.

---

## The Concept in One Sentence

HeyGen looks at your character's face, listens to your audio, and generates
a video where the mouth moves to match every word. You supply the face and the voice.
HeyGen supplies the movement.

---

## Which Characters Need This

| Character | Episodes | Audio File |
|---|---|---|
| Marcus Johnson | Ep1 Scene 6 + Ep3 Comeback | marcus-three-workers.mp3 / marcus-comeback-interview.mp3 |
| Carol Smith | Ep1 Algorithm Interview | carol-smith-interview.mp3 |
| Dr. Linda Chen | Ep3 Pioneer Presenting | dr-linda-chen-presenting.mp3 |

All other characters are off-camera — voice only, no HeyGen needed.

---

## Before You Open HeyGen

You need two files ready before starting.

### File 1 — The Character Face (PNG)

| Character | Image to Use | File Location |
|---|---|---|
| Marcus | `front Facing.png` | `Desktop/what-if-psa/characters/Marcus/` |
| Carol | `Carol professional white woman.png` | `Desktop/what-if-psa/characters/Carol/` |
| Dr. Linda Chen | `fullFront.png` | `Desktop/what-if-psa/characters/Dr-Linda-Chen/` |

**Requirements for the image:**
- Front-facing — looking directly at camera
- Mouth closed or slightly closed — not mid-speech, not smiling wide
- Clean background preferred — complex backgrounds can confuse HeyGen
- High resolution — use the PNG files from the characters folder, not screenshots

### File 2 — The Character Voice (MP3)

Generate in ElevenLabs first using the character's script file.
Save the MP3 before opening HeyGen.

| Character | Script File | Output MP3 |
|---|---|---|
| Marcus (Ep1) | ELEVENLABS-SCRIPT-MARCUS-HEYGEN.txt | marcus-three-workers.mp3 |
| Marcus (Ep3) | ELEVENLABS-SCRIPT-MARCUS-HEYGEN.txt | marcus-comeback-interview.mp3 |
| Carol | ELEVENLABS-SCRIPT-CAROL-HEYGEN.txt | carol-smith-interview.mp3 |
| Dr. Linda Chen | ELEVENLABS-SCRIPT-HEYGEN-CHARACTERS.txt | dr-linda-chen-presenting.mp3 |

Save all MP3s to: `Desktop/what-if-psa/PSA/voiceover/characters/`

---

## Step-by-Step: Marcus in HeyGen

### STEP 1 — Open HeyGen and Navigate to Talking Photo

1. Go to `heygen.com` → log in
2. Left sidebar → **Photo Avatar** or **Talking Photo**
3. If you can't find it: top navigation → **Create** → **Talking Photo**

> You are looking for the feature that takes a PHOTO (not a video) and makes it talk.
> Not HeyGen Avatars (that's for pre-built characters).
> Not HeyGen Studio (that's for full video production).
> Talking Photo only.

---

### STEP 2 — Upload Marcus's Face

1. Click **Upload Photo**
2. Navigate to: `Desktop/what-if-psa/characters/Marcus/`
3. Select: **front Facing.png**
4. Wait 10–30 seconds for HeyGen to process the face
5. Marcus's face will appear in the preview window

**If HeyGen rejects the image:**
HeyGen occasionally rejects AI-generated faces. Try these backups in order:
- `casual dress.png`
- `90 degree.png`
- `Gemini_Generated_Image_8piyt18piyt18piy.png`

---

### STEP 3 — Add the Audio

**Option A — Upload Your ElevenLabs MP3 (Use This First)**

1. Look for **Upload Audio** or **Add Audio** button in the interface
2. Navigate to: `Desktop/what-if-psa/PSA/voiceover/characters/`
3. Select: `marcus-comeback-interview.mp3`
4. HeyGen loads the file and displays the waveform
5. You can trim or adjust the start point if needed

**Option B — Type Text Directly in HeyGen (Backup Only)**

Use this only if Option A produces bad sync results.
1. Select a HeyGen voice that sounds close to Marcus
   (deep, measured, American male, 60s)
2. Paste the script text directly into the text box
3. HeyGen generates its own TTS and syncs it
4. Downside: voice will not match Marcus's ElevenLabs voice from other scenes

---

### STEP 4 — Configure Settings

Set these before generating:

| Setting | Value | Why |
|---|---|---|
| Aspect ratio | **16:9** | Matches your film format |
| Resolution | **1080p** | Required for Canva assembly |
| Background | **Keep original** | Preserves the character image background |
| Avatar motion | **Subtle** | Minimal head movement — realistic, not animated |

---

### STEP 5 — Preview (If Available)

Most HeyGen plans include a short preview before spending full credits.

1. Click **Preview** if the button is visible
2. Watch the first 3–5 seconds
3. Check sync quality on these specific words — hard consonants reveal bad sync fastest:

| Word | Sound to Check |
|---|---|
| "breaks" | B and K sounds |
| "twenty-eight" | T sounds |
| "anyway" | W and Y sounds |
| "department" | D and T sounds (Marcus Ep1) |

**Good sync:** Mouth opens and closes with each word. Consonants match.
**Bad sync:** Mouth moves too early or too late. Words feel disconnected from movement.

---

### STEP 6 — Generate

1. Click **Generate** or **Submit**
2. HeyGen queues the job
3. Estimated wait time: 2–5 minutes for a 10-second clip
4. You will receive a notification or the preview will update when complete

Do not close the browser tab while generating.

---

### STEP 7 — Review the Full Output

When generation completes:
1. Watch the entire clip from start to finish
2. Check sync throughout — not just the first few seconds
3. Check that Marcus's face looks natural and not distorted

**If sync is slightly off:** Regenerate once with the same settings.
Usually the second generation improves.

**If sync is still off after two attempts:**
Switch to Option B (type text directly). HeyGen's internal TTS syncs more reliably
than uploaded audio in some account configurations.

**If the face looks distorted or unnatural:**
The source PNG may have too much background complexity.
Try cropping the image in Canva to show only the face and shoulders,
save as a new PNG, then re-upload.

---

### STEP 8 — Download

1. Click **Download** on the completed clip
2. Select format: **MP4**
3. Select quality: **1080p**
4. Rename the file immediately on download:

| Session | Save As | Save To |
|---|---|---|
| Marcus Ep1 | `marcus-heygen-ep1-threeworkers.mp4` | `Desktop/what-if-psa/characters/Marcus/heygen-exports/` |
| Marcus Ep3 | `marcus-heygen-ep3-comeback.mp4` | `Desktop/what-if-psa/characters/Marcus/heygen-exports/` |
| Carol Ep1 | `carol-heygen-ep1-interview.mp4` | `Desktop/what-if-psa/characters/Carol/heygen-exports/` |
| Dr. Linda Chen Ep3 | `lindachen-heygen-ep3-presenting.mp4` | `Desktop/what-if-psa/characters/Dr-Linda-Chen/heygen-exports/` |

---

### STEP 9 — Repeat for Marcus Episode 1

Same exact process. Different audio file.

- Image: `front Facing.png` (same)
- Audio: `marcus-three-workers.mp3`
- Script: "That's our department." — 3 words, approximately 2 seconds
- Output: `marcus-heygen-ep1-threeworkers.mp4`
- Save to: `Desktop/what-if-psa/characters/Marcus/heygen-exports/`

Note: This is a very short clip — 2 seconds of speech.
HeyGen handles short clips the same way as longer ones.
Generate, review, download.

---

## What You Have When Finished

```
Desktop/what-if-psa/characters/
├── Marcus/heygen-exports/
│   ├── marcus-heygen-ep1-threeworkers.mp4    ← "That's our department." (2 sec)
│   └── marcus-heygen-ep3-comeback.mp4        ← Full comeback speech (11 sec)
├── Carol/heygen-exports/
│   └── carol-heygen-ep1-interview.mp4        ← Interview speech (10 sec)
└── Dr-Linda-Chen/heygen-exports/
    └── lindachen-heygen-ep3-presenting.mp4   ← Presenting analysis (12 sec)
```

These MP4 files drop directly into Canva on the timeline.
No further processing. No conversion. Drag and place.

---

## How These Clips Land in Canva

### Marcus — Episode 1 (Three Workers)

```
Timeline:
[0:00–0:02]  marcus-heygen-ep1-threeworkers.mp4     "That's our department."
[0:02–0:03]  [1 second silence]
[0:03–0:12]  james-okafor-threeroom.mp3 (audio)     "I know. I saw the numbers..."
             clip-06-three-workers.mp4 (video)       Camera on headcount screen
```

---

### Marcus — Episode 3 (Comeback Interview)

```
Timeline:
[0:00–0:11]  marcus-heygen-ep3-comeback.mp4          Marcus speaks — 11 seconds
[0:11–0:12]  [1 second silence]
[0:12–0:23]  interviewer-warm-ep3.mp3 (audio)        Interviewer responds — engaged
             [interviewer clip or static shot]
```

---

### Carol — Episode 1 (Algorithm Interview)

```
Timeline:
[0:00–0:10]  carol-heygen-ep1-interview.mp4          Carol speaks — composed
[0:10–0:11]  [1 second silence]
[0:11–0:21]  clip-02-algorithm-interview-carol.mp4   Camera pushes to FLAG screen
             interviewer-cold-ep1.mp3 (audio)         "We appreciate your interest..."
[0:21–0:24]  [Hold on Carol's face — she heard it]
```

---

## Quick Reference — HeyGen Settings Cheat Sheet

| Setting | Value |
|---|---|
| Feature | Talking Photo (not Studio, not Avatars) |
| Aspect ratio | 16:9 |
| Resolution | 1080p |
| Avatar motion | Subtle |
| Audio | Upload MP3 from ElevenLabs (Option A) |
| Background | Keep original |
| Download format | MP4, 1080p |

---

## Troubleshooting

| Problem | Fix |
|---|---|
| HeyGen rejects the PNG | Try a different PNG from the same character folder |
| Face looks distorted | Crop image to head and shoulders only, re-upload |
| Sync is off by more than 0.5 sec | Regenerate once, then try typing text directly |
| Clip generates but mouth barely moves | Avatar motion is too low — increase to Medium |
| Download button missing | Refresh the page — completed jobs stay in your history |

---

## After HeyGen — What's Left

Once all four HeyGen clips are exported and saved:

1. Open Canva video editor
2. Import all HeyGen MP4s into your project assets
3. Place each clip on the timeline at the correct scene position
4. Stack character voice MP3s (off-camera characters) on separate audio tracks
5. Adjust volumes: VO at 100%, music at 15%, character voices at 85%
6. Add transitions: cross-fade, 0.5 seconds between clips
7. Auto-caption → review → export

The film is built from these pieces. HeyGen gives you the talking faces.
Canva assembles them into the story.

---

*HeyGen Lip Sync Tutorial | What If Brand Film*
*Learn More Technologies | 50+TechBridge*
*Created: 2026-08-05*
