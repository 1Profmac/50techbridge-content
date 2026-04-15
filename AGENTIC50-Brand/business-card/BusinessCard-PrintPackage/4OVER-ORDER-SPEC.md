# 4over.com Order Specification — LMT Business Cards
## Learn More Technologies | Professor Brian McKinney
### Prepared: April 15, 2026

---

## ORDER DETAILS

| Spec | Value |
|------|-------|
| **Product** | Business Cards |
| **Stock** | 16pt C2S (Coated 2 Sides) |
| **Size** | 3.5" x 2" (standard US) |
| **Sides** | 2-sided (full color front + back) |
| **Lamination** | Soft Touch Matte — BOTH sides |
| **Spot UV** | YES — BOTH sides (mask files provided) |
| **Corners** | Rounded — 1/8" (3mm) radius, die-cut |
| **Bleed** | 0.125" on all sides |
| **Quantity** | 500 |
| **Proof** | YES — request digital press proof before full run |

---

## FILES PROVIDED

| File | Purpose | Dimensions |
|------|---------|-----------|
| `BusinessCard-FRONT-2100x1200.png` | Front artwork | 2100x1200px (3x scale, 300dpi at print) |
| `BusinessCard-BACK-2100x1200.png` | Back artwork | 2100x1200px (3x scale, 300dpi at print) |
| `SpotUV-MASK-FRONT.html` | Front spot UV mask (black = gloss) | Open in browser, screenshot at 2100x1200 |
| `SpotUV-MASK-BACK.html` | Back spot UV mask (black = gloss) | Open in browser, screenshot at 2100x1200 |
| `BusinessCard-SOURCE.html` | Editable HTML source (both sides) | Open in browser |
| `AGENTIC50-logo.svg` | Vector logo — scalable | SVG |
| `qr-code-speak.png` | QR code — links to learnmoretechnologies.com/speak | PNG |

**Note to prepress:** If you need the spot UV masks as PNGs instead of HTML, please render the HTML files in Chrome at 2100x1200 or contact us and we will provide PNGs.

---

## COLOR SPECIFICATIONS

| Element | Hex | CMYK Build (recommended) | Pantone |
|---------|-----|--------------------------|---------|
| Navy background | #0E1C2F | C:100 M:90 Y:40 K:60 | Pantone 296 C |
| Gold text/accents | #C8942E | C:15 M:40 Y:85 K:10 | Pantone 1245 C |
| White text | #FFFFFF | C:0 M:0 Y:0 K:0 | — |

**CRITICAL:** Navy must print rich and deep — not washed out gray. If your standard CMYK build looks thin, please add a bump plate or double-hit the black channel. Request a drawdown or press check if possible.

---

## SPOT UV INSTRUCTIONS

**What gets spot UV (glossy raised finish):**

### FRONT:
- Gold inset border (thin border around entire card)
- Entire #AGENTIC50 logo stamp (rings, microphone, text, diamonds, "50")
- Gold divider line between left and right panels
- "LEARNMORE TECHNOLOGIES" text
- Gold underline rule below brand name
- "CEO & FOUNDER" text

### FRONT — NO spot UV:
- Navy background
- "Professor Brian McKinney" (white text — matte only)
- "MBE Certified — Austin, Texas" (gray text — matte only)
- "ceo@learnmo.com | (512) 200-4241" (gray text — matte only)

### BACK:
- Gold inset border + corner accents
- Microphone illustration
- "learnmoretechnologies.com/speak" URL
- "50+techbridge.com" URL
- Gold rule separator
- Social platform names (LinkedIn, YouTube, Facebook, Instagram, Podcast)
- Social handles (/brianmckinneylmt, @LearnMoreTechnologies, etc.)
- QR code frame border
- "SCAN TO BOOK" label

### BACK — NO spot UV:
- Navy background
- "AI Training for the 50+ Workforce" (italic tagline — matte only)
- White rule separator
- QR code image itself (matte — UV on QR can cause scan issues)

---

## DESIGN REVIEW — REQUESTED CHANGES BEFORE PRINT

Please review the following concerns and advise:

### 1. FRONT — "LEARNMORE TECHNOLOGIES" may be too small
- Currently renders at ~16px in the HTML which translates to approximately 5-6pt at print size
- **Request:** Can you verify this text is legible at final print size? If not, recommend increasing to 8pt minimum or adjusting letter spacing for readability
- This is the company name — it must be clearly readable

### 2. FRONT — Contact info legibility
- "MBE Certified — Austin, Texas" is white at 50% opacity on navy
- "ceo@learnmo.com | (512) 200-4241" is white at 70% opacity on navy
- **Concern:** At print size these may be too faint to read, especially on matte stock which absorbs more light
- **Request:** Advise whether bumping opacity to 80-90% would improve legibility without losing the elegant understated look

### 3. BACK — Social handles are hard to read
- Platform names (LinkedIn, YouTube, etc.) are bold gold — these are fine
- Handles (/brianmckinneylmt, @LearnMoreTechnologies, etc.) are lighter gold at 75% opacity
- **Concern:** Gold-on-navy at 75% opacity will likely disappear at print size on matte stock
- **Request:** Should the handles be changed to WHITE instead of light gold? White on navy is higher contrast and ensures readability. The platform names can stay gold to maintain the brand color hierarchy:
  - **LinkedIn** (gold) /brianmckinneylmt (white)
  - **YouTube** (gold) @LearnMoreTechnologies (white)
  - etc.

### 4. BACK — "AI Training for the 50+ Workforce" tagline
- Currently white italic at 60% opacity
- **Concern:** May be invisible at print size on dark navy matte
- **Request:** Bump to 80% opacity or change to gold italic

### 5. GENERAL — Rounded corner alignment
- Both front and back have a gold inset border with rounded corners
- The die-cut rounded corners must align with the inset border radius
- **Request:** Verify the 1/8" die-cut radius matches the visual border radius so they read as concentric, not misaligned

### 6. QR CODE — Scan test
- QR code links to learnmoretechnologies.com/speak
- **Request:** Please verify the QR code scans correctly at print size before running

---

## SUMMARY OF RECOMMENDED CHANGES (for our own reference)

| Issue | Current | Recommended Change |
|-------|---------|-------------------|
| Front brand name size | ~5-6pt | Increase to 8pt minimum |
| Front contact info opacity | 50-70% white | Bump to 80-90% white |
| Back social handles | Gold at 75% opacity | Change to WHITE |
| Back tagline opacity | 60% white italic | Bump to 80% or change to gold |

**These changes should be made in `BusinessCard-SOURCE.html` and new PNGs re-exported before final print.**

---

## DELIVERY

| Field | Value |
|-------|-------|
| Ship to | Brian McKinney |
| Address | [FILL IN BEFORE ORDERING] |
| Shipping | Standard (or rush if needed for an event) |

---

*Package prepared April 15, 2026*
*Brand: LearnMore Technologies / #AGENTIC50 / 50+TechBridge*
