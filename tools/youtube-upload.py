"""
YOUTUBE-UPLOAD — Upload videos to YouTube from the command line.
Learn More Technologies | learnmoretechnologies.com

USAGE:
  # Upload a video (unlisted — safe for landing page embed):
  python tools/youtube-upload.py upload "path/to/video.mp4" --title "Video Title"

  # Upload as public (visible on channel/search):
  python tools/youtube-upload.py upload "video.mp4" --title "Title" --privacy public

  # Upload with description and tags:
  python tools/youtube-upload.py upload "video.mp4" --title "Title" --description "..." --tags AI technology 50plus

  # Print only the video ID (for scripting):
  python tools/youtube-upload.py upload "video.mp4" --title "Title" --id-only

SETUP (one time):
  1. Go to https://console.cloud.google.com
  2. Create or select a project
  3. APIs & Services → Library → search "YouTube Data API v3" → Enable
  4. APIs & Services → Credentials → Create Credentials → OAuth client ID
  5. Application type: Desktop app → Create
  6. Download JSON → save as tools/youtube-client-secrets.json
  7. First run will open browser for authorization → token cached automatically

NOTES:
  - youtube-client-secrets.json and .youtube-token.json are gitignored (credentials stay local)
  - Videos default to "unlisted" — embeds on site but not searchable
  - Use --privacy public when you're ready to promote on channel
  - Resumable upload — safe for large files, auto-retries on network hiccup
"""

import sys
import os
import json
import argparse
import time

try:
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
except ImportError:
    print("ERROR: Missing dependencies. Run:")
    print("  pip install google-api-python-client google-auth-oauthlib google-auth-httplib2")
    sys.exit(1)


# --- Config ---

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SECRETS_FILE = os.path.join(SCRIPT_DIR, "youtube-client-secrets.json")
TOKEN_FILE = os.path.join(SCRIPT_DIR, ".youtube-token.json")
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
CHUNK_SIZE = 5 * 1024 * 1024  # 5MB resumable chunks


def get_youtube_client():
    """Authenticate and return an authorized YouTube API client."""
    if not os.path.exists(SECRETS_FILE):
        print(f"ERROR: Client secrets not found at {SECRETS_FILE}")
        print()
        print("SETUP:")
        print("1. https://console.cloud.google.com → select project")
        print("2. APIs & Services → Enable 'YouTube Data API v3'")
        print("3. Credentials → Create OAuth client ID → Desktop app → Download JSON")
        print(f"4. Save as: {SECRETS_FILE}")
        sys.exit(1)

    creds = None

    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
            print("  Token refreshed.")
        else:
            flow = InstalledAppFlow.from_client_secrets_file(SECRETS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
            print("  Authorization complete.")

        with open(TOKEN_FILE, "w") as f:
            f.write(creds.to_json())

    return build("youtube", "v3", credentials=creds)


def upload_video(filepath, title, description="", privacy="unlisted", thumbnail=None, tags=None):
    """Upload an MP4 to YouTube. Returns the video ID."""
    filepath = os.path.abspath(filepath)

    if not os.path.exists(filepath):
        print(f"ERROR: File not found: {filepath}")
        sys.exit(1)

    file_size_mb = os.path.getsize(filepath) / 1024 / 1024
    print(f"\nUploading: {os.path.basename(filepath)}")
    print(f"  Size:    {file_size_mb:.1f} MB")
    print(f"  Title:   {title}")
    print(f"  Privacy: {privacy}")
    print()

    youtube = get_youtube_client()

    body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags or ["50plus", "AI", "technology", "LearnMoreTechnologies"],
            "categoryId": "27",  # Education
            "defaultLanguage": "en",
        },
        "status": {
            "privacyStatus": privacy,
            "selfDeclaredMadeForKids": False,
        },
    }

    media = MediaFileUpload(
        filepath,
        mimetype="video/mp4",
        chunksize=CHUNK_SIZE,
        resumable=True,
    )

    request = youtube.videos().insert(
        part="snippet,status",
        body=body,
        media_body=media,
    )

    # Resumable upload with progress bar
    response = None
    start_time = time.time()
    last_pct = -1

    print("  Uploading ", end="", flush=True)
    while response is None:
        try:
            status, response = request.next_chunk()
        except Exception as e:
            print(f"\n  Upload error: {e}")
            print("  Retrying in 5 seconds...")
            time.sleep(5)
            continue

        if status:
            pct = int(status.progress() * 100)
            if pct != last_pct:
                print(f"{pct}% ", end="", flush=True)
                last_pct = pct

    elapsed = time.time() - start_time
    video_id = response["id"]
    print(f"\n\n  Done in {elapsed:.0f}s")
    print(f"  Video ID: {video_id}")
    print(f"  Watch:    https://www.youtube.com/watch?v={video_id}")

    # Set thumbnail if provided
    if thumbnail and os.path.exists(thumbnail):
        ext = os.path.splitext(thumbnail)[1].lower()
        mime = "image/jpeg" if ext in (".jpg", ".jpeg") else "image/png"
        youtube.thumbnails().set(
            videoId=video_id,
            media_body=MediaFileUpload(thumbnail, mimetype=mime),
        ).execute()
        print(f"  Thumbnail set: {os.path.basename(thumbnail)}")

    return video_id


def print_embed_snippet(video_id):
    """Print the iframe embed code ready to paste into the landing page."""
    snippet = (
        f'\n  <iframe\n'
        f'    src="https://www.youtube.com/embed/{video_id}?rel=0&modestbranding=1"\n'
        f'    allow="accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture"\n'
        f'    allowfullscreen loading="lazy"\n'
        f'    title="Learn More Technologies">\n'
        f'  </iframe>'
    )
    print()
    print("  --- LANDING PAGE EMBED (paste into hero-video iframe) ---")
    print(snippet)
    print("  ----------------------------------------------------------")
    print()
    print(f"  Or update the src URL in the live page to:")
    print(f"  https://www.youtube.com/embed/{video_id}?rel=0&modestbranding=1")


# --- Main ---

def main():
    parser = argparse.ArgumentParser(
        description="Upload videos to YouTube | Learn More Technologies",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    subparsers = parser.add_subparsers(dest="command")

    up = subparsers.add_parser("upload", help="Upload a video file to YouTube")
    up.add_argument("filepath", help="Path to the MP4 file")
    up.add_argument("--title", required=True, help="Video title on YouTube")
    up.add_argument("--description", default=(
        "Learn More Technologies helps adults 50+ own the digital age.\n\n"
        "Free AI curriculum | WIOA-eligible | MBE Certified\n"
        "https://learnmoretechnologies.com"
    ), help="Video description")
    up.add_argument(
        "--privacy",
        choices=["unlisted", "public", "private"],
        default="unlisted",
        help="Privacy setting (default: unlisted — embeds on site but not searchable)"
    )
    up.add_argument("--thumbnail", help="Path to thumbnail image (JPG or PNG)")
    up.add_argument("--tags", nargs="+", help="Space-separated tags")
    up.add_argument("--id-only", action="store_true", help="Print only the video ID (for scripting)")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    if args.command == "upload":
        video_id = upload_video(
            filepath=args.filepath,
            title=args.title,
            description=args.description,
            privacy=args.privacy,
            thumbnail=getattr(args, "thumbnail", None),
            tags=getattr(args, "tags", None),
        )

        if args.id_only:
            print(video_id)
        else:
            print_embed_snippet(video_id)


if __name__ == "__main__":
    main()
