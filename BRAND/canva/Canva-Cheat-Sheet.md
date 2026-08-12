# Canva Cheat Sheet for Premiere Pro Editors

**For:** Brian McKinney (Premiere Pro background, learning Canva)
**Print this. Tape it next to your monitor. Stop guessing.**

---

## 🧠 The mental model swap

| Premiere Pro | Canva |
|---|---|
| ONE timeline with multiple tracks | MULTIPLE PAGES played in sequence |
| Layers = stacked tracks (V1, V2, V3) | Layers = z-order on a single page |
| Cut between scenes = razor on timeline | Cut between scenes = a NEW PAGE |
| Lower-third on V2 over V1 b-roll | Lower-third = "Bring to Front" on the page |
| 2-min video = 1 long timeline | 2-min video = 14 short pages |

**The bottom of your Canva screen showing "elements" is NOT a Premiere timeline.** It shows what's on ONE page. To make a video, build many pages and Canva strings them together on export.

---

## ➕ How to ADD a layer (it's automatic)

Every element you put on the canvas IS a layer. No special button. Just add things:

| Want this | Click this |
|---|---|
| Text | Top toolbar → **T** (or press `T`) |
| Video clip | Left sidebar → **Uploads** → drag mp4 onto canvas |
| Shape (rectangle, pill) | Left sidebar → **Elements** → search "rectangle" |
| Image | Left sidebar → **Uploads** → drag png/jpg onto canvas |
| Solid color background | Right-click empty canvas → **Background color** |

---

## 🔃 How to MOVE a layer (change z-order)

### Method 1 — Right-click (easiest)
1. Click the element
2. Right-click → pick:
   - **Bring to Front** (top of stack)
   - **Send to Back** (bottom of stack)
   - **Bring Forward** (up one)
   - **Send Backward** (down one)

### Method 2 — Layers panel (Canva Pro)
- Bottom-right of screen: small **stacked rectangles icon**
- Click → layers panel opens
- Drag elements up/down to reorder
- Click an element name to select it

---

## 📄 How to ADD A PAGE

**Look at the bottom of the canvas.** Below your current page is a **+ Add page** button. Click it. New blank page appears.

**Pages play in sequence on export.** Page 1 → Page 2 → Page 3 → ... → Page 14 = your finished video.

Or use the killer shortcut: **`Ctrl+D`** (duplicates the current page so you can edit text-only and keep the layout).

---

## ⌨️ Keyboard shortcuts you'll actually use

| Shortcut | Action |
|---|---|
| `Ctrl+D` | **Duplicate page** ⭐ most useful |
| `Ctrl+]` | Bring forward one layer |
| `Ctrl+[` | Send backward one layer |
| `Ctrl+Shift+]` | Bring to front |
| `Ctrl+Shift+[` | Send to back |
| `Ctrl+G` / `Ctrl+Shift+G` | Group / Ungroup |
| `Ctrl+Z` / `Ctrl+Shift+Z` | Undo / Redo |
| `Space + drag` | Pan the canvas (like Premiere) |
| `Ctrl+scroll` | Zoom in/out |
| `T` | Add text |
| `R` | Add rectangle |
| `Ctrl+S` | Save (auto-saves anyway) |
| `Ctrl+Enter` | Play preview |
| `Ctrl+/` | Show all shortcuts |

---

## 🏗 The 6-layer architecture (every page)

Stack from BOTTOM to TOP:

```
┌──────────────────────────────────────────┐
│  6 ▲ Lower-third name bar                 │  (only on Brian-on-camera pages)
├──────────────────────────────────────────┤
│  5 ▲ Brand bug (LMT logo top-left)        │  (always visible)
├──────────────────────────────────────────┤
│  4 ▲ Text overlay (stat or quote)         │  (center)
├──────────────────────────────────────────┤
│  3 ▲ Brian PIP video (320×180)            │  (bottom-right)
├──────────────────────────────────────────┤
│  2 ▲ B-roll video (full frame, with Pan)  │
├──────────────────────────────────────────┤
│  1 ▼ Navy background #0E1C2F               │  (always at bottom)
└──────────────────────────────────────────┘
```

