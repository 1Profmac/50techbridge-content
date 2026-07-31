# AI Video Production — Tools FAQ
## Learn More Technologies | Master Reference
## Last Updated: 2026-07-29

---

## QUICK REFERENCE — FULL STACK
## Last Updated: 2026-07-31

| Step | Tool | Purpose | Cost |
|---|---|---|---|
| Script | Claude / ChatGPT | Write story, scenes, voiceover | Free–$20/mo |
| Voice | ElevenLabs | Narration + character voices | $5–$22/mo |
| **Images + Video** | **Google Vids — Veo 3.1** | **Text prompt → video clip directly. Replaces Nano Banana + Kling** | **$16.80/mo (AI Expanded Access — ACTIVE)** |
| **AI Avatar** | **Google Vids — AI Avatar** | **Write script → choose avatar → generate presenter video** | **Included in AI Expanded Access** |
| **Character Images** | **Google Vids — Nano Banana Pro** | **Character consistency across scenes** | **Included in AI Expanded Access** |
| Images (backup) | Leonardo AI | Scene generation + character consistency | $10–$24/mo |
| Animation (backup) | Kling v3 Pro | Image-to-video, up to 15 sec clips | $10–$35/mo |
| Video Alt | Runway Gen-4.5 | Cinematic image-to-video, camera control | $15–$35/mo |
| Editing | CapCut | Assemble, captions, music sync | Free |
| Music | Soundraw / Suno AI | Royalty-free background score | Free–$16/mo |
| Thumbnails | Canva | Cover art, title cards | Free–$13/mo |
| Avatar (backup) | HeyGen | AI presenter/talking head | $29–$89/mo |
| Render | lmt-video-overlay.py | LMT branded video assembly | Already built |

---

## SECTION 1 — SCRIPTING TOOLS

### Q: What tool do I use to write scripts?
**Claude (this tool)** for structured, brand-voice scripts aligned to LMT.
**ChatGPT** as a backup or for rapid variation generation.

### Q: What script structure works best for AI story videos?
5-part structure:
1. **Hook** (0–15 sec) — Bold statement or question
2. **Setup** (15–45 sec) — Who/what/why
3. **Body** (1–5 min) — 3 core scenes or points
4. **Payoff** (30 sec) — Emotional resolution
5. **CTA** (15 sec) — One clear ask

### Q: How long should scripts be per scene?
- 60-second PSA: 8–10 scenes, 5–8 seconds each
- 4:50 film: 14–15 scenes, 10–20 seconds each
- Rule: write 20% more than you need — edit down in post

---

## SECTION 2 — VOICE & AUDIO

### Q: What tool generates the voiceover?
**ElevenLabs** — already in LMT stack.
- Brian's Voice ID: `uAs0vN0GLLpz7FM7JVkz`
- Save all outputs to: `VIDEOS/[project]/voiceover/`

### Q: What are the ElevenLabs plan limits?
| Plan | Cost | Minutes/mo | Best For |
|---|---|---|---|
| Free | $0 | 10 min | Testing only |
| Starter | $5/mo | 30 min | Short PSAs |
| Creator | $22/mo | 100 min | Full series |

### Q: What tool creates background music?
- **Soundraw** ($16/mo) — best for cinematic/emotional scores
- **Suno AI** (free tier) — full songs, mood-based prompts
- **Mubert** (free tier) — adaptive ambient/background loops
- All are royalty-free and YouTube-safe

### Q: What music fits the What If PSA?
- Machine world (0:00–2:30): NO music — sound design only (low hum, data tones)
- The Turn (2:30): Silence — 2 full seconds
- Human world (2:33–end): Sparse piano → builds to piano + cello

---

## SECTION 3 — IMAGE GENERATION

### Q: What tool generates scene images?
**Leonardo AI** — primary tool for LMT video production.
- Handles character reference locking
- Supports LoRA training for series
- Has IP-Adapter for face consistency
- Cost: $10–$24/mo

**Midjourney** — higher aesthetic quality, less character control.
- Use `--cref [image URL]` for character reference
- Cost: $10–$30/mo

**Free alternative:** Microsoft Bing Image Creator (DALL-E powered, no cost)

### Q: What model should I use in Leonardo AI?
- **Flux Kontext** — best for character consistency 2026
- **Phoenix** — best for cinematic realism
- **Leonardo Diffusion XL** — good all-rounder

### Q: What image size/ratio for YouTube videos?
- **16:9, 1920x1080** (1080p) for all scene images
- Export at highest quality before animating

---

## SECTION 4 — CHARACTER CONSISTENCY

