"""
LMT Video Overlay Builder
==========================
Adds branded text overlays to HeyGen talking-head videos.
Produces finished YouTube/LinkedIn videos from a simple JSON config.

Requires: FFmpeg installed (with Intel QSV for GPU acceleration)
Brand: Learn More Technologies / 50+TechBridge

Usage:
    python lmt-video-overlay.py my-config.json

Config format: see example-config.json in this folder
"""

import json
import sys
import os
import subprocess

# FFmpeg path — update if installed elsewhere
FFMPEG = "C:/Users/Jordyn/Desktop/ffmpeg-8.1-essentials_build/bin/ffmpeg.exe"

# Brand constants
BRAND = {
    "gold": "C8942E",
    "orange": "E8733A",
    "green": "109F35",
    "white": "FFFFFF",
    "body_text": "C4CDD9",
    "muted": "A8B8CC",
    "bg_mid": "162640",
}

# Font paths (Windows)
FONT_HEADING = "'C\\:/Windows/Fonts/georgiab.ttf'"
FONT_BODY = "'C\\:/Windows/Fonts/arial.ttf'"


def build_drawtext_filters(config):
    """Build FFmpeg drawtext filter chain from config."""
    filters = []
    duration = config.get("duration", 300)

    # Persistent header (if enabled)
    if config.get("show_header", True):
        # Gold line top
        filters.append(
            f"drawbox=x=iw*0.10:y=30:w=iw*0.80:h=3:color=0x{BRAND['gold']}:t=fill:"
            f"enable='between(t,0,{duration})'"
        )
        # Header text
        filters.append(
            f"drawtext=fontfile={FONT_HEADING}:"
            f"text='LEARN MORE TECHNOLOGIES':"
            f"fontsize=64:fontcolor=0x{BRAND['gold']}:"
            f"x=(w-text_w)/2:y=40:"
            f"enable='between(t,0,{duration})'"
        )
        # Subheading
        filters.append(
            f"drawtext=fontfile={FONT_BODY}:"
            f"text='50+TechBridge':"
            f"fontsize=36:fontcolor=0x{BRAND['orange']}:"
            f"x=(w-text_w)/2:y=115:"
            f"enable='between(t,0,{duration})'"
        )
        # Gold line bottom
        filters.append(
            f"drawbox=x=iw*0.10:y=158:w=iw*0.80:h=3:color=0x{BRAND['gold']}:t=fill:"
            f"enable='between(t,0,{duration})'"
        )

    # Persistent lower third (if enabled)
    if config.get("show_lower_third", True):
        filters.append(
            f"drawbox=x=0:y=ih-65:w=iw:h=65:color=0x{BRAND['bg_mid']}@0.9:t=fill:"
            f"enable='between(t,0,{duration})'"
        )
        filters.append(
            f"drawbox=x=0:y=ih-67:w=iw:h=3:color=0x{BRAND['gold']}:t=fill:"
            f"enable='between(t,0,{duration})'"
        )
        lower_text = config.get("lower_third_text", "Subscribe   |   Like   |   Share")
        filters.append(
            f"drawtext=fontfile={FONT_BODY}:"
            f"text='{lower_text}':"
            f"fontsize=32:fontcolor=0x{BRAND['gold']}:"
            f"x=(w-text_w)/2:y=h-52:"
            f"enable='between(t,0,{duration})'"
        )

    # Timed text overlay slides
    for slide in config["slides"]:
        start = slide["start"]
        end = slide["end"]
        color = slide.get("color", "#FFFFFF").replace("#", "")
        font_size = slide.get("font_size", 46)
        x = slide.get("x", 80)
        y = slide.get("y", 250)
        fade = slide.get("fade", 0.5)
        no_bullet = slide.get("no_bullet", False)

        bullets = slide["bullets"]
        for j, bullet in enumerate(bullets):
            if not bullet:
                continue
            line_y = y + (j * (font_size + 35))

            prefix = "" if no_bullet else "-  "
            safe_text = (prefix + bullet).replace("%", "%%").replace("'", "\u2019").replace(":", "\\:")

            filters.append(
                f"drawtext=fontfile={FONT_BODY}:"
                f"text='{safe_text}':"
                f"fontsize={font_size}:fontcolor=0x{color}:"
                f"x={x}:y={line_y}:"
                f"enable='between(t,{start},{end})':"
                f"alpha='if(lt(t-{start},{fade}),(t-{start})/{fade},if(lt({end}-t,{fade}),({end}-t)/{fade},1))'"
            )

        # Source reference
        if "source" in slide:
            source_y = y + (len(bullets) * (font_size + 35)) + 20
            safe_source = slide["source"].replace("'", "\u2019").replace(":", "\\:").replace("%", "%%")
            filters.append(
                f"drawtext=fontfile={FONT_BODY}:"
                f"text='{safe_source}':"
                f"fontsize=28:fontcolor=0x{BRAND['muted']}:"
                f"x={x}:y={source_y}:"
                f"enable='between(t,{start},{end})'"
            )

        # Badge
        if "badge" in slide:
            badge_y = y + (len(bullets) * (font_size + 35)) + 20
            safe_badge = slide["badge"].replace("'", "\u2019").replace(":", "\\:").replace("%", "%%")
            filters.append(
                f"drawtext=fontfile={FONT_BODY}:"
                f"text='{safe_badge}':"
                f"fontsize=16:fontcolor=0x{BRAND['green']}:"
                f"x={x}:y={badge_y}:"
                f"enable='between(t,{start},{end})'"
            )

    return ",".join(filters)


