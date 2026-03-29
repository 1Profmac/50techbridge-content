# Layers — Video Production Assets

Like Photoshop layers. Each folder = one layer. Swap files to change the look without re-coding anything.

---

## Folder Structure

```
layers/
├── base/                          LAYER 0 — Background
│   └── navy-1920x1080.png         ✅ DONE — solid navy #0E1C2F
│
├── chrome/                        LAYER 1 — Header + Footer
│   └── header-footer-1920x1080.png  ✅ DONE — transparent PNG, gold titles + subscribe bar
│
├── brian/                         LAYER 2 — Talking Head Video
│   └── lesson-1-brian-nobg.webm   ⬜ NEEDED — Brian from HeyGen, NO background
│   └── lesson-2-brian-nobg.webm   ⬜ NEEDED
│   └── lesson-3-brian-nobg.webm   ⬜ NEEDED
│
├── clips/                         LAYER 3+ — B-Roll Video Clips
│   ├── lesson-1/                  ⬜ NEEDED — 5-8 Galaxy clips, 8 sec each
│   │   ├── clip-01-senior-ai.mp4
│   │   ├── clip-02-smartwatch.mp4
│   │   ├── clip-03-mobile.mp4
│   │   └── ...
│   ├── lesson-2/
│   └── lesson-3/
```

---

## What Brian Needs to Provide

### 1. Brian Talking Head (NO background)
- Export from HeyGen with **transparent/green screen background**
- Format: `.webm` (supports transparency) or `.mov` (ProRes 4444)
- If only `.mp4` available: export with solid green screen, script will chromakey it out
- One file per lesson (matches the lesson audio/script)
- Drop into `layers/brian/`

### 2. Galaxy AI Clips (per lesson)
- Create in Samsung Galaxy AI Video Generator
- Settings: **8-10 seconds, landscape 16:9, 1080p**
- 5-8 clips per lesson showing real 50+ adults using technology
- Save as `.mp4`
- Drop into `layers/clips/lesson-1/`, `lesson-2/`, `lesson-3/`
- Name them in order: `clip-01-description.mp4`, `clip-02-description.mp4`, etc.

### Lesson 1 clip ideas (from script content):
1. Senior interacting with tablet/phone (welcome/intro moment)
2. Adult 50+ looking confident with technology (you are not behind)
3. Woman using smartwatch for health (AgeTech in action)
4. Man 50+ on mobile device (device comparison)
5. Couple video calling family (staying connected)
6. Person checking health app (independence)
7. Group learning together (347 Pioneers)
8. Person smiling with device (your experience is your advantage)

---

## How Rendering Works

The script stacks layers bottom to top:
1. `base/navy-1920x1080.png` — always visible, full screen
2. `clips/lesson-X/clip-XX.mp4` — full screen at timed moments
3. `brian/lesson-X-brian-nobg.webm` — lower right, always visible
4. `chrome/header-footer-1920x1080.png` — always on top
5. Text overlays from config.json — on top of everything

**To change anything, just swap the file. No code changes needed.**
