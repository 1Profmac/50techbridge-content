"""
WP-PUBLISH — Push markdown articles to WordPress as drafts or publish them.
Learn More Technologies | learnmoretechnologies.com

USAGE:
  # Push a single article as draft:
  python wp-publish.py draft "content/articles/influence-is-not-who-you-know.md"

  # Push a single article and publish immediately:
  python wp-publish.py publish "content/articles/influence-is-not-who-you-know.md"

  # Push all .md files in a folder as drafts:
  python wp-publish.py draft-folder "content/articles/"

  # List all current drafts on WP:
  python wp-publish.py list-drafts

  # Publish an existing draft by WP post ID:
  python wp-publish.py publish-id 2290

SETUP (one time):
  1. In WP Admin: Users → Your Profile → Application Passwords
  2. Create a new app password named "Claude CLI"
  3. Copy the password (spaces are fine — include them)
  4. Create the .env file:
     echo WP_USER=brian@learnmoretechnologies.com > Desktop/LMT/tools/.env
     echo WP_APP_PASSWORD=xxxx xxxx xxxx xxxx xxxx xxxx >> Desktop/LMT/tools/.env
  5. Test: python wp-publish.py list-drafts

NOTES:
  - .env file is gitignored — credentials never go to GitHub
  - After publish, a LinkedIn post is generated and copied to clipboard
  - Articles with frontmatter (title, slug, category, tags) will use those values
  - Articles without frontmatter will extract title from first # heading
"""

import sys
import os
import re
import base64
import json
import glob
import subprocess
import markdown

try:
    import frontmatter
    HAS_FRONTMATTER = True
except ImportError:
    HAS_FRONTMATTER = False

try:
    import requests
except ImportError:
    print("ERROR: requests not installed. Run: pip install requests")
    sys.exit(1)


# --- Config ---

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_FILE = os.path.join(SCRIPT_DIR, ".env")
WP_SITE = "https://learnmoretechnologies.com"
WP_API = f"{WP_SITE}/wp-json/wp/v2"


