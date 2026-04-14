# LearnMore Technologies — Mobile + CSS Fix List
## Generated 2026-04-12 · Updated 2026-04-13

---

## /speak Page — CSS Issues
- [ ] List item text (descriptions after bold topic names) too low contrast on navy background
- [ ] Theme overriding inline white color on `<li>` elements — needs `!important` or theme override
- [ ] Check same issue on /workforce page list items
- [ ] SEO block text colors need to survive theme CSS cascade

---

## /workforce + /speak — SEO / Indexing
- [ ] /workforce — indexed, SEO block added 2026-04-13, re-indexing requested
- [ ] /speak — NOT indexed (redirect issue), SEO block added 2026-04-13, re-indexing requested
- [ ] 318 pages not indexed site-wide — investigate in Google Search Console → Pages
- [ ] Check all key pages have Yoast focus keyphrase set
- [ ] Add images with alt text to /workforce and /speak (Yoast flagged)

---

## Business Card (LMT_BusinessCard_v3.html)
- [ ] Add responsive CSS for mobile preview (card scales down on phone screens)
- [ ] Test card HTML renders correctly on mobile browsers

---

## learnmoretechnologies.com (Homepage)

### Critical
- [ ] Fixed search width `25rem` overflows on phones under 400px
- [ ] Horizontal scroll slider (`scroll-snap-type: x mandatory`) causes unwanted horizontal scroll
- [ ] Negative margins on `.nfd-overlap-x` cause overflow on narrow screens
- [ ] Inline CSS is extremely verbose — impacts load time on mobile connections

### Font / Readability
- [ ] `.nfd-text-xs` at 0.75rem (12px) too small for mobile — bump to 14px minimum
- [ ] `.nfd-text-sm` at 0.875rem borderline — review for ADA compliance
- [ ] No mobile-specific font size overrides on many text elements

### Touch Targets
- [ ] Icon buttons at 28px do not meet 44-48px minimum recommendation
- [ ] Review all interactive elements for minimum 44px tap area

### Images
- [ ] No `srcset` or `<picture>` elements — add for responsive image loading
- [ ] Verify all images have `max-width: 100%` in every context

### Performance
- [ ] Simplify/defer heavy inline CSS on mobile
- [ ] Audit BuddyPress/WooCommerce component rendering on mobile

---

## learnmoretechnologies.com/speak (Speaker Page)

### Critical
- [ ] 100vw cover elements cause horizontal scrollbar — use `100%` or `calc(100vw - scrollbar)`
- [ ] Wave patterns with absolute positioning overflow on small screens (380px, 106px fixed values)
- [ ] Container max-width 1200px — verify tablet breakpoints (768px–1024px)

### Touch Targets
- [ ] Icon buttons lack 44px minimum touch target
- [ ] Link preview carousel angle buttons too small for touch
- [ ] Toolbar buttons need size audit

### Font / Readability
- [ ] Heading sizes jump dramatically with no intermediate breakpoints
- [ ] 0.75rem minimum in `clamp()` too small for mobile

### Images
- [ ] Profile card, group card, link preview images lack `srcset`/`sizes`
- [ ] Fixed image dimensions — switch to fluid sizing

### Layout
- [ ] `.nfd-absolute-header` not tested for mobile stacking
- [ ] 12-column grid (`.nfd-grid-cols-12`) may not reflow on mobile without explicit breakpoints
- [ ] Skeleton loaders for cards may disorient mobile users

### Navigation
- [ ] No clear mobile menu indicator visible
- [ ] Verify hamburger/mobile nav exists and works

---

## learnmoretechnologies.com/workforce (Workforce Page)

### Critical
- [ ] `width:3000px` element will cause massive horizontal scroll
- [ ] `width:25rem!important` on search component overflows small screens
- [ ] `.nfd-overlap-x-lg` uses `translateX(-150px)` with no mobile override
- [ ] 11/12 column grids don't reflow on mobile

### Touch Targets
- [ ] Button padding too minimal — verify 44-48px tap areas
- [ ] Icon buttons at 28px below minimum

### Font / Readability
- [ ] `--wndb--text--xs: 0.75rem` (12px) too small
- [ ] `calc()` font scaling with CSS variables — test actual rendered sizes on phones

### Images
- [ ] Some images missing explicit `max-width: 100%`
- [ ] Fixed aspect ratios need testing at 320px width

### Performance
- [ ] Multiple overlay effects (masks, gradients, perspective transforms) heavy on mobile GPU
- [ ] Simplify `.nfd-bg-effect-*` on mobile breakpoints

### Forms
- [ ] `min-height: 50px` on inputs — verify doesn't exceed viewport on small phones
- [ ] Modal elements may cause layout shifts

---

## Global Recommendations
1. Test all pages on actual devices: iPhone SE (375px), iPhone 14 (390px), Android small (360px)
2. Set minimum font size to 16px for ADA compliance across all pages
3. Ensure all touch targets are minimum 44px × 44px
4. Add `srcset` to all images for responsive loading
5. Remove or override all fixed pixel widths at mobile breakpoints
6. Audit and simplify CSS payload for mobile performance
7. Add proper mobile navigation (hamburger menu) if not present

---

*Fix priority: Critical items first, then touch targets, then fonts, then performance.*
