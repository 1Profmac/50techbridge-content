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

    build_video(config)


if __name__ == "__main__":
    main()
