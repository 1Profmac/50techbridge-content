# Bridge Video — Canva Build Guide (Step-by-Step)

**Source script:** `bridge-video-canva-broll-script.md` (14 segments, ~90 seconds)
**Target style:** AARP "Attention Managers" news format — host on camera + text overlays + b-roll + clean graphics
**Tool:** Canva (free or Pro), no other software required
**Estimated build time:** 90 minutes start to finish
**Output:** MP4, 1920×1080, ready for LinkedIn / YouTube

---

## What you're building

A 14-page Canva video that, when exported, produces a 90-second "It's Not About the Data" bridge episode in the same news-style format as the AARP Carly Roszkowski video — but with the LMT brand and Brian as the host.

Each Canva page = one video segment. Canva auto-stitches the pages into video on export.

---

## Phase 1 — Prep (10 minutes, do this once)

### Step 1.1 — Open Canva
- Go to https://canva.com
- Sign in
- Top-right → **Create a design** → **Custom size** → **Width: 1920, Height: 1080, px** → **Create new design**

### Step 1.2 — Set up your Brand Kit (skip if already done)
- Left sidebar → **Brand** → **Brand Kit**
- **Brand colors** → add:
  - `#0E1C2F` (label: LMT Navy)
  - `#162640` (label: LMT Navy Mid)
  - `#C8942E` (label: LMT Gold)
  - `#FFFFFF` (label: White)
  - `#A8B8CC` (label: Muted)
  - `#3a4555` (label: Drained Gray — for the desaturate effect in Segment 2)
- **Brand fonts** → set:
  - Heading: **Playfair Display** Bold Italic
  - Subheading: **DM Sans** Bold
  - Body: **DM Sans** Regular