**Build order on each page:** navy bg → b-roll → Brian PIP → text → brand bug → lower-third.
**Then right-click → Send to Back / Bring to Front** to fix the z-order.

---

## 🎨 LMT brand colors (memorize)

| Use | Hex |
|---|---|
| Navy (primary bg) | `#0E1C2F` |
| Navy Mid | `#162640` |
| Gold (accent / big numbers) | `#C8942E` |
| Gold Light (hover) | `#E8B84B` |
| White (text) | `#FFFFFF` |
| Muted (secondary text) | `#A8B8CC` |
| Drained gray (Segment 02 desat) | `#3a4555` |

## 🔤 LMT brand fonts

| Use | Font |
|---|---|
| Big numbers / italic emphasis | **Playfair Display** Bold Italic |
| Headlines / pill labels / footers | **DM Sans** Bold |
| Body / muted text | **DM Sans** Regular |

---

## 🎬 The 6 motion techniques (use on every video)

| # | Name | How in Canva |
|---|---|---|
| **T1** | Slow Zoom (Ken Burns) | Click clip → **Animate → Pan** |
| **T2** | Slow Pan (LR/RL) | Make video larger than canvas, position focal point start/end across 2 pages |
| **T3** | Punch-In on stat | 2 pages: 100% → 110% with Dissolve transition + Bounce In on stat text |
| **T4** | Scene change cut | Page transition: Dissolve (default) / Hard Cut / Fade to Black / Slide |
| **T5** | L-Cut (audio leads) | Export Brian voice as separate MP3, drop on timeline, mute on-cam pages |
| **T6** | The Hold | Static page, no animation, 5+ seconds, ONE per video at the key moment |

---

## ⚠️ Top 10 Canva gotchas for Premiere editors

1. **There is no multi-track timeline.** Pages, not tracks.
2. **Each page has its own layer stack.** Don't try to put everything on Page 1.
3. **B-Roll under text** = right-click b-roll → Send to Back. NOT moving it on a "video track".
4. **"Page duration"** is set per page via the clock icon at bottom-right of each page.
5. **Audio across pages**: drag an MP3 onto Canva and it spans multiple pages by default (for L-cuts).
6. **Animations are per-element, not per-page** (use the Animate menu on each element).
7. **Page transitions are between pages** (click the gap between pages to set Dissolve / Slide / etc.).
8. **`Ctrl+D` duplicates a PAGE, not just an element** — different from Premiere's `Ctrl+D` razor.
9. **Resize a video by dragging a CORNER** (locks aspect ratio). Dragging an edge stretches it.
10. **Canva auto-saves.** Don't waste time hunting for a save button.

---

## 🚀 Building the bridge video — quickstart

1. **Open Canva** → Custom size 1920×1080
2. **Set background to navy `#0E1C2F`** (right-click canvas → Background color)
3. **Build Page 1** (Cold Open): drag Brian's HeyGen mp4 onto canvas → fill frame → 6 second duration. NO TEXT. NO B-ROLL. Just Brian.
4. **`Ctrl+D` → Page 2** (Numbers Wash): resize Brian to 320×180 PIP bottom-right, add 4 stat text lines staggered. 12 second duration.
5. Continue per `bridge-video-motion-map.md` for Pages 3–14.
6. **Each page is its own scene.** Don't try to layer all 14 segments on Page 1.

---

## 📂 Companion files (in `Desktop\LMT\` and `marketing\`)

- `bridge-video-script.md` — HeyGen narration
- `bridge-video-canva-broll-script.md` — 14-segment b-roll spec
- `bridge-video-canva-build-guide.md` — step-by-step Canva walkthrough
- `bridge-video-motion-map.md` — pre-decided motion choices per segment
- `lmt-broll-production-recipe.md` — REUSABLE recipe for ALL future LMT videos
- `Canva-Cheat-Sheet.md` ← THIS FILE

Open this cheat sheet on your second monitor while building. Stop guessing. Build the page, ship the video.
