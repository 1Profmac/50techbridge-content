# Yoast SEO Compliance — Skill Reference
## Run on EVERY new or updated page before publishing
## Tell Claude: "yoast check" for SEO metadata recommendations

---

## WHAT TO DO FOR EVERY PAGE

Before publishing or updating any page on learnmoretechnologies.com:

### 1. Focus Keyphrase
- Open the page in WordPress editor
- Click the **Yoast icon** (top right toolbar, Y symbol)
- Type a focus keyphrase in the **Focus keyphrase** field
- Should be 3-5 words describing what the page is about
- Include "50+" or "adults 50+" when relevant

### 2. SEO Title
- Click **Search appearance** (magnifying glass icon in Yoast panel)
- Delete the default tags (Title, Page, Separator, Site title)
- Write a custom title under 60 characters
- Include the focus keyphrase
- Format: `What It Is — Brand Name`

### 3. Slug
- Keep it short, lowercase, hyphens only
- No special characters, no `+`, no spaces
- Example: `workforce`, `join-now`, `train`, `speak`

### 4. Meta Description
- Write 120-155 characters describing the page
- Include the focus keyphrase naturally
- Include a call to action or proof point
- End with a period

### 5. Save + Request Indexing
- Click **Return to your page** → **Save**
- Go to Google Search Console → URL Inspection
- Paste the page URL → **Request Indexing**

---

## CURRENT PAGES — SEO STATUS

| Page | Slug | Keyphrase | SEO Title | Meta Desc | Indexed |
|---|---|---|---|---|---|
| Join Now | join-now | free digital skills training adults 50+ | Join 50+TechBridge Free — Digital Skills Training for Adults 50+ | Free digital skills training for adults 50+. 347 Pioneers. 3X completion rate. No credit card needed. Start your free lessons today. | Requested |
| Workforce | workforce | workforce digital skills training 50+ | Workforce Digital Skills Training for Adults 50+ \| 50+TechBridge | AI and digital skills training built for adults 50+. 3X industry completion rate. WIOA eligible. MBE certified. 23 organizations trust 50+TechBridge. Schedule a free consult. | Requested |
| Train | train | digital skills training adults 50+ | 50+TechBridge Training — Free Digital Skills Course for Adults 50+ | Free digital skills and AI training for adults 50+. Three modules. Hands-on learning. 347 Pioneers. 3X completion rate. No tech background needed. Start free today. | Requested |
| Speak | speak | keynote speaker ageism technology 50+ | Book Brian McKinney — Keynote Speaker on Ageism, AI & the $76T Opportunity | Brian McKinney delivers keynotes on ageism, AI, and the $76 trillion opportunity for adults 50+. Former AARP Insider. MBE Certified. Book a speaking engagement today. | Requested |
| Blog | blog | agetech blog digital skills adults 50+ | Blog — AgeTech, AI & Digital Skills for Adults 50+ \| Learn More Technologies | Articles on agetech, AI, digital skills, and workforce development for adults 50+. Tips, stories, and insights from Brian McKinney and the 50+TechBridge community. | Requested |
| Consult | consult | agetech workforce consulting adults 50+ | Schedule a Consult — 50+TechBridge Workforce & AgeTech Strategy | Book a free 20-minute consult with Brian McKinney. Workforce digital skills training, AgeTech strategy, and AI readiness for organizations serving adults 50+. MBE Certified. | Requested |
| Contact | contact-us | contact learn more technologies 50+techbridge | Contact Learn More Technologies — 50+TechBridge | Contact Brian McKinney and Learn More Technologies. Workforce training, speaking engagements, AgeTech consulting, and 50+TechBridge partnership inquiries. | Requested |

---

## YOAST COLOR GUIDE

| Color | Meaning | Action |
|---|---|---|
| Green | Good length/optimization | No changes needed |
| Orange | OK but could improve | Adjust if easy, not critical |
| Red | Too long or too short | Fix before publishing |
| Grey dot | No keyphrase set | Add a focus keyphrase |

---

## FOR NEW PAGES

When creating any new page, tell Claude:

**"yoast check for [page name] about [topic]"**

Claude will provide:
- Focus keyphrase
- SEO title
- Meta description
- Slug recommendation

Then paste them into Yoast and request indexing.

---

## WEEKLY MAINTENANCE (part of Founders Bridge)

Every Monday check:
- [ ] Any new pages created this week without Yoast?
- [ ] Any pages with grey dots (no keyphrase)?
- [ ] Any 404 errors in Search Console?
- [ ] All key pages still indexed?
