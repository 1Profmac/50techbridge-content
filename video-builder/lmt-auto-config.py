"""
LMT Auto Config Generator
===========================
Reads a PLAINTEXT article and automatically generates a video config.json.
Splits article into timed slides, generates ElevenLabs voiceover,
and creates SRT captions.

Usage:
    python lmt-auto-config.py article.txt heygen-video.mp4 [output-dir]

Example:
    python lmt-auto-config.py workforce-article-1-PLAINTEXT.txt heygen-clean.mp4 ./output
"""

import json
import sys
import os
import re
import urllib.request
from dotenv import load_dotenv

load_dotenv()

FFMPEG = "C:/tools/ffmpeg-8.1-essentials_build/bin/ffmpeg.exe"
ELEVENLABS_KEY = os.getenv("ELEVENLABS_API_KEY", "")
VOICE_ID = "uAs0vN0GLLpz7FM7JVkz"  # Brian McKinney clone


def get_video_duration(video_path):
    """Get video duration in seconds."""
    import subprocess
    ffprobe = FFMPEG.replace("ffmpeg.exe", "ffprobe.exe")
    cmd = [ffprobe, "-v", "quiet", "-print_format", "json", "-show_format", video_path]
    result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if result.returncode == 0:
        info = json.loads(result.stdout)
        return float(info["format"]["duration"])
    return 300


def parse_article(article_path):
    """Parse a PLAINTEXT article into sections."""
    with open(article_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Split by double newlines (paragraph breaks) or section headers
    lines = text.strip().split("\n")

    sections = []
    current_section = {"title": "", "bullets": [], "raw_text": ""}

    for line in lines:
        line = line.strip()
        if not line:
            if current_section["bullets"] or current_section["raw_text"]:
                sections.append(current_section)
                current_section = {"title": "", "bullets": [], "raw_text": ""}
            continue

        # Check if it's a header (ALL CAPS or starts with #)
        if line.isupper() and len(line) > 10:
            if current_section["bullets"] or current_section["raw_text"]:
                sections.append(current_section)
            current_section = {"title": line, "bullets": [], "raw_text": ""}
        elif line.startswith("- ") or line.startswith("* "):
            # Bullet point
            bullet = line.lstrip("- *").strip()
            # Replace % with "percent" for FFmpeg
            bullet = bullet.replace("%", " percent")
            current_section["bullets"].append(bullet)
        else:
            current_section["raw_text"] += " " + line

    if current_section["bullets"] or current_section["raw_text"]:
        sections.append(current_section)

    # Filter out metadata sections (author, hashtags, type info)
    filtered = []
    for s in sections:
        text_lower = (s["title"] + s["raw_text"]).lower()
        if any(skip in text_lower for skip in ["type:", "audience:", "cta:", "author:", "#workforce", "#adults", "seo", "meta description", "primary keyword", "target audience"]):
            continue
        if s["bullets"] or len(s["raw_text"].strip()) > 30:
            filtered.append(s)

    # Consolidate: merge small sections into their parent header sections
    # Target: 8-12 sections max
    consolidated = []
    current = None

    for s in filtered:
        if s["title"]:
            # New header section — save previous and start new
            if current:
                consolidated.append(current)
            current = {"title": s["title"], "bullets": list(s["bullets"]), "raw_text": s["raw_text"]}
        else:
            # No title — merge into current section
            if current:
                current["bullets"].extend(s["bullets"])
                current["raw_text"] += " " + s["raw_text"]
            else:
                current = {"title": "", "bullets": list(s["bullets"]), "raw_text": s["raw_text"]}

    if current:
        consolidated.append(current)

    # If still too many, keep only the ones with headers + first/last
    if len(consolidated) > 12:
        consolidated = consolidated[:11] + [consolidated[-1]]

    return consolidated


def sections_to_slides(sections, total_duration):
    """Convert article sections into timed slides."""
    # Reserve 12s for title, 30s for end card
    content_duration = total_duration - 42
    # Minimum 20 seconds per slide for readability
    max_slides = int(content_duration / 20)
    sections = sections[:max_slides]
    time_per_section = content_duration / max(len(sections), 1)

    slides = []
    current_time = 0

    # Title slide
    title_text = sections[0]["title"] if sections and sections[0]["title"] else "50+TechBridge"
    slides.append({
        "start": 0,
        "end": 12,
        "x": 80,
        "y": 250,
        "font_size": 48,
        "color": "#FFFFFF",
        "fade": 0.8,
        "no_bullet": True,
        "chapter_label": "Introduction",
        "bullets": [title_text[:40], title_text[40:80] if len(title_text) > 40 else ""]
    })
    current_time = 12

    # Content slides
    for i, section in enumerate(sections):
        end_time = min(current_time + time_per_section, total_duration - 30)

        if section["bullets"]:
            # Use bullet points directly (max 4 per slide)
            bullets = section["bullets"][:4]
        else:
            # Extract key sentences from raw text
            sentences = [s.strip() for s in section["raw_text"].split(".") if len(s.strip()) > 15]
            bullets = sentences[:4]

        # Shorten bullets to fit on screen
        bullets = [b[:55] for b in bullets if b.strip()]

        if not bullets:
            continue

        # Determine if this is a highlight slide
        is_highlight = any(word in section.get("title", "").lower() for word in
                         ["cost", "question", "built", "result", "ready", "unlock"])

        slide = {
            "start": round(current_time),
            "end": round(end_time),
            "x": 80,
            "y": 250,
            "font_size": 46,
            "color": "#FFFFFF",
            "chapter_label": section.get("title", f"Section {i+1}")[:50],
            "bullets": bullets
        }

        # Add source tags for data-heavy sections
        raw_lower = section["raw_text"].lower()
        if "aarp" in raw_lower or "oxford" in raw_lower:
            slide["source"] = "Source: AARP / Oxford Economics"
        elif "shrm" in raw_lower:
            slide["source"] = "Source: SHRM"
        elif "mit" in raw_lower or "kellogg" in raw_lower:
            slide["source"] = "Source: MIT / Kellogg / AARP"

        slides.append(slide)
        current_time = end_time

    # End card (last 30 seconds)
    slides.append({
        "start": round(total_duration - 30),
        "end": round(total_duration),
        "x": 80,
        "y": 250,
        "font_size": 46,
        "color": "#C8942E",
        "fade": 1.0,
        "no_bullet": True,
        "chapter_label": "Contact and next steps",
        "bullets": [
            "Learn More Technologies",
            "learnmoretechnologies.com/workforce",
            "",
            "Schedule a free consult:",
            "calendly.com/brianmckinney/new-meeting",
            "",
            "Brian McKinney | MBE Certified | Former AARP Insider"
        ]
    })

    return slides


def generate_voiceover(text, output_path):
    """Generate voiceover using ElevenLabs API."""
    if not ELEVENLABS_KEY:
        print("  WARNING: No ElevenLabs API key. Skipping voiceover.")
        return None

    data = json.dumps({
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}
    }).encode()

    req = urllib.request.Request(
        f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}",
        data=data,
        headers={"xi-api-key": ELEVENLABS_KEY, "Content-Type": "application/json"}
    )

    try:
        resp = urllib.request.urlopen(req)
        with open(output_path, "wb") as f:
            f.write(resp.read())
        size = os.path.getsize(output_path)
        print(f"  Voiceover: {size/1024:.0f} KB -> {output_path}")
        return output_path
    except Exception as e:
        print(f"  Voiceover ERROR: {e}")
        return None


