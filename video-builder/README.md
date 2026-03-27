# LMT Video Overlay Builder

Automated branded text overlays on HeyGen talking-head videos.
Produces finished YouTube/LinkedIn videos from a simple JSON config.
Renders in under 2 minutes using Intel QSV GPU acceleration.

## What It Does

Takes a clean HeyGen video of Brian talking (no text) and adds:
- Branded header (LEARN MORE TECHNOLOGIES / 50+TechBridge)
- Gold accent lines
- Timed bullet-point slides that appear and disappear
- Source references and badges
- Lower third bar (Subscribe | Like | Share)
- End card with contact info
- Fade in/out on all text

## Requirements

- Python 3.10+
- FFmpeg with Intel QSV support
- FFmpeg path: `C:/Users/Jordyn/Desktop/ffmpeg-8.1-essentials_build/bin/ffmpeg.exe`

## Quick Start — Your Next Video

```bash
# 1. Copy the example config
cp example-config.json my-new-video-config.json

# 2. Edit my-new-video-config.json:
#    - Set input_video to your clean HeyGen MP4
#    - Set output_video to your desired output path
#    - Edit the slides (text, timing)

# 3. Run
python lmt-video-overlay.py my-new-video-config.json

# 4. Done — finished video at your output path
```

## Config Format

```json
{
  "input_video": "path/to/clean-heygen.mp4",
  "output_video": "path/to/finished.mp4",
  "show_header": true,
  "show_lower_third": true,
  "slides": [
    {
      "start": 0,        // seconds — when this slide appears
      "end": 12,          // seconds — when it disappears
      "x": 80,            // pixels from left (keep at 80)
      "y": 250,           // pixels from top (keep at 250)
      "font_size": 46,    // point size (46 for content, 48 for titles)
      "color": "#FFFFFF",  // text color (always #FFFFFF for ADA)
      "no_bullet": false,  // true for title/end card, false for content
      "fade": 0.5,         // fade in/out duration in seconds
      "bullets": [
        "First bullet point",
        "Second bullet point",
        "Third bullet point"
      ],
      "source": "Source: AARP",  // optional — shows below bullets
      "badge": "MBE Certified"   // optional — green text below bullets
    }
  ]
}
```

## Slide Defaults (don't change unless needed)

| Setting | Value | Why |
|---|---|---|
| x | 80 | Left margin — keeps text off Brian on right |
| y | 250 | Below header area |
| font_size | 46 | ADA readable at 1080p for 50+ audience |
| color | #FFFFFF | High contrast white on dark blue — ADA compliant |
| no_bullet | false | Adds "- " prefix for readability |

## Special Slides

**Title slide** — first slide, `no_bullet: true`, `font_size: 48`
**Highlight slides** — key statements, `no_bullet: true`
**End card** — last 30 seconds, `no_bullet: true`, contact info with empty lines for spacing

## Important Notes

- Do NOT use the % symbol in bullet text — spell out "percent" instead (FFmpeg limitation)
- Do NOT use apostrophes — use plain text alternatives
- Colons are auto-escaped
- Empty strings in bullets ("") create blank line spacing (useful for end card)
- Input video MUST be a clean HeyGen export with NO baked-in text

## Brand Constants

| Element | Value |
|---|---|
| Header | LEARN MORE TECHNOLOGIES — Georgia Bold 64pt Gold #C8942E |
| Subheading | 50+TechBridge — Arial 36pt Orange #E8733A |
| Content | Arial 46pt White #FFFFFF |
| Source refs | Arial 28pt Muted #A8B8CC |
| Lower third | Arial 32pt Gold #C8942E on Navy Mid #162640 |
| Gold lines | 3px #C8942E at 80% width |

## Files

| File | What |
|---|---|
| `lmt-video-overlay.py` | The builder script |
| `example-config.json` | Template config — copy this for each new video |
| `workforce-article-1-config.json` | Working config for Article 1 (tested, verified) |
| `README.md` | This file |

## Workflow for 30 Videos in 30 Days

1. Write the article (SEO version in TRACK-1 or TRACK-2)
2. Record Brian in HeyGen reading the PLAINTEXT version — clean, no overlays
3. Export clean MP4
4. Copy `example-config.json` and edit the slides to match the article
5. Run `python lmt-video-overlay.py your-config.json`
6. Review the output video
7. Upload to YouTube
8. Move config to the article folder for the record

Each video takes: ~15 min HeyGen recording + ~10 min config writing + ~2 min render = under 30 minutes total.