### Step 1.3 — Upload your assets
- Left sidebar → **Uploads** → **Upload files**
- Upload these 3 things:
  1. **Brian's HeyGen avatar render** (the navy-bg version with the lighter shirt) — save as `bridge-brian.mp4`
  2. **The $850B series end card** (reuse from Part 3 — find it in `Desktop\LMT\850-Billion-Series\YOUTUBE\PART-3\`)
  3. **Any soft outro music** (optional — Canva also has free music in the Audio tab)

### Step 1.4 — Set the background to navy
- Click anywhere on the blank page
- Right sidebar → **Background color** → pick **LMT Navy `#0E1C2F`**
- This will be your default for every page

### Step 1.5 — Save the file
- Top-left → rename the file to **"$850B Bridge Episode — Its Not About the Data"**
- Canva auto-saves from now on

---

## Phase 2 — Build the 14 pages (60 minutes)

> **Pro tip:** Build Page 6 first as your master template. It's the cleanest "card" layout. Once you have Page 6 looking right, **right-click → Duplicate page** five times to make Pages 7–11. Edit text only. Don't rebuild from scratch.

### Page 1 — Cold Open · 6 seconds

**What's on screen:** Brian's face, full-frame, no text.

**Steps:**
1. Add a new page (bottom-right → +)
2. Drag `bridge-brian.mp4` from Uploads onto the canvas
3. Resize to fill the entire 1920×1080 frame
4. **Trim:** click the video → top toolbar → **Trim** → set start to 0s, end to 6s
5. **Page duration:** bottom-right of page → click the clock icon → set to 6 seconds
6. No text, no graphics. Brian alone.

---

### Page 2 — Numbers Wash · 12 seconds

**What's on screen:** Brian inset bottom-right. Four lines of stats fading in over 12 seconds, then visually draining color at the end.

**Steps:**
1. New page
2. Background: navy `#0E1C2F`
3. Drag `bridge-brian.mp4` onto canvas → resize to **320×180 px**, position bottom-right with 60px margin
4. **Trim:** 6s to 18s of the source video
5. Add 4 text elements, stacked vertically, centered horizontally:
   - **Text 1:** `$850 BILLION` — DM Sans Bold, 56px, white
   - **Text 2:** `19% INNOVATION LIFT` — DM Sans Bold, 56px, white
   - **Text 3:** `60-YEAR-OLDS OUTPERFORMING 25-YEAR-OLDS` — DM Sans Bold, 48px, white
   - **Text 4:** `UNITED HEALTH · CISCO · BMW · CVS` — DM Sans Bold, 56px, white
6. **Animate each text** with staggered fades:
   - Click Text 1 → top toolbar → **Animate** → **Fade** → set to start at 0:00, duration 0.5s
   - Click Text 2 → Animate → Fade → start at 0:02
   - Click Text 3 → Animate → Fade → start at 0:05
   - Click Text 4 → Animate → Fade → start at 0:08
7. **The desaturate effect (Canva workaround):** Canva can't desaturate live, so use this trick:
   - At 0:10, copy all 4 text elements
   - Change the copies to color **`#3a4555`** (drained gray)
   - Animate them to fade IN at 0:10 while the white versions fade OUT at 0:10
   - The visual effect: the bright stats "drain" to muted gray
8. Page duration: 12 seconds

---

### Page 3 — The Pivot · 6 seconds

**What's on screen:** Brian full-frame. Behind/around him, the phrase "But the data was never the point." in italic gold.

**Steps:**
1. New page
2. Drag `bridge-brian.mp4` → fill frame → trim 18s–24s
3. Add text: **"But the data was never the point."**
   - Font: Playfair Display Italic
   - Size: 96px
   - Color: LMT Gold `#C8942E`
   - Position: center of canvas
   - **Opacity: 30%** (so Brian shows through)
4. Animate → **Pan** → slow drift left to right (subtle)
5. Page duration: 6 seconds

---

### Page 4 — Founder Line · 8 seconds

**What's on screen:** Brian full-frame. Bottom-third has the brand lockup.

**Steps:**
1. New page
2. Drag `bridge-brian.mp4` → fill frame → trim 24s–32s
3. **Lower-third bar:**
   - Add a rectangle at the bottom: 1920×120px, color navy mid `#162640`, 80% opacity
   - Inside the rectangle, add:
     - `LEARN MORE TECHNOLOGIES` — DM Sans Bold, 22px, gold
     - `Founded by Brian McKinney · Austin TX` — DM Sans Regular, 16px, white (below the gold line)
4. Animate the lower-third bar with **Slide up** entrance
5. Page duration: 8 seconds

---

### Page 5 — The Metaphor · 6 seconds

**What's on screen:** The most visually important card. "THE DATA IS THE DOOR." in white, then "It is not the room." in gold italic below.

**Steps:**
1. New page (no Brian video on this page)
2. Background: navy
3. Add text 1: **"THE DATA IS THE DOOR."**
   - DM Sans Bold, 84px, white
   - Letter-spacing: tracking +40
   - Position: center, slightly above middle
4. Add text 2: **"It is not the room."**
   - Playfair Display Italic, 96px, gold `#C8942E`
   - Position: center, slightly below text 1
5. Animate text 1: Fade In at 0:00
6. Animate text 2: Fade In at 0:01 (1 second delayed)
7. Add Brian's video as a small PIP bottom-right (320×180px), trimmed 32s–38s
8. Page duration: 6 seconds

---

### Page 6 — INTENTION · 6 seconds ⭐ MASTER TEMPLATE

> **Build this page perfectly. Then duplicate 5 times for pages 7–11.**

**What's on screen:** Pill label at top, large italic headline below, Brian PIP bottom-right.

**Steps:**
1. New page
2. **Pill label** (top center):
   - Add a rounded rectangle: 280×40px, navy mid `#162640` background, gold border 1px
   - Inside it, text: `01 · INTENTION` — DM Sans Bold, 18px, gold, letter-spacing tracking +60, centered
3. **Big headline:**
   - Add text: **"Stop apologizing for being experienced."**
   - Playfair Display Italic, 96px, white
   - Center horizontally, position below the pill with 60px gap
   - Max width: 1400px (wraps if needed)
4. **Brian PIP** bottom-right:
   - Drag `bridge-brian.mp4` → resize to 320×180px → position bottom-right
   - Trim: 38s–44s
5. Animate pill: Fade In at 0:00
6. Animate headline: Fade In at 0:00 (same time)
7. Page duration: 6 seconds

**Now: right-click this page → Duplicate page → repeat 5 times. You'll have Pages 7–11 ready to edit.**

---

### Page 7 — ACTION · 6 seconds

(Duplicated from Page 6, edit only:)
- Pill: `02 · ACTION`
- Headline: **"347 Pioneers. 3X completion rate."**
- Make `347` and `3X` gold `#C8942E` (highlight just those words and recolor)
- Brian PIP trim: 44s–50s

---

### Page 8 — INVITATION · 6 seconds

(Duplicated, edit only:)
- Pill: `03 · INVITATION`
- Headline: **"A safe place to learn — built for adults 50+."**
- Headline size: 84px (slightly smaller — longer text)
- Make `safe` and `50+` gold
- Brian PIP trim: 50s–56s

---

### Page 9 — COMMUNITY · 6 seconds

(Duplicated, edit only:)
- Pill: `04 · COMMUNITY`
- Headline: **"Bidirectional mentorship. Buddies. People."**
- Make `People.` gold AND slightly larger (100px)
- Brian PIP trim: 56s–62s

---

### Page 10 — INDEPENDENCE · 8 seconds

(Duplicated, edit only:)
- Pill: `05 · INDEPENDENCE`
- Headline: **"Devices that stop being ornaments and start being assistants."**
- Headline size: 76px
- Make `assistants` gold AND slightly larger (88px)
- Optional: make `ornaments` 30% opacity (it visually fades while `assistants` shines)
- Brian PIP trim: 62s–70s
- Page duration: **8 seconds** (longer than the others)

---

### Page 11 — SECURITY · 6 seconds

(Duplicated, edit only:)
- Pill: `06 · SECURITY`
- Headline: **"Dignity is the foundation, not the afterthought."**
- Make `foundation` gold
- Brian PIP trim: 70s–76s

---

### Page 12 — Challenge Line · 8 seconds

**What's on screen:** Brian full-frame. Two muted-gray lines fade in word by word.

**Steps:**
1. New page
2. Drag `bridge-brian.mp4` → fill frame → trim 76s–84s
3. Add text 1: **"Remember the numbers."** — DM Sans Bold, 56px, muted `#A8B8CC`, top-left at 80px from edges
4. Add text 2: **"Then remember the room."** — same style, below text 1
5. Animate text 1: Fade In at 0:01
6. Animate text 2: Fade In at 0:03
7. Page duration: 8 seconds

---

### Page 13 — Closing Card · 8 seconds

**What's on screen:** Brian fades out. Big closing typography on navy.

**Steps:**
1. New page (no Brian video)
2. Background: navy
3. Add text 1: **"THE DATA IS THE DOOR."**
   - DM Sans Bold, 64px, white
   - Letter-spacing tracking +60
   - Center horizontally, top of frame
4. Add text 2: **"The room is open."**
   - Playfair Display Italic, 140px, gold `#C8942E`
   - Center horizontally, below text 1
5. Animate text 1: Fade In at 0:00
6. Animate text 2: Fade In at 0:02
7. Page duration: 8 seconds

---

### Page 14 — End Card · 6 seconds

**What's on screen:** LMT brand lockup with CTA.

**Steps:**
1. New page
2. Background: navy
3. Add a thin horizontal rule at top center: 120×2px, gold
4. Add text 1: **"LEARN MORE TECHNOLOGIES"** — DM Sans Bold, 36px, gold, centered, letter-spacing +60
5. Add text 2: **"50+TechBridge"** — DM Sans Regular, 22px, white, centered, below text 1
6. Add text 3: **"learnmoretechnologies.com/join-now"** — DM Sans Bold, 22px, white, centered, in middle of frame
7. Add text 4: **"Watch the full $850 Billion Series →"** — DM Sans Regular, 16px, muted `#A8B8CC`, centered, below text 3
8. Page duration: 6 seconds

---

## Phase 3 — Audio (5 minutes)

### Step 3.1 — Add Brian's voice
- The HeyGen render of Brian already has his voice baked in
- The PIP video segments will play his voice automatically
- **Important:** Canva will play audio from ALL video elements on screen. If Brian appears as PIP across multiple pages, his voice will continue across the cuts naturally — but check the audio levels on each page

### Step 3.2 — Optional outro music
- Left sidebar → **Audio**
- Search "ambient" or "cinematic" — pick a soft track
- Drag onto the timeline at the bottom
- Trim to play only over Pages 13–14 (last 14 seconds)
- Set audio level to ~30% so it doesn't compete with Brian's voice

---

## Phase 4 — Export (5 minutes)

### Step 4.1 — Final review
- Click **Play** at the top to preview the full video
- Check:
  - Total runtime is ~90 seconds
  - Brian's voice is audible
  - Text fades match the narration beats
  - No empty gaps between pages

### Step 4.2 — Export
- Top-right → **Share** → **Download**
- File type: **MP4 Video**
- Quality: **1080p (Full HD)**
- Pages: **All pages**
- Click **Download**
- Canva will render and download the final MP4

### Step 4.3 — Save to LMT folder
- Move the downloaded MP4 to: `C:\Users\USER\Desktop\LMT\850-Billion-Series\BRIDGE\Bridge-Episode-CanvaExport.mp4`

---

## Phase 5 — Cross-platform variants (10 minutes)

In Canva:
1. **Square version (LinkedIn / Instagram feed):** File → Resize → 1080×1080 → Apply
2. **Vertical version (Reels / Shorts / TikTok):** File → Resize → 1080×1920 → Apply
3. Re-export each as MP4

---

## Why this works

- **Same exact visual structure as Carly Roszkowski's AARP video** — host on camera + b-roll-style text cards + clean graphics + 90-second cadence
- **Brand-locked** to LMT navy + gold
- **No external software needed** — 100% buildable in Canva
- **Output is professional** — looks like it came from a marketing team, not a solo founder
- **Repeatable template** — once you've built this once, you can make 4 more "bridge episodes" in 30 min each by duplicating the file and swapping text + Brian video

---

## What you DON'T need

- Final Cut Pro / Premiere Pro / DaVinci Resolve
- A motion graphics designer
- The Python renderer (`lmt-video-overlay.py`)
- The chromakey pipeline
- A video editor contractor
- Stock footage subscription

Just Canva + the HeyGen render of Brian + this guide.

---

## Build order checklist

- [ ] Phase 1 — Prep (10 min)
- [ ] Page 1 — Cold open (3 min)
- [ ] Page 2 — Numbers wash (8 min — most complex)
- [ ] Page 3 — The pivot (3 min)
- [ ] Page 4 — Founder line (4 min)
- [ ] Page 5 — Metaphor (4 min)
- [ ] Page 6 — INTENTION master template (8 min)
- [ ] Pages 7–11 — Duplicate + edit (4 min each = 20 min)
- [ ] Page 12 — Challenge line (4 min)
- [ ] Page 13 — Closing card (4 min)
- [ ] Page 14 — End card (3 min)
- [ ] Phase 3 — Audio (5 min)
- [ ] Phase 4 — Export (5 min)
- [ ] Phase 5 — Variants (10 min)

**Total: ~90 minutes**

---

## Troubleshooting

**Canva doesn't have Playfair Display Italic.**
Canva Pro has it. If you're on free, use **Cormorant Garamond Italic** or **DM Serif Display Italic** as a substitute — both are close enough.

**Brian's video has a weird crop.**
The HeyGen render is 1920×1080. When you scale it down to PIP size (320×180), make sure to **lock aspect ratio** (Canva does this by default if you drag from a corner).

**Text doesn't fit the headline area.**
Drop the font size by 10–15px. The headlines on Pages 6–11 use 96px as the default but should scale down for longer text (Page 8, Page 10).

**The desaturate effect on Page 2 looks weird.**
Skip it. Just have the white text fade out at 0:10. The "drain to gray" effect is an aesthetic bonus, not a requirement.

**Animations feel jittery.**
Canva animations are simple. Don't try to over-engineer. Stick to **Fade In / Fade Out / Pan**. Avoid Bounce, Tumble, or Block.
