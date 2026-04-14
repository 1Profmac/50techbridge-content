"""
Build 2-minute speaking sizzle reel — Professional Edition
Quick fade-to-black transitions + title cards between clips
"""
import subprocess, os, json

FFMPEG = r"C:\Users\USER\AppData\Local\Microsoft\WinGet\Packages\BtbN.FFmpeg.GPL.8.1_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-n8.1-7-ga3475e2554-win64-gpl-8.1\bin\ffmpeg.exe"
OUT_DIR = r"C:\Users\USER\Desktop\LMT\AGENTIC50-Brand"
TEMP = os.path.join(OUT_DIR, "sizzle-temp")
os.makedirs(TEMP, exist_ok=True)

# Source videos
P1 = r"C:\Users\USER\Desktop\LMT\850-Billion-Series\Part-1\ALL-FORMATS\PART-1-FINISHED-LANDSCAPE-1920x1080.mp4"
P2 = r"C:\Users\USER\Desktop\LMT\850-Billion-Series\Part-2\ALL-FORMATS\PART-2-FINISHED-LANDSCAPE-1920x1080.mp4"
P3 = r"C:\Users\USER\Desktop\LMT\850-Billion-Series\Part-3\ALL-FORMATS\PART-3-FINISHED-LANDSCAPE-1920x1080.mp4"
P4 = r"C:\Users\USER\Desktop\LMT\850-Billion-Series\Part-4\ALL-FORMATS\YOUTUBE\PART-4\PART-4-FINISHED.mp4"

FONT = "C\\\\:/Windows/Fonts/arial.ttf"
FADE_DUR = 0.4  # seconds for fade in/out

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        # Try CPU fallback
        if "h264_nvenc" in cmd:
            cmd[cmd.index("h264_nvenc")] = "libx264"
            r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r

def extract_clip(src, start, end, name):
    """Extract clip with fade in/out"""
    dur = end - start
    out = os.path.join(TEMP, f"{name}.mp4")
    cmd = [
        FFMPEG, "-y", "-ss", str(start), "-to", str(end), "-i", src,
        "-vf", f"fade=in:st=0:d={FADE_DUR},fade=out:st={dur-FADE_DUR}:d={FADE_DUR}",
        "-af", f"afade=in:st=0:d={FADE_DUR},afade=out:st={dur-FADE_DUR}:d={FADE_DUR}",
        "-c:v", "h264_nvenc", "-preset", "fast", "-b:v", "8M",
        "-c:a", "aac", "-b:a", "192k",
        out
    ]
    run(cmd)
    print(f"  {name}: {dur}s (with fades)")
    return out

def make_title_card(text, duration, name):
    """Navy card with gold centered text"""
    out = os.path.join(TEMP, f"{name}.mp4")
    # Escape special characters for drawtext
    safe_text = text.replace("'", "\\'").replace(":", "\\:")
    cmd = [
        FFMPEG, "-y",
        "-f", "lavfi", "-i", f"color=c=0x0E1C2F:s=1920x1080:d={duration}:r=25",
        "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
        "-vf", (
            f"drawtext=text='{safe_text}':fontcolor=0xC8942E:fontsize=56:"
            f"x=(w-text_w)/2:y=(h-text_h)/2:fontfile={FONT},"
            f"fade=in:st=0:d=0.3,fade=out:st={duration-0.3}:d=0.3"
        ),
        "-c:v", "libx264", "-preset", "medium", "-b:v", "4M",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest", "-t", str(duration),
        out
    ]
    run(cmd)
    print(f"  title-{name}: {duration}s")
    return out

# ===========================================
# BUILD THE REEL
# ===========================================
print("Building sizzle reel with transitions...\n")
all_clips = []

# Opening title
all_clips.append(make_title_card("THE $850 BILLION PROBLEM", 2, "title-00"))

# Clip 1: The Hook
all_clips.append(extract_clip(P1, 0, 10, "01-hook"))

# Title card
all_clips.append(make_title_card("THE CAUSE", 2, "title-01"))

# Clip 2: The Cause
all_clips.append(extract_clip(P1, 47, 55, "02-cause"))

