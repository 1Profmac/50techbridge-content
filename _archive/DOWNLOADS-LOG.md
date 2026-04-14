# LMT Downloads Log

Chronological log of every file added to `Desktop/LMT/`. Newest at the bottom. Append-only.

| Date | File | Source | Destination | Why |
|---|---|---|---|---|
| 2026-04-08 07:54 | valuing-the-invaluable-2026-...pdf | AARP Public Policy Institute (manually downloaded) | `Research/AARP-Valuing-the-Invaluable-2026.pdf` | $1.01T family caregiving research — used for Carly Roszkowski + Jessica Lemann + Alan Weil outreach |
| 2026-04-08 10:05 | bridge-video-canva-broll-script.md | Created by Claude | `850-Billion-Article/Bridge-Episode/` | 14-segment b-roll spec for the bridge episode |
| 2026-04-08 10:05 | bridge-video-canva-broll-plaintext.txt | Created by Claude | `850-Billion-Article/Bridge-Episode/` | Plain-text version of the b-roll script |
| 2026-04-08 10:39 | bridge-video-canva-build-guide.md | Created by Claude | `850-Billion-Article/Bridge-Episode/` | Step-by-step Canva build walkthrough |
| 2026-04-08 10:42 | lmt-broll-production-recipe.md | Created by Claude | `850-Billion-Article/Bridge-Episode/` | REUSABLE production recipe for ALL future LMT videos |
| 2026-04-08 11:17 | bridge-video-motion-map.md | Created by Claude | `850-Billion-Article/Bridge-Episode/` | Pre-decided motion choices per segment |
| 2026-04-08 13:24 | It's not Just About the data_1080p.mp4 | HeyGen render (manual) | `850-Billion-Series/BRIDGE/NEEDS-RERENDER_*` | First HeyGen attempt at bridge — WRONG SCRIPT, needs re-render |
| 2026-04-08 14:33 | AARP-Valuing-the-Invaluable-2026.pdf (renamed copy) | Copy of Documents/ original | `Research/` | Same file as 07:54 — copied to LMT folder for project access |
| 2026-04-08 14:38 | LMT folder cleanup phase 1 | n/a | n/a | Created Bridge-Episode/, images/, BRIDGE/ subfolders. Moved 8 root files into proper homes. Wrote README.md and this DOWNLOADS-LOG.md. |
| 2026-04-08 14:45 | B-Roll consolidation phase 1 | n/a | `850-Billion-Series/B-Roll/` | Consolidated ALL B-Roll into one canonical home. Source-Clips/ for video files (16 mp4s + Part-3/ subfolder with 5 mp4s), Prompts-and-Scripts/ for .md/.pdf files (4 BROLL-PROMPTS + 3 from Elevenlabs + Manus-2026-04-06/ legacy folder). Source folders moved: 04-ASSETS/CHUNK1 broll-clips, 04-ASSETS/CHUNK2 broll-clips, 20260406Manus B-Roll, Elevenlabs (3 mis-filed scripts), 850-Billion-Series/YOUTUBE/PART-3 (5 segment files), 850-Billion-Series/B-Roll/Part2 Canva Chunks. |
| 2026-04-09 07:18 | LinkedIn cheat sheet | Created by Claude | `Canva-Cheat-Sheet.md` (root, marketing/, git) | Premiere -> Canva translation reference for Brian to use while building bridge video |
| 2026-04-09 07:30 | Project consolidation phase 2 | n/a | `850-Billion-Series/Part-1/` through `Part-4/` | Restructured all 4 parts into self-contained project folders. Each Part-X/ now contains its FINISHED.mp4 + LinkedIn post + YouTube metadata + thumbnail + ALL-FORMATS + B-Roll subfolder with the specific clips that part uses. Part 1 and Part 4 both have COPIES of the 5 clip-XX files (they share the same set). All 4 part configs in git updated (commits a737d97, fd52f82, 8e1ba0c). YOUTUBE/ folder now empty placeholders, can be deleted after verification. |
| 2026-04-09 07:42 | 4-subfolder master structure enforced | n/a | `Part-1/` through `Part-4/` | Per Brian's master format (Part-3 model): every Part-X folder now has EXACTLY 4 subfolders — ALL-FORMATS, B-Roll, LINKEDIN, Youtube — and ZERO loose files at the Part-X root. Moved finished videos + thumbnails into ALL-FORMATS, LinkedIn posts into LINKEDIN/, YouTube metadata into Youtube/, and Part 2's SHORTS folder into Youtube/Shorts/. |
| 2026-04-09 07:50 | All B-Roll co-located with parts | n/a | `Part-X/B-Roll/` | Per Brian's rule: 'all b-roll go into the b-roll folder for that part'. Moved each part's HeyGen fullGreen source render INTO its own Part-X/B-Roll/ folder (Part 1 Chap1 fullGreen, Part 2 CHUNK-2-of-4 + 2 SHORT variants, Part 3 CHUNK-3-of-4, Part 4 CHUNK-4-of-4). Updated all 4 part configs' input_video paths in git (commit e88bb4b). Each Part-X/B-Roll/ is now fully self-contained for re-rendering. Also preserved Part 1's alternate CHUNK-1 fullGreen as CHUNK-1-of-4-fullGreen-ALTERNATE.mp4. |
| 2026-04-09 07:55 | Final cleanup pass | n/a | n/a | Deleted YOUTUBE/ entirely (after moving Part 1's + Part 4's missing variants into their respective ALL-FORMATS folders). Deleted B-Roll/Source-Clips/ entirely (clips now live in Part-X/B-Roll/). Deleted bridge script duplicates from Source-Clips/Bridge-Episode/ (canonicals in 850-Billion-Article/Bridge-Episode/). Killed runaway ffmpeg PID 18812 + python PID 26644 that were writing a 4.5GB partial render to wrong location. Moved 3 review-and-decide files to _INBOX/: CHUNCK3-stray (75MB, typo'd), PART-2-SHORT-PARTIAL-RUNAWAY-RENDER-4.5GB.mp4 (killed render), temp-lesson-ref-orphan.json. |

---

## How to add new entries

Format: `| YYYY-MM-DD HH:MM | filename | source URL or "manual" | destination subfolder | one-line reason |`

Always append at the bottom. Never edit existing rows. If something gets moved later, add a new row noting the move.