def get_video_duration(input_video):
    """Get video duration using ffprobe."""
    ffprobe = FFMPEG.replace("ffmpeg.exe", "ffprobe.exe")
    cmd = [ffprobe, "-v", "quiet", "-print_format", "json", "-show_format", input_video]
    result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if result.returncode == 0:
        info = json.loads(result.stdout)
        return float(info["format"]["duration"])
    return 300


def build_video(config):
    """Build the video using FFmpeg with Intel QSV (GPU) or libx264 (CPU) fallback."""
    input_video = config["input_video"]
    output_video = config["output_video"]

    print(f"Input:  {input_video}")
    print(f"Output: {output_video}")

    # Get actual duration
    duration = get_video_duration(input_video)
    config["duration"] = duration
    print(f"Duration: {duration:.1f}s ({duration/60:.1f} min)")

    # Build filter chain
    print("Building overlay filters...")
    vf = build_drawtext_filters(config)
    print(f"Filters: {len(config['slides'])} slides")

    # Try Intel QSV (GPU) first
    cmd = [
        FFMPEG, "-y",
        "-i", input_video,
        "-vf", vf,
        "-c:v", "h264_qsv",
        "-preset", "fast",
        "-b:v", "5M",
        "-c:a", "aac",
        "-b:a", "128k",
        output_video,
    ]

    print("Rendering (Intel QSV GPU)...")
    result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")

    if result.returncode != 0:
        print("QSV unavailable, using libx264 (CPU)...")
        cmd[cmd.index("h264_qsv")] = "libx264"
        cmd[cmd.index("fast")] = "medium"
        result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")

        if result.returncode != 0:
            print("BUILD FAILED:")
            print(result.stderr[-2000:])
            return None

    file_size = os.path.getsize(output_video)
    print(f"DONE! {file_size / 1024 / 1024:.1f} MB -> {output_video}")
    return output_video


