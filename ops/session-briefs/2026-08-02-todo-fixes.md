# Session Brief — To Do / Fix Next
## Date: 2026-08-02

---

## DONE THIS SESSION

- [x] What If PSA rendered — WHAT-IF-PSA-FINAL.mp4 (92s, B-Roll first w/ captions)
- [x] Captions burned into B-Roll section (C:/Users/USER/captions.srt)
- [x] ElevenLabs voiceover finalized and merged into video
- [x] Research stats added to content/research-brief.md (ageism + AI displacement)
- [x] $3.9T article drafted → content/articles/3-9-trillion-by-2050.md
- [x] Metricool connected: Facebook ✅ Instagram ✅ YouTube ✅
- [x] PSA captions written for FB, IG, YouTube, LinkedIn → content/captions/what-if-psa-captions.md
- [x] PSA scheduled in Metricool: Tuesday Aug 5, 2026 10:00 AM (FB + IG + YouTube)
- [x] marketing/accounts.md updated: Instagram ✅ connected, LinkedIn ❌ requires paid plan

---

## TO DO NEXT SESSION

### 1. Fix WordPress REST API — BLOCKING
**Problem:** `wp-publish.py` returns 404 on `learnmoretechnologies.com/wp-json/`
**Fix:**
- Log in to WP Admin → Settings → Permalinks
- Switch from "Plain" to "Post name"
- Click Save Changes (flushes rewrite rules)
- Retry: `python tools/wp-publish.py publish "content/articles/3-9-trillion-by-2050.md"`

### 2. Publish $3.9T Article to WordPress
- File ready: `content/articles/3-9-trillion-by-2050.md`
- Command (after WP API fix): `python tools/wp-publish.py publish "content/articles/3-9-trillion-by-2050.md"`
- After publish: copy LinkedIn caption from clipboard, post natively on LinkedIn

### 3. Post PSA to LinkedIn Manually (Tuesday Aug 5)
- When Metricool posts to FB/IG/YT at 10 AM — also post LinkedIn natively the same morning
- Caption ready: `content/captions/what-if-psa-captions.md` → LinkedIn section
- Attach: `C:/Users/USER/Desktop/what-if-psa/WHAT-IF-PSA-FINAL.mp4`

### 4. Metricool — Reconnect LinkedIn (Optional / Paid)
- LinkedIn in Metricool requires $20/mo Starter plan
- Current decision: skip, post LinkedIn natively
- Revisit when posting volume hits 20+ pieces/month

### 5. Check Instagram Privacy Settings
- `marketing/accounts.md` shows Instagram privacy as TBD
- Log into IG app → Settings → Privacy → review discoverability + ad tracking

### 6. YouTube — PSA Upload Confirmation
- Metricool will push to YouTube Tuesday Aug 5 at 10 AM
- Verify it went live in YouTube Studio after it posts

### 7. $850B Article Series — Part 2+
- Part 1 shipped 2026-04-05
- 9 follow-up tasks logged in memory (project_850b_series_todo.md)
- $3.9T article is a strong Part 2 candidate — publish after WP API is fixed

---

## VIDEO FILES — WHERE THINGS ARE

| File | Path |
|------|------|
| Final PSA | C:/Users/USER/Desktop/what-if-psa/WHAT-IF-PSA-FINAL.mp4 |
| Version B (slides first) | C:/Users/USER/Desktop/what-if-psa/WHAT-IF-PSA-VERSION-B.mp4 |
| Captions SRT | C:/Users/USER/captions.srt |
| Voiceover | C:/Users/USER/Desktop/what-if-psa/voiceover/psa-final-voiceover.mp3.mp3 |
| ElevenLabs Script | C:/Users/USER/Desktop/what-if-psa/ELEVENLABS-SCRIPT-PSA-FINAL.txt |

---

## TOOLS STATUS

| Tool | Status |
|------|--------|
| wp-publish.py | Broken — WP REST API 404. Fix permalinks first. |
| Metricool | FB + IG + YT connected. PSA scheduled Aug 5. |
| LinkedIn | Native posting only. No Metricool on free plan. |
| ElevenLabs | Active. Voice ID: uAs0vN0GLLpz7FM7JVkz |
| ffmpeg | Active. Use filter_complex for multi-clip assembly. |
