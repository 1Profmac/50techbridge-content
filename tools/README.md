# LMT Tools

## Homepage Page Revisions — learnmoretechnologies.com

**File:** `BRAND/pages/LMT-Homepage.html` (always the live version)
**WP Page ID:** 1454

### Process (the only method that works — REST API is blocked by ModSecurity)

1. Tell Claude what to change — Claude edits the file and drops it on the Desktop
2. Open the file → Ctrl+A → Ctrl+C
3. WP Admin → Pages → Home → Edit → ⋮ menu → Code editor
4. Ctrl+A → Ctrl+V → Save
5. Claude commits the updated file to git

**Note:** Do NOT attempt WP REST API, XML-RPC, or Python scripts to update this page. All blocked by Bluehost ModSecurity. Paste-into-WP-editor is the only method confirmed working.

---

## wp-publish.py — WordPress Publisher

Push markdown articles to WordPress from the command line.

### One-Time Setup

1. Go to **WP Admin → Users → Your Profile → Application Passwords**
2. Enter name: `Claude CLI`
3. Click **Add New Application Password**
4. Copy the password (keep the spaces)
5. Create the .env file:

```bash
cd Desktop/LMT/tools
echo "WP_USER=brian@learnmoretechnologies.com" > .env
echo "WP_APP_PASSWORD=xxxx xxxx xxxx xxxx xxxx xxxx" >> .env
```

### Commands

```bash
# Push one article as draft
python tools/wp-publish.py draft "content/articles/influence-is-not-who-you-know.md"

# Push one article and publish immediately (auto-shares to LinkedIn)
python tools/wp-publish.py publish "content/articles/influence-is-not-who-you-know.md"

# Push all articles in a folder as drafts
python tools/wp-publish.py draft-folder "content/articles/"

# List all drafts currently on WP
python tools/wp-publish.py list-drafts

# Publish an existing draft by WP ID
python tools/wp-publish.py publish-id 2290
```

### How It Works

1. Reads markdown file
2. Extracts title from `# Heading` or frontmatter
3. Converts markdown to HTML
4. Pushes to WordPress via REST API
5. If you use `publish` instead of `draft`, a LinkedIn post is auto-generated and copied to your clipboard — just open LinkedIn, paste, and post

### .env Security

The `.env` file contains your WP password. It is gitignored and never committed.
