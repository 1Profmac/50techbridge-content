# 50+TechBridge YouTube Shorts — Content System

YouTube Short series fighting ageism in advertising for LearnMoreTechnologies / 50+TechBridge.

## Series

| Part | File | Theme | Status |
|---|---|---|---|
| 1 | `scripts/part-1-indictment.md` | 5% vs $76T | Ready |
| 2 | `scripts/part-2-the-decision.md` | They knew. They chose anyway. | Ready |
| 3 | `scripts/part-3-real-people.md` | Real people, real results | Ready |
| 4 | `scripts/part-4-solution.md` | What we built for you | Upcoming |
| 5 | `scripts/part-5-movement.md` | The movement | Upcoming |

## Assets

| File | Purpose |
|---|---|
| `ticker-bg.html` | News-ticker background (open in Chrome, record with OBS) |
| `animated-bg.html` | Animated scene-by-scene background |

## Production Workflow

```
1. Open ticker-bg.html in Chrome (1080x1920)
2. Record background with OBS or Windows Game Bar (Win+G)
3. Export HeyGen avatar — talking head, green screen, 1080p
4. In Canva (1080x1920):
   a. Layer recorded background
   b. Upload HeyGen MP4 → remove background → place lower third
   c. Add timed caption text overlays
   d. Export MP4 1080p
5. Upload to YouTube as Short
6. Post cross-platform per script file
```

## Reusable Skill

The `/yt-short` slash command is saved at:
`~/.claude/commands/yt-short.md`

Usage: `/yt-short [topic] [tone] [part-number]`

## Brand

- Primary: `#F0D060` / `#C8A028` (gold)
- Background: `#080F1F` (navy)
- Font: Montserrat Black
- CTA: learnmoretechnologies.com/join-now/
