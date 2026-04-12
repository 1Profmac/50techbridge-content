---
name: RepurposeContent
description: >
  Automatically repurpose any LMT video/script into all platform formats.
  When a YouTube video is produced, this skill generates: podcast episode,
  LinkedIn post, YouTube Short script, email newsletter, and social clips.
  Trigger after ANY video production or script completion.
---

# RepurposeContent — Multi-Platform Content Skill
## Learn More Technologies | 50+TechBridge | #AGENTIC50
### One piece of content. Seven platforms. Every time.

---

## TRIGGER PHRASES

- "Repurpose this video for all platforms"
- "Make a podcast episode from this video"
- "Cross-post this to all channels"
- "Full repurpose package for [video/script name]"
- After any LMTMovieStudio render completes, ask: "Want me to repurpose this?"

---

## WHAT THIS SKILL PRODUCES

From ONE video or script, generate ALL of these:

| # | Output | Platform | Format | Auto-generate? |
|---|--------|----------|--------|---------------|
| 1 | **Podcast episode audio** | Spotify, Apple, Amazon | MP3 via ElevenLabs | Yes |
| 2 | **Podcast episode description** | Spotify, Apple, Amazon | Text (title + description + show notes) | Yes |
| 3 | **LinkedIn post** | LinkedIn | 1300 chars max, hook + insight + CTA | Yes |
| 4 | **YouTube Short script** | YouTube Shorts, IG Reels, TikTok | 60-sec vertical, strongest data point | Yes |
| 5 | **Email newsletter** | Mailchimp | Subject + preview + body + CTA | Yes |
| 6 | **Facebook/Instagram post** | FB page, IG | Shorter version of LinkedIn post | Yes |
| 7 | **Twitter/X thread** | X (when active) | 5-tweet thread, data-first | Yes |

---

## INPUT — What You Give This Skill

Provide ONE of these:
- A finished video file path (MP4)
- A script file path (MD)
- A video-builder config JSON path
- A topic description ("the video about workforce training costs")

The skill will find the source content and generate everything.

---

## STEP-BY-STEP PROCESS

### Step 1: Identify Source Content
```
- Read the script/config to understand the content
- Extract: topic, key data points, quotes, CTA, target audience
- Identify the single strongest hook (for Short + social)
```

### Step 2: Generate Podcast Episode
```
Input:  Original script or video transcript
Output: podcast/episodes/EP[XX]-[slug].md

Process:
1. Rewrite the script for audio-only (remove visual references)
2. Add podcast intro: "Welcome to #AGENTIC50 — The Pioneers Podcast. 
   I'm Professor Brian McKinney..."
3. Add podcast close: "I'm Brian McKinney. This is #AGENTIC50 — 
   The Pioneers Podcast. You're not done yet."
4. Add CTAs: learnmoretechnologies.com/speak, /join-now
5. Strip to ElevenLabs-ready format (ELEVENLABS-RENDER-READY style):
   - No markdown formatting
   - No citations in brackets
   - Numbers spelled out or spoken naturally
   - [PAUSE] markers for natural cadence
6. Chunk for ElevenLabs character limit (~2500 chars per chunk)
7. Save chunks to: Desktop/LMT/Elevenlabs/[episode-name]/CHUNK-X-of-Y.txt
```

### Step 3: Generate Podcast Episode Description
```
Output: Same file as script, in frontmatter or footer

Include:
- Episode title
- Episode number
- One-paragraph description (under 500 chars for Spotify)
- Full show notes with timestamps
- Key data points mentioned
- Links: /speak, /join-now, YouTube link to video version
- Tags/keywords for search
```

### Step 4: Generate LinkedIn Post
```
Output: Desktop/LMT/04-ASSETS/content-drafts/text-drafts/[topic]-LINKEDIN-POST.txt

Format (1300 chars max):
- Line 1: Hook (question or shocking stat)
- Line 2-3: The insight (what most people get wrong)
- Line 4-6: The data (2-3 key stats)
- Line 7-8: The shift (what this means for the reader)
- Line 9: CTA (link to video/podcast/page)
- Line 10: Hashtags: #AGENTIC50 #50PlusTechBridge #WorkforceDevelopment #AITraining

Tone: Opportunity, not indictment. Data-first. FOMO, not guilt.
```

