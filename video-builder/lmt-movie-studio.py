"""
LMT Training Movie Builder — Mobile Vertical Format
=====================================================
Badge header + alternating image/text + Brian PIP bottom-right.
Output: 1080x1920 vertical (mobile-first)

Usage:
    python lmt-training-movie.py lesson-1-config.json
"""

import json
import sys
import os
import subprocess

FFMPEG = "C:/tools/ffmpeg-8.1-essentials_build/bin/ffmpeg.exe"

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

FONT_HEADING = "'C\\:/Windows/Fonts/georgiab.ttf'"
FONT_BODY = "'C\\:/Windows/Fonts/arial.ttf'"


def get_audio_duration(audio_path):
    ffprobe = FFMPEG.replace("ffmpeg.exe", "ffprobe.exe")
    cmd = [ffprobe, "-v", "quiet", "-print_format", "json", "-show_format", audio_path]
    result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if result.returncode == 0:
        info = json.loads(result.stdout)
        return float(info["format"]["duration"])
    return 10


def build_scene_video(scene, scene_index, brian_image, temp_dir):
    """Build a single scene: badge top + image first half / text second half + Brian PIP."""
    slide_file = scene.get("image", scene.get("clip", ""))
    is_video_clip = slide_file.lower().endswith(".mp4")
    audio = scene["audio"]
    text_lines = scene.get("text", [])
    text_color = scene.get("text_color", "#FFFFFF").replace("#", "")
    no_bullet = scene.get("no_bullet", False)
    font_size = scene.get("font_size", 56)

    duration = get_audio_duration(audio) + 1.5
    half = duration / 2
    output = os.path.join(temp_dir, f"scene-{scene_index:02d}.mp4")

    print(f"  Scene {scene_index + 1}: {os.path.basename(slide_file)} ({'video' if is_video_clip else 'image'}) + {os.path.basename(audio)} ({duration:.1f}s)")

    # Filter complex inputs:
    # [0] = navy background 1080x1920
    # [1] = brian talking head
    # [2] = slide image
    # [3] = badge image
    # [4] = audio

    fc = []

    # Navy background
    fc.append(f"color=c=0x{BRAND['navy']}:s=1080x1920:d={duration}[bg]")

    # Brian — bottom 1/3 of screen (large, not PIP)
    # Brian image is 1920x1080 — scale down, crop to center chest-up
    fc.append(f"[1:v]scale=1920:-1,crop=1920:640:0:100,scale=1080:360[brian]")

    # Slide/clip — top 2/3 content area, first half only
    fc.append(f"[2:v]scale=1000:800:force_original_aspect_ratio=decrease,pad=1000:800:(ow-iw)/2:(oh-ih)/2:color=0x{BRAND['navy']}[slide]")

    # Compose: slide in center (first half), Brian at bottom (full duration)
    fc.append(f"[bg][slide]overlay=40:400:enable='lt(t,{half})'[withslide]")
    fc.append(f"[withslide][brian]overlay=0:1500[composed]")

    # Text overlays (second half only)
    text_filters = []

    # Header — text based, large, top of screen
    text_filters.append(
        f"drawbox=x=iw*0.05:y=30:w=iw*0.90:h=4:color=0x{BRAND['gold']}:t=fill"
    )
    text_filters.append(
        f"drawtext=fontfile={FONT_HEADING}:"
        f"text='LEARN MORE':"
        f"fontsize=90:fontcolor=0x{BRAND['gold']}:"
        f"x=(w-text_w)/2:y=50"
    )
    text_filters.append(
        f"drawtext=fontfile={FONT_HEADING}:"
        f"text='TECHNOLOGIES':"
        f"fontsize=90:fontcolor=0x{BRAND['gold']}:"
        f"x=(w-text_w)/2:y=150"
    )
    text_filters.append(
        f"drawtext=fontfile={FONT_BODY}:"
        f"text='50+TechBridge':"
        f"fontsize=52:fontcolor=0x{BRAND['orange']}:"
        f"x=(w-text_w)/2:y=260"
    )
    text_filters.append(
        f"drawbox=x=iw*0.05:y=330:w=iw*0.90:h=4:color=0x{BRAND['gold']}:t=fill"
    )

    # Lower third
    text_filters.append(
        f"drawbox=x=0:y=ih-55:w=iw:h=55:color=0x{BRAND['bg_mid']}@0.9:t=fill"
    )
    text_filters.append(
        f"drawbox=x=0:y=ih-57:w=iw:h=3:color=0x{BRAND['gold']}:t=fill"
    )
    text_filters.append(
        f"drawtext=fontfile={FONT_BODY}:"
        f"text='Subscribe   |   Like   |   Share':"
        f"fontsize=28:fontcolor=0x{BRAND['gold']}:"
        f"x=(w-text_w)/2:y=h-42"
    )

    # Text bullet points — center of screen, second half only
    y_start = 450
    for j, line in enumerate(text_lines):
        if not line:
            continue
        line_y = y_start + (j * (font_size + 40))
        prefix = "" if no_bullet else "-  "
        safe_text = (prefix + line).replace("%", "%%").replace("'", "\u2019").replace(":", "\\:")
        text_start = half + 0.3 + (j * 0.5)
        text_filters.append(
            f"drawtext=fontfile={FONT_BODY}:"
            f"text='{safe_text}':"
            f"fontsize={font_size}:fontcolor=0x{text_color}:"
            f"x=60:y={line_y}:"
            f"alpha='if(lt(t,{text_start}),0,if(lt(t,{text_start + 0.5}),(t-{text_start})/0.5,1))'"
        )

    vf_text = ",".join(text_filters)
    full_fc = ";".join(fc) + f";[composed]{vf_text}[out]"

    # Build input args — loop images, direct input for video clips
    slide_input = ["-i", slide_file] if is_video_clip else ["-loop", "1", "-i", slide_file]

    cmd = [
        FFMPEG, "-y",
        "-f", "lavfi", "-i", f"color=c=0x{BRAND['navy']}:s=1080x1920:d={duration}",
        "-loop", "1", "-i", brian_image,
        *slide_input,
        "-i", audio,
        "-filter_complex", full_fc,
        "-map", "[out]",
        "-map", "3:a",
        "-c:v", "h264_qsv",
        "-preset", "fast",
        "-b:v", "5M",
        "-c:a", "aac",
        "-b:a", "128k",
        "-t", str(duration),
        "-shortest",
        output,
    ]

    result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")

    if result.returncode != 0:
        for i, c in enumerate(cmd):
            if c == "h264_qsv":
                cmd[i] = "libx264"
            if c == "fast" and i > 0 and cmd[i-1] == "-preset":
                cmd[i] = "medium"
        result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
        if result.returncode != 0:
            print(f"    ERROR: {result.stderr[-800:]}")
            return None

    return output