def load_env():
    """Load credentials from .env file."""
    if not os.path.exists(ENV_FILE):
        print(f"ERROR: No .env file found at {ENV_FILE}")
        print()
        print("SETUP INSTRUCTIONS:")
        print("1. Go to WP Admin → Users → Your Profile → Application Passwords")
        print("2. Create app password named 'Claude CLI'")
        print("3. Create .env file in this folder:")
        print(f'   echo WP_USER=brian@learnmoretechnologies.com > "{ENV_FILE}"')
        print(f'   echo WP_APP_PASSWORD=your_app_password_here >> "{ENV_FILE}"')
        sys.exit(1)

    env = {}
    with open(ENV_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if "=" in line and not line.startswith("#"):
                key, val = line.split("=", 1)
                env[key.strip()] = val.strip()

    user = env.get("WP_USER")
    password = env.get("WP_APP_PASSWORD")

    if not user or not password:
        print("ERROR: .env file must contain WP_USER and WP_APP_PASSWORD")
        sys.exit(1)

    return user, password


def get_auth_headers(user, password):
    """Build auth headers for WP REST API.
    Uses browser-like User-Agent to avoid Bluehost ModSecurity blocking."""
    token = base64.b64encode(f"{user}:{password}".encode()).decode()
    return {
        "Authorization": f"Basic {token}",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
        "Accept": "application/json, text/plain, */*",
    }


def parse_markdown_file(filepath):
    """Parse a markdown file into title, slug, content, and metadata."""
    with open(filepath, "r", encoding="utf-8") as f:
        raw = f.read()

    meta = {}
    content = raw

    # Try frontmatter parsing
    if HAS_FRONTMATTER:
        post = frontmatter.loads(raw)
        if post.metadata:
            meta = post.metadata
            content = post.content

    # Extract title from first # heading if not in frontmatter
    title = meta.get("title", "")
    if not title:
        match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        if match:
            title = match.group(1).strip()
            # Remove the title line from content
            content = content[match.end():].strip()

    # Generate slug from title if not provided
    slug = meta.get("slug", "")
    if not slug and title:
        slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")

    # Convert markdown to HTML
    md = markdown.Markdown(extensions=["tables", "fenced_code"])
    html_content = md.convert(content)

    # Clean up — remove byline if present (it's in the author field)
    html_content = re.sub(
        r"<strong>By Professor Brian McKinney.*?</strong>", "", html_content
    )

    # Remove hashtags at the end (those go in tags)
    html_content = re.sub(r"<p>#\w+(\s+#\w+)*\s*</p>\s*$", "", html_content)

    # Append sponsor CTA block
    sponsor_cta = (
        '<hr>\n'
        '<h3>Bring 50+TechBridge to Your Community</h3>\n'
        '<p>We train adults 50+ in AI and digital skills at senior centers, libraries, '
        'churches, and workplaces. Sponsors cover the session so learners never pay.</p>\n'
        '<p><strong>$500 covers one Lunch &amp; Learn for 20 Pioneers.</strong> '
        '$25 per person. 90 minutes. Real skills. Real impact.</p>\n'
        '<p>Organizations get completion tracking and an impact report. '
        'Every session builds toward our goal of 50,000 Pioneers.</p>\n'
        '<p><strong><a href="https://calendly.com/brianmckinney/new-meeting">'
        'Sponsor a session</a></strong></p>\n'
    )
    html_content += sponsor_cta

    # Extract tags from hashtags
    tags = meta.get("tags", [])
    hashtags = re.findall(r"#(\w+)", raw[-500:])  # Check last 500 chars
    if hashtags and not tags:
        tags = hashtags

    return {
        "title": title,
        "slug": slug,
        "content": html_content,
        "tags": tags,
        "category": meta.get("category", ""),
        "excerpt": meta.get("excerpt", meta.get("meta_description", "")),
        "focus_keyphrase": meta.get("focus_keyphrase", ""),
    }


def get_or_create_category(name, headers):
    """Find a category by name or create it."""
    if not name:
        return None

    # Search for existing
    resp = requests.get(
        f"{WP_API}/categories", params={"search": name}, headers=headers
    )
    if resp.ok and resp.json():
        return resp.json()[0]["id"]

    # Create new
    resp = requests.post(
        f"{WP_API}/categories",
        json={"name": name},
        headers=headers,
    )
    if resp.ok:
        return resp.json()["id"]

    return None


def get_or_create_tags(tag_names, headers):
    """Find or create tags, return list of IDs."""
    if not tag_names:
        return []

    tag_ids = []
    for name in tag_names:
        name = name.strip()
        if not name:
            continue

        # Search existing
        resp = requests.get(
            f"{WP_API}/tags", params={"search": name}, headers=headers
        )
        if resp.ok and resp.json():
            tag_ids.append(resp.json()[0]["id"])
            continue

        # Create new
        resp = requests.post(
            f"{WP_API}/tags", json={"name": name}, headers=headers
        )
        if resp.ok:
            tag_ids.append(resp.json()["id"])

    return tag_ids


def push_to_wp(parsed, status, headers):
    """Push article to WordPress. Status: 'draft' or 'publish'.
    Uses chunked upload to avoid Bluehost ModSecurity blocking large payloads."""

    # Step 1: Create post with title only (avoids ModSecurity on large content)
    data = {
        "title": parsed["title"],
        "content": "<p>Loading...</p>",
        "status": "draft",
        "slug": parsed["slug"],
        "author": 1,
    }

    if parsed.get("excerpt"):
        data["excerpt"] = parsed["excerpt"]

    # Handle category
    cat_id = get_or_create_category(parsed.get("category"), headers)
    if cat_id:
        data["categories"] = [cat_id]

    # Handle tags
    tag_ids = get_or_create_tags(parsed.get("tags", []), headers)
    if tag_ids:
        data["tags"] = tag_ids

    resp = requests.post(f"{WP_API}/posts", json=data, headers=headers)

    if not resp.ok:
        print(f"  FAILED to create post — {resp.status_code}: {resp.text[:300]}")
        return None

    post_id = resp.json()["id"]
    print(f"  Created draft — WP ID: {post_id}")

    # Step 2: Upload content in chunks to avoid ModSecurity
    content = parsed["content"]
    chunk_size = 2000
    chunks = [content[i:i + chunk_size] for i in range(0, len(content), chunk_size)]
    full_content = ""

    for i, chunk in enumerate(chunks):
        full_content += chunk
        resp2 = requests.post(
            f"{WP_API}/posts/{post_id}",
            json={"content": full_content},
            headers=headers,
        )
        if resp2.ok:
            print(f"  Chunk {i + 1}/{len(chunks)} uploaded")
        else:
            print(f"  Chunk {i + 1} FAILED — {resp2.status_code}: {resp2.text[:200]}")
            print(f"  Post created as draft (ID {post_id}) but content may be incomplete.")
            return resp2.json() if resp2.ok else None

    # Step 3: Set final status (publish if requested)
    if status == "publish":
        resp3 = requests.post(
            f"{WP_API}/posts/{post_id}",
            json={"status": "publish"},
            headers=headers,
        )
        if resp3.ok:
            post = resp3.json()
            print(f"  PUBLISHED — {post['link']}")
            copy_linkedin_post(parsed["title"], post["link"], parsed.get("excerpt", ""))
            return post
        else:
            print(f"  Content uploaded but publish FAILED — {resp3.status_code}")
            print(f"  Post is saved as draft (ID {post_id}). Publish manually in WP.")
            return None
    else:
        post = resp2.json() if resp2.ok else None
        if post:
            print(f"  Draft saved — WP ID: {post_id}")
            print(f"  Slug: {parsed['slug']}")
        return post


def publish_existing(post_id, headers):
    """Publish an existing draft by WP post ID."""
    resp = requests.post(
        f"{WP_API}/posts/{post_id}",
        json={"status": "publish"},
        headers=headers,
    )

    if resp.ok:
        post = resp.json()
        print(f"  PUBLISHED — WP ID: {post['id']}")
        print(f"  Title: {post['title']['rendered']}")
        print(f"  URL: {post['link']}")
        copy_linkedin_post(post["title"]["rendered"], post["link"])
        return post
    else:
        print(f"  FAILED — {resp.status_code}: {resp.text[:300]}")
        return None


def copy_linkedin_post(title, url, excerpt=""):
    """Generate a LinkedIn post and copy it to clipboard."""
    post = f"""{title}

{excerpt if excerpt else "New from Learn More Technologies — read the full article:"}

{url}

#50PlusTechBridge #AIForEveryone #YoureNotDoneYet #WorkforceDevelopment"""

    try:
        subprocess.run(["clip"], input=post.encode("utf-8"), check=True)
        print()
        print("  --- LINKEDIN POST COPIED TO CLIPBOARD ---")
        print("  Open LinkedIn > New Post > Ctrl+V > Post")
        print("  -----------------------------------------")
    except Exception:
        print()
        print("  --- LINKEDIN POST (copy manually) ---")
        print(post)
        print("  -------------------------------------")


def list_drafts(headers):
    """List all draft posts on WP."""
    page = 1
    all_drafts = []

    while True:
        resp = requests.get(
            f"{WP_API}/posts",
            params={"status": "draft", "per_page": 50, "page": page},
            headers=headers,
        )
        if not resp.ok or not resp.json():
            break
        all_drafts.extend(resp.json())
        page += 1

    if not all_drafts:
        print("No drafts found.")
        return

    print(f"\n{'ID':<8} {'Title':<70} {'Slug'}")
    print("-" * 120)
    for post in sorted(all_drafts, key=lambda p: p.get("menu_order", 0)):
        title = post["title"]["rendered"][:68]
        print(f"{post['id']:<8} {title:<70} {post['slug']}")

    print(f"\nTotal drafts: {len(all_drafts)}")


# --- Main ---

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    command = sys.argv[1].lower()
    user, password = load_env()
    headers = get_auth_headers(user, password)

    if command == "list-drafts":
        list_drafts(headers)

    elif command in ("draft", "publish"):
        if len(sys.argv) < 3:
            print(f"Usage: python wp-publish.py {command} <path-to-markdown-file>")
            sys.exit(1)

        filepath = sys.argv[2]
        if not os.path.exists(filepath):
            # Try relative to LMT folder
            alt = os.path.join(os.path.dirname(SCRIPT_DIR), filepath)
            if os.path.exists(alt):
                filepath = alt
            else:
                print(f"ERROR: File not found: {filepath}")
                sys.exit(1)

        print(f"\nParsing: {filepath}")
        parsed = parse_markdown_file(filepath)
        print(f"  Title: {parsed['title']}")
        print(f"  Slug: {parsed['slug']}")
        print(f"  Pushing to WP as {command}...")
        push_to_wp(parsed, command, headers)

    elif command == "draft-folder":
        if len(sys.argv) < 3:
            print("Usage: python wp-publish.py draft-folder <folder-path>")
            sys.exit(1)

        folder = sys.argv[2]
        if not os.path.isdir(folder):
            alt = os.path.join(os.path.dirname(SCRIPT_DIR), folder)
            if os.path.isdir(alt):
                folder = alt
            else:
                print(f"ERROR: Folder not found: {folder}")
                sys.exit(1)

        files = sorted(glob.glob(os.path.join(folder, "*.md")))
        if not files:
            print(f"No .md files found in {folder}")
            sys.exit(1)

        print(f"\nFound {len(files)} markdown files in {folder}\n")
        for f in files:
            print(f"Parsing: {os.path.basename(f)}")
            parsed = parse_markdown_file(f)
            print(f"  Title: {parsed['title']}")
            push_to_wp(parsed, "draft", headers)
            print()

    elif command == "publish-id":
        if len(sys.argv) < 3:
            print("Usage: python wp-publish.py publish-id <wp-post-id>")
            sys.exit(1)

        post_id = sys.argv[2]
        print(f"\nPublishing WP post ID {post_id}...")
        publish_existing(post_id, headers)

    else:
        print(f"Unknown command: {command}")
        print("Commands: draft, publish, draft-folder, list-drafts, publish-id")
        sys.exit(1)


if __name__ == "__main__":
    main()