### Q: What is the easiest way to keep characters looking the same?
**Level 1 — Character Reference Sheet** (start here)
- Generate your character once: front, side, 3/4, face close-up
- Upload as reference image in every new scene prompt
- Set strength to 0.8–1.0
- Cost: free with Leonardo AI subscription

**Level 2 — Seed Locking**
- After generating base character, copy the Seed Number
- Paste seed into every new generation for that character
- Boosts consistency ~80% on its own

**Level 3 — IP-Adapter / Face Lock**
- Locks the face specifically across different poses
- Built into Leonardo AI and ComfyUI
- Best for main characters across 10+ scenes

**Level 4 — LoRA Training**
- Train a small model on 15–30 images of your character
- Bakes face, body, clothing permanently into the model
- ~$5–10 to train, free to use forever after
- Best for long series (Maid and Billionaire style)

**Level 5 — ComfyUI + PuLID + InstantID**
- Full professional control: face + pose + camera angle
- Steep learning curve, cinematic results
- For advanced production only

### Q: What negative prompts prevent character drift?
Always add:
```
deformed face, extra limbs, inconsistent features, different age,
different skin tone, blurry face, cartoon, anime, disfigured, bad anatomy
```

### Q: Where are the What If PSA character prompts?
`VIDEOS/what-if-psa/CHARACTER-REFERENCE-PROMPTS.md`
- Character 1: The Worker (Black man, 58)
- Character 2: The Pioneer (Black woman, 64)
- Character 3: The Authority (White man, early 30s)

---

## SECTION 5 — ANIMATION (IMAGE TO VIDEO)

### Q: What tool animates still images into video clips?
**Kling v3 Pro** — best for narrative consistency
- Up to 15 seconds per clip
- Strong character consistency across shots
- Voice ID ties character voice to face
- Cost: $10–$35/mo

**Runway Gen-4.5** — best for cinematic camera control
- Director Mode: set pan, tilt, zoom with precision
- Best for ads and polished deliverables
- Cost: $15–$35/mo

**Pika 2.5** — fastest render, best for short-form
- Pikaframes: define start and end frames
- 2–3x faster than Runway
- Cost: free tier available

### Q: What settings work best for the What If PSA clips?
- Duration: 8–15 seconds per clip
- Format: 16:9, 1080p
- Motion: subtle — slight push in, slow pan
- Machine world: slow motion, cold blue toning
- Human world: natural motion, warm toning

### Q: How long does rendering take?
- Kling: ~60–90 seconds per 10-second clip
- Runway: ~45–90 seconds per 5-second clip
- Pika: ~20–40 seconds per 3-second clip

---

## SECTION 6 — VIDEO EDITING

### Q: What tool assembles the final video?
**CapCut** (free) — fastest for AI video assembly
- Auto-captions built in
- Music sync tools
- Text overlays and transitions
- Best for: storytelling/social style videos

**DaVinci Resolve** (free) — professional grade
- Full color grading
- Advanced audio mixing
- Best for: cinematic productions like the 4:50 film

**lmt-video-overlay.py** — LMT branded assembly
- Use for all official LMT channel videos
- Requires JSON config file
- Applies navy overlay, logo, branded text
- Run from `video-builder/` directory

### Q: What editing order should I follow?
1. Lock voiceover first (drives all timing)
2. Cut B-Roll clips to voiceover rhythm
3. Add machine world: cold color grade, data text overlays
4. Add the turn: black frame, silence
5. Add human world: warm color grade, gold text
6. Add Brian on-camera segment
7. Add music bed
8. Add captions
9. Add final title card
10. Export at 1080p, H.264

---

## SECTION 7 — AI AVATAR / TALKING HEAD

### Q: What tool creates AI presenter videos?
**HeyGen** — primary LMT tool
- Can use Brian's cloned avatar
- Or use stock avatars (Shayla Hart Studios style)
- Cost: $29–$89/mo
- Brian's HeyGen layout: ORIGINAL (not Circle)

**D-ID** — simpler, faster, less quality
- Good for quick social clips
- Not recommended for main productions

**Synthesia** — corporate/polished
- 50,000+ companies use it
- Good for training/explainer style

### Q: When do I use HeyGen vs shooting Brian live?
| Situation | Use |
|---|---|
| Scripted, branded LMT video | HeyGen avatar OR live iPhone |
| Quick social proof clip | iPhone Shorts |
| Faceless storytelling video | Stock HeyGen avatar |
| Grant pitch / serious proposal | Live Brian on iPhone |

---

## SECTION 8 — THUMBNAIL & GRAPHICS

### Q: What tool builds thumbnails?
**Canva** — primary LMT tool
- Navy background base already in `layers/base/`
- Gold text: #C8942E
- LMT logo: already in assets