# Title card
all_clips.append(make_title_card("THE ORIGIN", 2, "title-02"))

# Clip 3: The Origin
all_clips.append(extract_clip(P1, 101, 115, "03-origin"))

# Title card
all_clips.append(make_title_card("THE DATA", 2, "title-03"))

# Clip 4: The Data
all_clips.append(extract_clip(P2, 87, 100, "04-data"))

# Title card
all_clips.append(make_title_card("THE PROOF", 2, "title-04"))

# Clip 5: The Proof
all_clips.append(extract_clip(P3, 40, 55, "05-proof"))

# Title card
all_clips.append(make_title_card("THE RESULTS", 2, "title-05"))

# Clip 6: The Results
all_clips.append(extract_clip(P4, 180, 200, "06-results"))

# Title card
all_clips.append(make_title_card("THE URGENCY", 2, "title-06"))

# Clip 7: The Urgency
all_clips.append(extract_clip(P4, 212, 232, "07-urgency"))

# Title card
all_clips.append(make_title_card("THE THESIS", 2, "title-07"))

# Clip 8: The Statement
all_clips.append(extract_clip(P1, 242, 252, "08-statement"))

# End card
end_card = os.path.join(TEMP, "09-endcard.mp4")
cmd = [
    FFMPEG, "-y",
    "-f", "lavfi", "-i", "color=c=0x0E1C2F:s=1920x1080:d=8:r=25",
    "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
    "-vf", (
        f"drawtext=text='PROFESSOR BRIAN McKINNEY':fontcolor=0xC8942E:fontsize=60:x=(w-text_w)/2:y=280:fontfile={FONT},"
        f"drawtext=text='CEO & Founder — Learn More Technologies':fontcolor=white:fontsize=36:x=(w-text_w)/2:y=380:fontfile={FONT},"
        f"drawtext=text='MBE Certified · Austin, Texas':fontcolor=white@0.6:fontsize=30:x=(w-text_w)/2:y=440:fontfile={FONT},"
        f"drawtext=text='Book a keynote':fontcolor=white@0.5:fontsize=28:x=(w-text_w)/2:y=520:fontfile={FONT},"
        f"drawtext=text='learnmoretechnologies.com/speak':fontcolor=0xC8942E:fontsize=44:x=(w-text_w)/2:y=570:fontfile={FONT},"
        f"drawtext=text='#AGENTIC50 — The Pioneers Podcast':fontcolor=white@0.4:fontsize=26:x=(w-text_w)/2:y=660:fontfile={FONT},"
        f"fade=in:st=0:d=0.5,fade=out:st=7:d=1"
    ),
    "-c:v", "libx264", "-preset", "medium", "-b:v", "4M",
    "-c:a", "aac", "-b:a", "192k",
    "-shortest", "-t", "8",
    end_card
]
run(cmd)
all_clips.append(end_card)
print("  end-card: 8s")

# Concatenate
print("\nConcatenating all clips...")
concat_file = os.path.join(TEMP, "concat.txt")
with open(concat_file, "w") as f:
    for cf in all_clips:
        f.write(f"file '{cf}'\n")

output = os.path.join(OUT_DIR, "sizzle-reel-LANDSCAPE-1920x1080.mp4")
cmd = [
    FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", concat_file,
    "-c:v", "libx264", "-preset", "medium", "-b:v", "8M",
    "-c:a", "aac", "-b:a", "192k",
    output
]
r = run(cmd)
if r.returncode == 0:
    probe = subprocess.run(
        [FFMPEG.replace("ffmpeg.exe", "ffprobe.exe"), "-v", "quiet", "-print_format", "json", "-show_format", output],
        capture_output=True, text=True, encoding="utf-8", errors="replace"
    )
    d = json.loads(probe.stdout)
    dur = float(d.get("format", {}).get("duration", 0))
    sz = os.path.getsize(output) / 1024 / 1024
    print(f"\nDONE! Sizzle reel: {output}")
    print(f"Duration: {dur:.0f}s ({dur/60:.1f} min)")
    print(f"Size: {sz:.1f} MB")
else:
    print("ERROR:", r.stderr[-500:])