def generate_youtube_package(config, video_path):
    """Generate YouTube upload package: thumbnail, title, description, tags."""
    output_dir = os.path.dirname(video_path)
    youtube_dir = os.path.join(output_dir, "YOUTUBE")
    os.makedirs(youtube_dir, exist_ok=True)

    video_name = os.path.splitext(os.path.basename(video_path))[0]
    yt = config.get("youtube", {})

    # Move video to YOUTUBE folder
    yt_video = os.path.join(youtube_dir, os.path.basename(video_path))
    if video_path != yt_video:
        import shutil
        shutil.move(video_path, yt_video)
        print(f"Video moved to: {yt_video}")

    # Extract thumbnail from the thumbnail_time or default to 51s
    thumb_time = yt.get("thumbnail_time", 51)
    thumb_path = os.path.join(youtube_dir, f"THUMBNAIL-{video_name}.png")
    ffprobe = FFMPEG.replace("ffmpeg.exe", "ffprobe.exe")
    thumb_cmd = [
        FFMPEG, "-y",
        "-ss", str(thumb_time),
        "-i", yt_video,
        "-vframes", "1",
        "-s", "1280x720",
        "-update", "1",
        thumb_path,
    ]
    subprocess.run(thumb_cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    print(f"Thumbnail: {thumb_path}")

    # Generate title
    title = yt.get("title", config["slides"][0]["bullets"][0] if config["slides"] else "Untitled")
    title_path = os.path.join(youtube_dir, "YOUTUBE-TITLE.txt")
    with open(title_path, "w", encoding="utf-8") as f:
        f.write(title)
    print(f"Title: {title}")

    # Generate chapters from slides
    chapters = []
    for slide in config["slides"]:
        start = slide["start"]
        mins = int(start // 60)
        secs = int(start % 60)
        timestamp = f"{mins}:{secs:02d}"
        label = slide.get("chapter_label", slide["bullets"][0] if slide["bullets"] and slide["bullets"][0] else "")
        if label:
            chapters.append(f"{timestamp} {label}")

    # Generate description
    desc_lines = []
    if "description" in yt:
        desc_lines.append(yt["description"])
    else:
        desc_lines.append(title)
    desc_lines.append("")
    desc_lines.append("Learn more: https://learnmoretechnologies.com/workforce/")
    desc_lines.append("Schedule a free consult: https://calendly.com/brianmckinney/new-meeting")
    desc_lines.append("")
    desc_lines.append("Brian McKinney | Founder, Learn More Technologies | MBE Certified | Former AARP Insider")
    desc_lines.append("")
    if chapters:
        desc_lines.append("CHAPTERS:")
        desc_lines.extend(chapters)
        desc_lines.append("")
    # Hashtags
    tags = yt.get("hashtags", "#WorkforceDevelopment #Adults50Plus #AgeTech #AITraining #DigitalInclusion #WIOA #FutureOfWork #MBECertified #50PlusTechBridge #LearnMoreTechnologies")
    desc_lines.append(tags)

    desc_path = os.path.join(youtube_dir, "YOUTUBE-DESCRIPTION.txt")
    with open(desc_path, "w", encoding="utf-8") as f:
        f.write("\n".join(desc_lines))
    print(f"Description: {desc_path}")

    # Generate tags
    tag_list = yt.get("tags", "workforce development, AI training, adults 50+, agetech, digital inclusion, WIOA, 50+ TechBridge, Learn More Technologies, age discrimination, experienced workers, AI skills training, workforce training ROI, MBE certified, Brian McKinney, digital skills, older workers, peer instructors, project based learning")
    tags_path = os.path.join(youtube_dir, "YOUTUBE-TAGS.txt")
    with open(tags_path, "w", encoding="utf-8") as f:
        f.write(tag_list)
    print(f"Tags: {tags_path}")

    # Copy article files into FINISHED folder if they exist
    article_dir = os.path.dirname(output_dir) if os.path.basename(output_dir) == "FINISHED" else output_dir
    for ext in [".md", "-SEO.md", "-PLAINTEXT.txt"]:
        for f_name in os.listdir(article_dir):
            if f_name.endswith(ext) and not f_name.startswith("YOUTUBE") and not f_name.startswith("THUMBNAIL"):
                src = os.path.join(article_dir, f_name)
                dst = os.path.join(output_dir, f_name)
                if src != dst and not os.path.exists(dst):
                    import shutil
                    shutil.copy2(src, dst)

    # Generate LinkedIn post
    linkedin_post = generate_linkedin_post(config, yt_video)
    linkedin_path = os.path.join(youtube_dir, "LINKEDIN-POST.txt")
    with open(linkedin_path, "w", encoding="utf-8") as f:
        f.write(linkedin_post)
    print(f"LinkedIn post: {linkedin_path}")

    print(f"\nYouTube package ready at: {youtube_dir}")
    print("")
    print("YOUTUBE UPLOAD:")
    print("  1. Open studio.youtube.com")
    print("  2. Create -> Upload video")
    print("  3. Drag the .mp4 from YOUTUBE folder")
    print("  4. Copy/paste title, description, and tags from the .txt files")
    print("  5. Upload thumbnail PNG")
    print("  6. Set visibility to Public")
    print("")
    print("LINKEDIN CROSS-POST:")
    print("  1. Open linkedin.com -> Start a post")
    print("  2. Copy/paste from LINKEDIN-POST.txt")
    print("  3. YouTube link auto-embeds as video preview")
    print("  4. Post")
    return youtube_dir


def generate_linkedin_post(config, video_path):
    """Generate a LinkedIn post that cross-promotes the YouTube video."""
    yt = config.get("youtube", {})
    linkedin = config.get("linkedin", {})

    # Get YouTube URL from config or placeholder
    yt_url = linkedin.get("youtube_url", "https://youtu.be/YOUR-VIDEO-ID")

    # Build post from config or auto-generate from slides
    if "post" in linkedin:
        post = linkedin["post"]
    else:
        # Auto-generate from slide content
        title = yt.get("title", "")
        lines = []

        # Opening hook from first content slide
        if len(config["slides"]) > 1:
            first_bullets = config["slides"][1].get("bullets", [])
            if first_bullets:
                lines.append(first_bullets[0])
                lines.append("")

        # Key stats from data slides
        for slide in config["slides"]:
            for bullet in slide.get("bullets", []):
                if any(word in bullet.lower() for word in ["million", "trillion", "percent", "billion", "pioneers", "3x", "organizations"]):
                    lines.append(bullet.replace("-  ", ""))

        lines.append("")
        lines.append(f"Watch the full video: {yt_url}")
        lines.append("")
        lines.append("learnmoretechnologies.com/workforce")
        lines.append("")

        hashtags = yt.get("hashtags", "#WorkforceDevelopment #Adults50Plus #AgeTech #AITraining #DigitalInclusion #WIOA #FutureOfWork #MBECertified #50PlusTechBridge #LearnMoreTechnologies")
        lines.append(hashtags)

        post = "\n".join(lines)

    return post


def main():
    if len(sys.argv) < 2:
        print("Usage: python lmt-video-overlay.py <config.json>")
        print("See example-config.json for format.")
        sys.exit(1)

    config_path = sys.argv[1]
    if not os.path.exists(config_path):
        print(f"Config not found: {config_path}")
        sys.exit(1)

    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    if not os.path.exists(config["input_video"]):
        print(f"Input video not found: {config['input_video']}")
        sys.exit(1)

    video_path = build_video(config)
    if video_path:
        generate_youtube_package(config, video_path)


if __name__ == "__main__":
    main()