### Q: What makes a strong AI movie thumbnail?
- Dramatic face close-up (your main character)
- Bold contrast: dark background + bright face
- 1–3 words max in large text
- Emotion first: intrigue, tension, warmth
- DO NOT use: stock photo smiles, clutter, small text

---

## SECTION 9 — LMT PRODUCTION RULES

### Q: What is the mandatory render procedure?
1. `git diff` vs part1-config before any render
2. Confirm JSON config matches current project
3. Check all asset paths exist
4. Run `lmt-video-overlay.py` from `video-builder/` directory
5. Review output before uploading
6. Log to `DOWNLOADS-LOG.md`

### Q: Where do B-Roll clips get saved?
- All B-Roll: `Desktop/LMT/850-Billion-Series/B-Roll/` regardless of origin
- What If PSA B-Roll: `VIDEOS/what-if-psa/B-Roll/`
- Never save B-Roll to root LMT folder

### Q: What background does LMT always use?
**Navy overlay** on all branded videos. Never green screen.
Base file: `video-builder/layers/base/navy-1920x1080.png`

### Q: What is banned in LMT videos?
- Green screen / chromakey — NEVER
- Auto-crop landscape to vertical for Shorts — NEVER
- The stat "1,200 people trained" — NEVER (real number: 347+ Pioneers)
- B-Roll written as "Broll" — always "B-Roll"

---

## SECTION 10 — COSTS SUMMARY

### YOUR ACTIVE STACK (Current — As of 2026-07-31)
| Tool | What It Does | Cost |
|---|---|---|
| Claude API (CLI) | File building, research, scripts | ~$150/mo cap (set) |
| claude.ai Pro | Desktop app, strategy, drafts | $21.32/mo |
| **Google AI Expanded Access** | **Veo 3.1 + Nano Banana Pro + AI Avatar + Gemini** | **$16.80/mo (30% off x4 months)** |
| ElevenLabs | Brian voiceover clone | $5–$22/mo |
| CapCut | Video editing + captions | Free |
| Suno AI | Background music | Free |
| Canva | Thumbnails + title cards | Free |
| **TOTAL** | | **~$193–$210/mo** |

---

### WHAT GOOGLE AI EXPANDED ACCESS REPLACES
| Was Paying | Tool | Replaced By | Savings |
|---|---|---|---|
| $19.99/mo | Nano Banana Pro | Google Vids — Nano Banana Pro | $19.99 saved |
| $25.99/mo | Kling Pro | Google Vids — Veo 3.1 | $25.99 saved |
| $29–$89/mo | HeyGen (avatar) | Google Vids — AI Avatar | $29–$89 saved |
| **$74–$134/mo** | **3 separate tools** | **$16.80/mo Google plan** | **$57–$117 saved** |

---

### Starter Stack (Under $30/mo)
| Tool | Cost |
|---|---|
| Claude | Already have it |
| ElevenLabs Starter | $5/mo |
| Google AI Expanded Access | $16.80/mo |
| CapCut | $0 |
| Suno AI Free | $0 |
| Canva Free | $0 |
| **TOTAL** | **~$22/mo** |

### Full Production Stack (Before Google upgrade)
| Tool | Cost |
|---|---|
| Claude | Already have it |
| ElevenLabs Creator | $22/mo |
| Leonardo AI Standard | $24/mo |
| Kling Pro | $35/mo |
| Runway Gen-4.5 | $35/mo |
| Soundraw | $16/mo |
| HeyGen Creator | $29/mo |
| Canva Pro | $13/mo |
| **TOTAL** | **~$174/mo** |

---

## RELATED FILES

| File | Location |
|---|---|
| What If PSA README | `VIDEOS/what-if-psa/README.md` |
| Character Reference Prompts | `VIDEOS/what-if-psa/CHARACTER-REFERENCE-PROMPTS.md` |
| Galaxy B-Roll Prompts | `VIDEOS/what-if-psa/GALAXY-PROMPTS-WHAT-IF-PSA.md` |
| ElevenLabs Script (60s) | `VIDEOS/what-if-psa/ELEVENLABS-SCRIPT-60S-PSA.txt` |
| Video Config | `VIDEOS/what-if-psa/what-if-psa-60s-config.json` |
| Futuristic Treatment | `marketing/drafts/WHAT-IF-PSA-FUTURISTIC-TREATMENT.md` |
| Full Film Script (4:50) | `marketing/drafts/what-if-4min50sec-film.md` |

---

*AI Video Tools FAQ | Learn More Technologies*
*Built: 2026-07-29 | Update this file when new tools are added to the stack*
