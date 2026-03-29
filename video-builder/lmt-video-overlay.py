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
FFMPEG = "C:/tools/ffmpeg-8.1-essentials_build/bin/ffmpeg.exe"

# Brand constants
BRAND = {
    "gold": "C8942E",
    "orange": "E8733A",
    "green": "109F35",
    "white": "FFFFFF",
    "body_text": "C4CDD9",
    "muted": "A8B8CC",
    "bg_mid": "162640",
    "navy": "0E1C2F",
}

# Font paths (Windows)
FONT_HEADING = "'C\\:/Windows/Fonts/georgiab.ttf'"
FONT_BODY = "'C\\:/Windows/Fonts/arial.ttf'"


def build_drawtext_filters(config):
    """Build FFmpeg drawtext filter chain from config."""
    filters = []
    duration = config.get("duration", 300)
    fmt = config.get("format", "landscape")  # "landscape" (1920x1080) or "short" (1080x1920)

    # Size presets based on format
    if fmt == "training":
        # Training movie — vertical, large header (1/4 screen), Brian PIP bottom-right
        # Header is split into two lines for vertical format
        header_size = 90
        header_split = True  # "LEARN MORE" + "TECHNOLOGIES" on two lines
        header_y = 70
        header_y2 = 170
        sub_size = 52
        sub_y = 290
        line_top_y = 40
        line_bot_y = 360
        lower_size = 32
        lower_bar_h = 50
        lower_text_y_offset = 38
        content_y = 500  # text starts here — same area as slide images
    elif fmt in ("short", "vertical"):
        header_size = 44
        header_split = False
        header_y = 60
        sub_size = 24
        sub_y = 112
        line_top_y = 50
        line_bot_y = 140
        lower_size = 24
        lower_bar_h = 50
        lower_text_y_offset = 38
        content_y = 200
    else:
        header_size = 64
        header_split = False
        header_y = 40
        sub_size = 36
        sub_y = 115
        line_top_y = 30
        line_bot_y = 158
        lower_size = 32
        lower_bar_h = 65
        lower_text_y_offset = 52
        content_y = 250

    # Persistent header (if enabled)
    if config.get("show_header", True):
        # Gold line top
        filters.append(
            f"drawbox=x=iw*0.05:y={line_top_y}:w=iw*0.90:h=4:color=0x{BRAND['gold']}:t=fill:"
            f"enable='between(t,0,{duration})'"
        )
        # Header text — split or single line
        if header_split:
            filters.append(
                f"drawtext=fontfile={FONT_HEADING}:"
                f"text='LEARN MORE':"
                f"fontsize={header_size}:fontcolor=0x{BRAND['gold']}:"
                f"x=(w-text_w)/2:y={header_y}:"
                f"enable='between(t,0,{duration})'"
            )
            filters.append(
                f"drawtext=fontfile={FONT_HEADING}:"
                f"text='TECHNOLOGIES':"
                f"fontsize={header_size}:fontcolor=0x{BRAND['gold']}:"
                f"x=(w-text_w)/2:y={header_y2}:"
                f"enable='between(t,0,{duration})'"
            )
        else:
            filters.append(
                f"drawtext=fontfile={FONT_HEADING}:"
                f"text='LEARN MORE TECHNOLOGIES':"
                f"fontsize={header_size}:fontcolor=0x{BRAND['gold']}:"
                f"x=(w-text_w)/2:y={header_y}:"
                f"enable='between(t,0,{duration})'"
            )
        # Subheading
        filters.append(
            f"drawtext=fontfile={FONT_BODY}:"
            f"text='50+TechBridge':"
            f"fontsize={sub_size}:fontcolor=0x{BRAND['orange']}:"
            f"x=(w-text_w)/2:y={sub_y}:"
            f"enable='between(t,0,{duration})'"
        )
        # Gold line bottom
        filters.append(
            f"drawbox=x=iw*0.05:y={line_bot_y}:w=iw*0.90:h=4:color=0x{BRAND['gold']}:t=fill:"
            f"enable='between(t,0,{duration})'"
        )

    # Persistent lower third (if enabled)
    if config.get("show_lower_third", True):
        filters.append(
            f"drawbox=x=0:y=ih-{lower_bar_h}:w=iw:h={lower_bar_h}:color=0x{BRAND['bg_mid']}@0.9:t=fill:"
            f"enable='between(t,0,{duration})'"
        )
        filters.append(
            f"drawbox=x=0:y=ih-{lower_bar_h + 2}:w=iw:h=3:color=0x{BRAND['gold']}:t=fill:"
            f"enable='between(t,0,{duration})'"
        )
        lower_text = config.get("lower_third_text", "Subscribe   |   Like   |   Share")
        filters.append(
            f"drawtext=fontfile={FONT_BODY}:"
            f"text='{lower_text}':"
            f"fontsize={lower_size}:fontcolor=0x{BRAND['gold']}:"
            f"x=(w-text_w)/2:y=h-{lower_text_y_offset}:"
            f"enable='between(t,0,{duration})'"
        )

    # Timed text overlay slides
    for slide in config["slides"]:
        start = slide["start"]
        end = slide["end"]
        color = slide.get("color", "#FFFFFF").replace("#", "")
        default_font = 52 if fmt == "training" else 46
        font_size = slide.get("font_size", default_font)
        # Center justify: use x=(w-text_w)/2 unless explicit x is set with center=false
        center = slide.get("center", True)
        x = "(w-text_w)/2" if center else slide.get("x", 60 if fmt in ["short", "training"] else 80)
        y = slide.get("y", content_y)
        fade = slide.get("fade", 0.5)
        no_bullet = slide.get("no_bullet", False)

        bullets = slide["bullets"]
        for j, bullet in enumerate(bullets):
            if not bullet:
                continue
            line_y = y + (j * (font_size + 35))

            prefix = "" if no_bullet else "-  "
            safe_text = (prefix + bullet).replace("%", "%%").replace("'", "\u2019").replace(":", "\\:")

            dt = (
                f"drawtext=fontfile={FONT_BODY}:"
                f"text='{safe_text}':"
                f"fontsize={font_size}:fontcolor=0x{color}:"
                f"x={x}:y={line_y}:"
                f"enable='between(t,{start},{end})'"
            )
            if fade > 0:
                dt += (
                    f":"
                    f"alpha='if(lt(t-{start},{fade}),(t-{start})/{fade},if(lt({end}-t,{fade}),({end}-t)/{fade},1))'"
                )
            filters.append(dt)

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
    """Build the video using FFmpeg with Intel QSV (GPU) or libx264 (CPU) fallback.

    Supports optional 'clips' array for B-roll video overlays.
    When clips are present, Galaxy/B-roll videos play full-screen behind Brian
    at specified times (e.g. between text slides). Brian's audio always continues.

    Config clips format:
        "clips": [
            {"file": "path/to/clip.mp4", "start": 5, "end": 12},
            {"file": "path/to/clip2.mp4", "start": 25, "end": 33}
        ]
    """
    input_video = config["input_video"]
    output_video = config["output_video"]

    print(f"Input:  {input_video}")
    print(f"Output: {output_video}")

    # Get actual duration
    duration = get_video_duration(input_video)
    config["duration"] = duration
    print(f"Duration: {duration:.1f}s ({duration/60:.1f} min)")

    # Build drawtext filter chain
    print("Building overlay filters...")
    vf = build_drawtext_filters(config)
    print(f"Filters: {len(config['slides'])} slides")

    clips = config.get("clips", [])

    if clips:
        # --- FILTER_COMPLEX MODE ---
        # Navy background base + Galaxy clips full screen + Brian PIP lower-right + text
        print(f"B-roll clips: {len(clips)}")
        for c in clips:
            print(f"  {os.path.basename(c['file'])} ({c['start']}s - {c['end']}s)")

        # Detect format dimensions
        fmt = config.get("format", "landscape")
        if fmt in ("short", "vertical", "training"):
            out_w, out_h = 1080, 1920
        else:
            out_w, out_h = 1920, 1080

        # Brian PIP size and position (lower-right corner)
        # Brian's source is 9:16 vertical — always maintain that ratio
        pip = config.get("brian_pip", {})
        pip_w = pip.get("width", 250)
        pip_h = int(pip_w * 16 / 9)  # 9:16 portrait ratio
        pip_margin = pip.get("margin", 20)
        pip_x = out_w - pip_w - pip_margin
        pip_y = out_h - pip_h - pip_margin - 55  # above lower third bar
        pip_border = pip.get("border", 3)
        pip_chromakey = pip.get("chromakey", True)  # remove dark bg by default

        print(f"Brian PIP: {pip_w}x{pip_h} at ({pip_x},{pip_y}) chromakey={pip_chromakey}")

        # Use static background image (lesson-bg.png) as base plate
        # This has header + lower third baked in — no need to render them
        bg_image = config.get("bg_image",
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "lesson-bg.png"))

        if not os.path.exists(bg_image):
            print(f"WARNING: bg_image not found: {bg_image}, falling back to color")
            bg_image = None

        # Build input args:
        # [0] = static background image (looped)
        # [1] = brian talking head video (audio + video for PIP)
        # [2..N+1] = galaxy clips
        input_args = []
        if bg_image:
            input_args.extend(["-loop", "1", "-i", bg_image])
        else:
            input_args.extend(["-f", "lavfi", "-i",
                f"color=c=0x{BRAND['navy']}:s={out_w}x{out_h}:d={duration}"])
        input_args.extend(["-i", input_video])
        for clip in clips:
            input_args.extend(["-i", clip["file"]])

        # Build filter_complex chain
        fc_parts = []

        # Brian PIP: scale talking head video to PIP size with gold border
        fc_parts.append(
            f"[1:v]scale={pip_w}:{pip_h},"
            f"pad={pip_w + pip_border*2}:{pip_h + pip_border*2}:{pip_border}:{pip_border}:"
            f"color=0x{BRAND['gold']}[brian_pip]"
        )

        # Scale each Galaxy clip to full screen and delay with tpad
        for i, clip in enumerate(clips):
            input_idx = i + 2  # offset by bg + brian
            start = clip["start"]
            fc_parts.append(
                f"[{input_idx}:v]scale={out_w}:{out_h}:force_original_aspect_ratio=increase,"
                f"crop={out_w}:{out_h},"
                f"tpad=start_duration={start}:start_mode=add:color=black@0"
                f"[clip{i}]"
            )

        # Start with background, overlay Galaxy clips (tpad handles timing)
        prev = "0:v"
        for i, clip in enumerate(clips):
            out_label = f"v{i}"
            fc_parts.append(
                f"[{prev}][clip{i}]overlay=0:0:"
                f"eof_action=pass:format=auto[{out_label}]"
            )
            prev = out_label

        # Brian PIP in lower-right — always visible
        pip_out = "vpip"
        pip_x_adj = pip_x - pip_border
        pip_y_adj = pip_y - pip_border
        fc_parts.append(
            f"[{prev}][brian_pip]overlay={pip_x_adj}:{pip_y_adj}:"
            f"eof_action=pass[{pip_out}]"
        )

        # Apply drawtext filters on top (text slides only, no header/footer)
        fc_parts.append(f"[{pip_out}]{vf}[vout]")

        filter_complex = ";".join(fc_parts)

        cmd = [
            FFMPEG, "-y",
            *input_args,
            "-filter_complex", filter_complex,
            "-map", "[vout]",
            "-map", "1:a",
            "-c:v", "h264_qsv",
            "-preset", "fast",
            "-b:v", "5M",
            "-c:a", "aac",
            "-b:a", "128k",
            "-t", str(duration),
            output_video,
        ]
    else:
        # --- SIMPLE MODE: text overlays only (original behavior) ---
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
        # Replace codec in command
        try:
            idx = cmd.index("h264_qsv")
            cmd[idx] = "libx264"
        except ValueError:
            pass
        try:
            idx = cmd.index("fast")
            if idx > 0 and cmd[idx - 1] == "-preset":
                cmd[idx] = "medium"
        except ValueError:
            pass
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


