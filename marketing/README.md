# LMT Marketing Folder — Organized Index

**Last reorganized:** 2026-04-16 (Come Down From the Clouds session — two passes: marketing restructure + video consolidation)

**Video files relocated (2026-04-16):** Bridge video production scripts moved to `../850-Billion-Series/Bridge-Its-About-the-People/scripts/`. Reusable B-Roll production recipe moved to `../video-builder/lmt-broll-production-recipe.md`. Marketing folder no longer holds video assets.

**Canonical source repos (git):**
- `C:\Users\USER\Documents\lmt-claude-brain\marketing\` → general marketing strategy + outreach
- `C:\Users\USER\Documents\50techbridge-content\marketing\` → article content + prospect dossiers

---

## ⚠ READ THIS FIRST — git sync status

This folder is a **working snapshot** of two git repos. The flat-file structure in the git repos has **not yet been updated** to match the new subfolder organization below.

**Files NEW as of 2026-04-16 that do NOT exist in git yet (must be committed):**
- `LINKEDIN-DAILY-PROCESS.md` (root)
- `LINKEDIN-PROFILE-CHECKLIST.md` (root)
- `linkedin-correspondence-log.csv` (root)

**Decision required:**
- **Option A (recommended):** Commit new files + new folder structure to `lmt-claude-brain` repo, then this snapshot stays accurate
- **Option B:** Stop using git as canonical; make this the working copy
- **Option C:** Leave as-is and manually reconcile when sync is run

Ask Claude: *"commit today's marketing changes to lmt-claude-brain"* to execute Option A.

---

## Folder Structure (root → subfolders)

### 📍 Root — Hot files (core, referenced by CEO-DASHBOARD, Claude CLI triggers, LinkedIn process)

| File | Purpose |
|---|---|
| `README.md` | This index |
| `DECISION-MAKER-TARGET-LIST.md` | 4-tier named target list + LinkedIn search strings |
| `DECISION-MAKER-ACCESS-PLAYBOOK.md` | How to reach senior buyers |
| `PROSPECTS-INDEX.md` | Master index of researched dossiers (1–5 ratings) |
| `WEEKLY-RHYTHM.md` | Mon–Fri cadence: what runs daily vs 3–4x/week |
| `LMT-CAPABILITY-STATEMENT.md` | Sales capability one-pager |
| `accounts.md` | High-level accounts list |

### 📂 `linkedIn/` — All LinkedIn operations in one place
- `LINKEDIN-DAILY-PROCESS.md` — FOCUS LOCK + 3-block daily routine
- `LINKEDIN-PROFILE-CHECKLIST.md` — 12-priority profile maximization
- `LINKEDIN-SERVICES-CATEGORIES.md` — LinkedIn Services page categories
- `linkedin-correspondence-log.csv` — 12-col touch tracker

### 📂 `prospects/` (existing — unchanged)
Individual researched dossier markdown files (e.g., `2026-04-08-carly-roszkowski.md`). See `PROSPECTS-INDEX.md` at root for the full index.

### 📂 `workforce/` — WIOA + funding intelligence
- `WIOA-BUYER-JOURNEY.md` — buyer journey for workforce board contracts
- `WIOA-ETPL-APPLICATION-PACKET.md` — Texas ETPL application requirements
- `funding-and-channels-intel.md` — where the money is + 8-org network map
- `wioa-prospects.md` — pipeline of 28 Texas WDBs as targets
- `prospects-and-funding.csv` — 60+ row master CSV (people, orgs, funding)
- `wioa-etpl-forms/` — ETPL form files

### 📂 `templates/` — Messages, proposals, and reference tools
- `EMAIL-SEQUENCES.md` — email outreach sequences
- `linkedin-message-templates.md` — LinkedIn DM templates
- `outreach-templates.md` — T1/T2/T3 connection + DM templates
- `RETAINER-PROPOSAL-TEMPLATE.md` — consulting retainer template
- `WORKSHOP-SELL-SHEET.md` — 90-min workshop sell sheet
- `Canva-Cheat-Sheet.md` — Canva reference
- `YOAST-SEO-SKILL.md` — Yoast SEO reference
- `email-sequences/` — additional email sequence assets

### 📂 `events/` — Calendar + tracker
- `EVENTS-CALENDAR-2026.md` — workforce/HR conferences calendar
- `events-tracker-2026.xlsx` — event tracking spreadsheet
- `build_events_xlsx.py` — Python script that builds the xlsx

### 📂 `strategy/` — High-level plans + reviews
- `COMMUNITY-LAUNCH-PLAN.md` — community launch plan
- `PROMOTION-BUDGET-2026.md` — marketing budget plan
- `SOCIAL-STRATEGY-REVIEW-2026-04.md` — April 2026 social review
- `small-company-entry-and-social-channels.md` — 4 entry paths + social channels
- `content-schedule.md` — content publishing schedule

### 📂 `drafts/` — Article drafts + scheduled posts (pre-publishing)
- `article-its-not-about-the-data-plaintext.txt` — "It's Not About the Data" manifesto draft
- `linkedin-article-ai-amplifies.md` — "AI amplifies" LinkedIn article draft
- `SOCIAL-POSTS-WEEK-OF-APRIL-14.txt` — week-of-April-14 social posts

---

## Editing rules (unchanged from prior README)

- ✅ READ any file here freely
- ✅ COPY content from here to LinkedIn / email / Canva / wherever
- ⚠️ If you want to EDIT a file that exists in git (lmt-claude-brain or 50techbridge-content), edit the version in the git repo so changes persist across sessions
- ✅ For NEW files created this session (see list at top), they live here only until committed to git — ask Claude to commit them

---

## How to refresh this snapshot from git

Ask Claude: *"sync the marketing folder from git"*

⚠️ Warning: a fresh sync will flatten the subfolder structure back to the git layout unless git has been updated with the new structure first.

---

## GitHub

- https://github.com/1Profmac/lmt-claude-brain (private)
- https://github.com/1Profmac/50techbridge-content (private)
