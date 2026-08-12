# CHUNK 3 — Canva B-Roll Template Spec

**Goal:** Build ONE master template in Canva, then duplicate it 23 times and swap text/numbers per segment.

---

## Document setup
- **Type:** Custom size — **1920 × 1080 px** (16:9, matches Part 1)
- **Pages:** Start with 1 master, duplicate to 23
- **Background:** Solid fill `#0E1C2F` (LMT Navy)

---

## Master template layout (single 1920×1080 frame)

### 1. Background
- Full-bleed rectangle, color `#0E1C2F`
- Optional: subtle radial gradient overlay top-right at 8% opacity in `#C8942E` (matches hero gradient on web pages) — adds depth without distraction

### 2. Top-left brand lockup (anchor: top-left, 80px from edges)
- Text: `LEARN MORE TECHNOLOGIES`
- Font: **DM Sans Bold**, 18px, letter-spacing 0.15em, color `#C8942E`
- Underline rule: 1px, 80px wide, color `#C8942E`, 12px below text
- Sub-line under rule: `50+TECHBRIDGE`, DM Sans Regular, 12px, color `#A8B8CC`

### 3. Center stage — the BIG NUMBER (anchor: center, ~40% from top)
- Text: `[STAT]` (e.g., `19%`, `$850 BILLION`, `1 IN 5`)
- Font: **Playfair Display Bold Italic**, size **240–320px** (scale to fit width — long stats like "$28.2 TRILLION" go smaller)
- Color: `#C8942E`
- Letter-spacing: -0.02em
- Center-aligned

### 4. Subhead (anchor: directly below big number, 40px gap)
- Text: `[Supporting line]`
- Font: **DM Sans Medium**, 38px, line-height 1.35
- Color: `#FFFFFF`
- Center-aligned, max width 1400px (let it wrap on 2 lines if needed)

### 5. Optional side stat (anchor: top-right of center stage)
- Used only on segments with TWO data points (e.g., Segment 3, Segment 6)
- Background: `#162640` rounded rectangle, 12px radius, padding 24px
- Text inside: number in DM Sans Bold 56px gold, label below in DM Sans Regular 16px white

### 6. Footer tag (anchor: bottom-center, 100px from bottom)
- Text: `[FOOTER TAG]` (e.g., `SMART ORGS · ASSET CLASS THINKING`)
- Font: **DM Sans Bold**, 16px, letter-spacing 0.18em, ALL CAPS
- Color: `#A8B8CC`
- Above the text: 1px horizontal rule, 60px wide, centered, color `#C8942E`

### 7. Bottom-right page indicator (optional, anchor: bottom-right, 60px margins)
- Text: `03 / 04 · CHUNK 3` then below `SEGMENT [N] / 23`
- Font: DM Sans Regular, 12px, color `rgba(168,184,204,0.5)`

---

## Color palette (save as Brand Kit)
| Name | Hex | Use |
|---|---|---|
| Navy (primary bg) | `#0E1C2F` | Background |
| Navy Mid | `#162640` | Side stat cards, accent panels |
| Gold | `#C8942E` | Big numbers, brand mark, accent rules |
| Gold Light | `#E8B84B` | Hover states (not used in B-Roll) |
| White | `#FFFFFF` | Subheads, primary text |
| Text Muted | `#A8B8CC` | Footer tags, secondary labels |

## Fonts (load both into Canva once)
- **Playfair Display** (Bold Italic) — every big number
- **DM Sans** (Bold, Medium, Regular) — everything else

---

## Workflow (fastest path)
1. Build the master page with all 7 zones using placeholder text (`[BIG NUMBER]`, `[SUBHEAD]`, etc.)
2. Save as a Canva Template (My Templates)
3. Duplicate page 22 times → 23 total pages
4. Open `CHUNK-3-BROLL-SEGMENTS.md` side-by-side and paste each segment's headline / subhead / footer tag into the corresponding page
5. Adjust big-number font size only when text overflows (e.g., `$28.2 TRILLION` → drop to 200px)
6. Export: **MP4 video, 1080p, page duration 6 seconds each** → 23 pages × 6s = ~2:18 of B-Roll, matches narration pacing
7. Drop the exported MP4 into your video editor as the background layer; overlay Brian's HeyGen avatar on top (no chromakey, just position the navy-bg avatar in the bottom-right or as a small inset)

---

## Variants for special segments
- **Segment 11** (Section A closer "+12% productivity"): Add a thin gold border around the whole frame to signal section-end
- **Segment 12** (Section B opener): Add an eyebrow card ABOVE the big number → small gold pill `THE URGENCY IS NOT GOING AWAY` in DM Sans Bold 22px, gold bg `rgba(200,148,46,0.15)`, gold border, white text
- **Segment 23** (closing card "MEASURED IN TRILLIONS"): Big number drops to 180px so it fits, subhead "*Not thousands.*" uses Playfair Display Italic 64px in gold

---

## Time estimate
- Master template: 30 min
- Duplicate + populate 23 segments: 60–90 min
- Export + review: 15 min
- **Total: ~2 hours** to a finished B-Roll MP4