### Step 5: Generate YouTube Short Script
```
Output: youtube-shorts/scripts/[topic]-short.md

Format:
- 60 seconds max (150 words)
- Hook in first 3 seconds
- ONE data point (the strongest)
- ONE actionable takeaway
- End: "Follow for more. Link in bio."
- Include overlay text timing for video-builder config
```

### Step 6: Generate Email Newsletter
```
Output: Desktop/LMT/04-ASSETS/content-drafts/text-drafts/[topic]-EMAIL.txt

Format:
- Subject line (under 50 chars, curiosity-driven)
- Preview text (under 100 chars)
- Body: 200-300 words max
  - Open with the question or stat
  - Brief insight
  - Link to full video/podcast
  - CTA: "Hit reply and tell me..."
- Footer: standard LMT signature
```

### Step 7: Generate Social Posts (FB/IG/X)
```
Output: social/[topic]-social-posts.md

Facebook: 300 chars, conversational, link to video
Instagram: 200 chars + 10 hashtags, no link (use "link in bio")
X thread: 5 tweets, each under 280 chars, data-first, thread numbered
```

---

## ELEVENLABS VOICE SETTINGS (DO NOT CHANGE)

| Setting | Value |
|---------|-------|
| Voice | Brian McKinney (custom clone) |
| Voice ID | uAs0vN0GLLpz7FM7JVkz |
| Model | Eleven Multilingual v2 |
| Stability | 50% |
| Similarity | 75% |
| Style Exaggeration | 0 |
| Speaker Boost | ON |
| Output | MP3 192kbps+ |

---

## ELEVENLABS CHUNK RULES

- Max ~2500 characters per chunk
- Never split mid-sentence
- Never split mid-paragraph if possible
- Start each chunk with a natural breath point
- End each chunk at a paragraph break
- Name files: CHUNK-1-of-4.txt, CHUNK-2-of-4.txt, etc.
- First chunk includes the intro
- Last chunk includes the close + CTA

---

## FILE NAMING CONVENTION

All outputs follow this pattern:
```
[SERIES]-[TOPIC]-[PLATFORM].[ext]

Examples:
850-Billion-Part-1-LINKEDIN-POST.txt
850-Billion-Part-1-PODCAST-EP.md
850-Billion-Part-1-SHORT-SCRIPT.md
850-Billion-Part-1-EMAIL.txt
```

---

## BRAND RULES (from brand-constants.md)

- "Pioneers" not "students" or "users"
- "50+TechBridge" with plus sign, capital T, capital B
- "#AGENTIC50" — no space, all caps after hash
- Opportunity tone, not indictment
- Data does the arguing
- Always end with: "You're not done yet."
- CTAs: learnmoretechnologies.com/speak (booking) and /join-now (free course)

---

## EXAMPLE — Full Repurpose from $850 Billion Part 1

**Input:** `850-Billion-Series/Part-1/ALL-FORMATS/PART-1-FINISHED-LANDSCAPE-1920x1080.mp4`

**Outputs generated:**
1. `podcast/episodes/EP-850B-Part1-The-Number.md` — 20-min podcast script
2. `Elevenlabs/EP-850B-Part1/CHUNK-1-of-4.txt` through `CHUNK-4-of-4.txt`
3. `850-Billion-Series/Part-1/LINKEDIN/PART-1-LINKEDIN-POST.txt` (already exists — skip)
4. `youtube-shorts/scripts/850B-Part1-short.md`
5. `04-ASSETS/content-drafts/text-drafts/850B-Part1-EMAIL.txt`
6. `social/850B-Part1-social-posts.md`

---

## POST-GENERATION CHECKLIST

After generating all outputs:
- [ ] Podcast script reads naturally as audio (no visual references)
- [ ] ElevenLabs chunks are clean (no markdown, symbols spelled out)
- [ ] LinkedIn post is under 1300 chars
- [ ] Short script is under 60 seconds
- [ ] Email subject line is under 50 chars
- [ ] All CTAs point to correct URLs (/speak and /join-now)
- [ ] All files follow naming convention
- [ ] Git add + commit all new files

---

*Skill created: April 12, 2026*
*Works with: LMTMovieStudio, yt-short-opportunity*