def generate_srt(slides, output_path):
    """Generate SRT caption file from slides."""
    lines = []
    counter = 1

    for slide in slides:
        start = slide["start"]
        end = slide["end"]

        for bullet in slide["bullets"]:
            if not bullet.strip():
                continue

            # SRT timestamp format
            s_h, s_m, s_s = int(start//3600), int((start%3600)//60), start%60
            e_h, e_m, e_s = int(end//3600), int((end%3600)//60), end%60

            lines.append(str(counter))
            lines.append(f"{s_h:02d}:{s_m:02d}:{s_s:06.3f} --> {e_h:02d}:{e_m:02d}:{e_s:06.3f}")
            lines.append(bullet.replace("-  ", "").strip())
            lines.append("")
            counter += 1

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"  Captions: {output_path}")
    return output_path


def main():
    if len(sys.argv) < 3:
        print("Usage: python lmt-auto-config.py <article.txt> <heygen-video.mp4> [output-dir]")
        print("")
        print("Reads article, generates config.json + voiceover + captions automatically.")
        sys.exit(1)

    article_path = sys.argv[1]
    video_path = sys.argv[2]
    output_dir = sys.argv[3] if len(sys.argv) > 3 else os.path.dirname(article_path) or "."

    os.makedirs(output_dir, exist_ok=True)

    print(f"Article: {article_path}")
    print(f"Video: {video_path}")
    print(f"Output: {output_dir}")

    # Get video duration
    duration = get_video_duration(video_path)
    print(f"Duration: {duration:.1f}s ({duration/60:.1f} min)")

    # Parse article
    sections = parse_article(article_path)
    print(f"Sections found: {len(sections)}")

    # Generate slides
    slides = sections_to_slides(sections, duration)
    print(f"Slides generated: {len(slides)}")

    # Generate voiceover from full article text
    with open(article_path, "r", encoding="utf-8") as f:
        full_text = f.read()
    # Clean for voiceover
    vo_text = full_text.replace("#", "").replace("*", "").replace("_", "")
    vo_text = re.sub(r'https?://\S+', '', vo_text)  # remove URLs
    vo_text = re.sub(r'%', ' percent', vo_text)
    vo_path = os.path.join(output_dir, "voiceover.mp3")
    generate_voiceover(vo_text[:5000], vo_path)  # ElevenLabs limit

    # Generate SRT captions
    srt_path = os.path.join(output_dir, "captions.srt")
    generate_srt(slides, srt_path)

    # Build config
    article_name = os.path.splitext(os.path.basename(article_path))[0]
    config = {
        "input_video": os.path.abspath(video_path).replace("\\", "/"),
        "output_video": os.path.join(os.path.abspath(output_dir), f"FINISHED-{article_name}.mp4").replace("\\", "/"),
        "format": "landscape",
        "show_header": True,
        "show_lower_third": True,
        "youtube": {
            "title": slides[0]["bullets"][0] if slides else "Untitled",
            "description": " ".join(sections[0].get("raw_text", "").split()[:30]) if sections else "",
            "thumbnail_time": 51,
            "hashtags": "#WorkforceDevelopment #Adults50Plus #AgeTech #AITraining #DigitalInclusion #WIOA #FutureOfWork #MBECertified #50PlusTechBridge #LearnMoreTechnologies",
            "tags": "workforce development, AI training, adults 50+, agetech, digital inclusion, WIOA, 50+ TechBridge, Learn More Technologies, Brian McKinney"
        },
        "linkedin": {
            "youtube_url": "https://youtu.be/YOUR-VIDEO-ID"
        },
        "slides": slides
    }

    config_path = os.path.join(output_dir, f"{article_name}-config.json")
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)

    print(f"\nConfig saved: {config_path}")
    print(f"\nREADY TO BUILD:")
    print(f"  python lmt-video-overlay.py {config_path}")
    print(f"\nOr review/edit the config first, then run the build.")

    return config_path


if __name__ == "__main__":
    main()