def build_training_movie(config):
    output_video = config["output_video"]
    scenes = config["scenes"]
    brian_image = config["brian_image"]
    temp_dir = os.path.join(os.path.dirname(output_video), "temp_scenes")
    os.makedirs(temp_dir, exist_ok=True)

    print(f"Building {len(scenes)} scenes (1080x1920 vertical)...")

    scene_files = []
    for i, scene in enumerate(scenes):
        sf = build_scene_video(scene, i, brian_image, temp_dir)
        if sf:
            scene_files.append(sf)

    if not scene_files:
        print("ERROR: No scenes built")
        return None

    concat_file = os.path.join(temp_dir, "concat.txt")
    with open(concat_file, "w") as f:
        for sf in scene_files:
            f.write(f"file '{sf.replace(os.sep, '/')}'\n")

    print(f"Stitching {len(scene_files)} scenes...")
    cmd = [
        FFMPEG, "-y",
        "-f", "concat", "-safe", "0",
        "-i", concat_file,
        "-c:v", "h264_qsv", "-preset", "fast", "-b:v", "5M",
        "-c:a", "aac", "-b:a", "128k",
        output_video,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if result.returncode != 0:
        for i, c in enumerate(cmd):
            if c == "h264_qsv":
                cmd[i] = "libx264"
            if c == "fast" and i > 0 and cmd[i-1] == "-preset":
                cmd[i] = "medium"
        result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
        if result.returncode != 0:
            print(f"STITCH ERROR: {result.stderr[-500:]}")
            return None

    for sf in scene_files:
        os.remove(sf)
    os.remove(concat_file)
    os.rmdir(temp_dir)

    file_size = os.path.getsize(output_video)
    print(f"DONE! {file_size / 1024 / 1024:.1f} MB -> {output_video}")
    return output_video


def main():
    if len(sys.argv) < 2:
        print("Usage: python lmt-training-movie.py <config.json>")
        sys.exit(1)
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        config = json.load(f)
    build_training_movie(config)


if __name__ == "__main__":
    main()