def auto_resize(source_video, output_dir):
    """Generate all 4 platform formats from one source video.

    From landscape (16:9): creates vertical (9:16) and square (1:1)
    From vertical (9:16): creates landscape (16:9) and square (1:1)
    Always creates thumbnail (1280x720)
    """
    import shutil

    name = os.path.splitext(os.path.basename(source_video))[0]
    resize_dir = os.path.join(output_dir, "ALL-FORMATS")
    os.makedirs(resize_dir, exist_ok=True)

    # Detect source format
    ffprobe = FFMPEG.replace("ffmpeg.exe", "ffprobe.exe")
    cmd = [ffprobe, "-v", "quiet", "-print_format", "json", "-show_streams", source_video]
    result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    width, height = 1920, 1080
    if result.returncode == 0:
        info = json.loads(result.stdout)
        for s in info.get("streams", []):
            if s.get("codec_type") == "video":
                width = int(s.get("width", 1920))
                height = int(s.get("height", 1080))
                break

    is_landscape = width > height
    print(f"\nAuto-resize: {width}x{height} ({'landscape' if is_landscape else 'vertical'})")

    formats = {}

    if is_landscape:
        # Source is landscape — copy as YouTube/LinkedIn
        formats["YOUTUBE-LANDSCAPE-1920x1080"] = None  # already exists
        shutil.copy2(source_video, os.path.join(resize_dir, f"{name}-LANDSCAPE-1920x1080.mp4"))
        print(f"  Copied: LANDSCAPE 1920x1080 (YouTube, LinkedIn, Facebook)")

        # Create vertical (9:16) — crop center
        vert_path = os.path.join(resize_dir, f"{name}-VERTICAL-1080x1920.mp4")
        cmd = [
            FFMPEG, "-y", "-i", source_video,
            "-vf", f"crop=ih*9/16:ih:iw/2-ih*9/32:0,scale=1080:1920",
            "-c:v", "h264_qsv", "-preset", "fast", "-b:v", "5M",
            "-c:a", "aac", "-b:a", "128k", vert_path
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
        if result.returncode != 0:
            cmd[cmd.index("h264_qsv")] = "libx264"
            cmd[cmd.index("fast")] = "medium"
            subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
        print(f"  Created: VERTICAL 1080x1920 (Shorts, Reels, TikTok)")

        # Create square (1:1) — crop center
        sq_path = os.path.join(resize_dir, f"{name}-SQUARE-1080x1080.mp4")
        cmd = [
            FFMPEG, "-y", "-i", source_video,
            "-vf", "crop=ih:ih:iw/2-ih/2:0,scale=1080:1080",
            "-c:v", "h264_qsv", "-preset", "fast", "-b:v", "5M",
            "-c:a", "aac", "-b:a", "128k", sq_path
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
        if result.returncode != 0:
            cmd[cmd.index("h264_qsv")] = "libx264"
            cmd[cmd.index("fast")] = "medium"
            subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
        print(f"  Created: SQUARE 1080x1080 (Instagram Feed, Facebook Feed)")

    else:
        # Source is vertical — copy as Shorts/Reels
        shutil.copy2(source_video, os.path.join(resize_dir, f"{name}-VERTICAL-1080x1920.mp4"))
        print(f"  Copied: VERTICAL 1080x1920 (Shorts, Reels, TikTok)")

        # Create landscape (16:9) — pad with navy background
        land_path = os.path.join(resize_dir, f"{name}-LANDSCAPE-1920x1080.mp4")
        cmd = [
            FFMPEG, "-y", "-i", source_video,
            "-vf", f"scale=-1:1080,pad=1920:1080:(ow-iw)/2:0:color=0x0E1C2F",
            "-c:v", "h264_qsv", "-preset", "fast", "-b:v", "5M",
            "-c:a", "aac", "-b:a", "128k", land_path
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
        if result.returncode != 0:
            cmd[cmd.index("h264_qsv")] = "libx264"
            cmd[cmd.index("fast")] = "medium"
            subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
        print(f"  Created: LANDSCAPE 1920x1080 (YouTube, LinkedIn)")

        # Create square (1:1) — crop center of vertical
        sq_path = os.path.join(resize_dir, f"{name}-SQUARE-1080x1080.mp4")
        cmd = [
            FFMPEG, "-y", "-i", source_video,
            "-vf", "crop=iw:iw:0:ih/2-iw/2,scale=1080:1080",
            "-c:v", "h264_qsv", "-preset", "fast", "-b:v", "5M",
            "-c:a", "aac", "-b:a", "128k", sq_path
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
        if result.returncode != 0:
            cmd[cmd.index("h264_qsv")] = "libx264"
            cmd[cmd.index("fast")] = "medium"
            subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
        print(f"  Created: SQUARE 1080x1080 (Instagram Feed, Facebook Feed)")

    # Thumbnail
    thumb_path = os.path.join(resize_dir, f"{name}-THUMBNAIL-1280x720.png")
    cmd = [
        FFMPEG, "-y", "-ss", "5", "-i", source_video,
        "-vframes", "1", "-s", "1280x720", "-update", "1", thumb_path
    ]
    subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    print(f"  Created: THUMBNAIL 1280x720")

    print(f"\nAll formats saved to: {resize_dir}")
    print("")
    print("PLATFORM GUIDE:")
    print(f"  YouTube Long:     {name}-LANDSCAPE-1920x1080.mp4")
    print(f"  YouTube Short:    {name}-VERTICAL-1080x1920.mp4")
    print(f"  Instagram Reel:   {name}-VERTICAL-1080x1920.mp4 (same file)")
    print(f"  TikTok:           {name}-VERTICAL-1080x1920.mp4 (same file)")
    print(f"  Instagram Feed:   {name}-SQUARE-1080x1080.mp4")
    print(f"  Facebook Feed:    {name}-SQUARE-1080x1080.mp4 (same file)")
    print(f"  LinkedIn Native:  {name}-LANDSCAPE-1920x1080.mp4")
    print(f"  Website Hero:     {name}-LANDSCAPE-1920x1080.mp4")
    print(f"  Thumbnail:        {name}-THUMBNAIL-1280x720.png")

    return resize_dir


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
        yt_dir = generate_youtube_package(config, video_path)
        # Auto-resize to all platform formats
        yt_video = os.path.join(yt_dir, os.path.basename(video_path))
        if os.path.exists(yt_video):
            auto_resize(yt_video, yt_dir)


if __name__ == "__main__":
    main()
