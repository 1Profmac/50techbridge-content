"""
LMT Render Timer
=================
Wraps lmt-video-overlay.py and displays a live clock during rendering.
Shows total render time when complete.

Usage:
    python render-timer.py my-config.json
"""

import subprocess
import sys
import time
import os

def format_time(seconds):
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    if h > 0:
        return f"{h}h {m:02d}m {s:02d}s"
    return f"{m}m {s:02d}s"

def main():
    # Force stdout to UTF-8 with error replacement so Windows cp1252 console
    # doesn't crash on Unicode characters (like U+FFFD) from ffmpeg output.
    # Without this, render succeeds but the wrapper crashes on its final print
    # and Claude sees the render as "failed" even though the mp4 is written.
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass  # older Python versions may not have reconfigure

    if len(sys.argv) < 2:
        print("Usage: python render-timer.py <config.json>")
        sys.exit(1)

    config = sys.argv[1]
    script = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lmt-video-overlay.py")
    python = sys.executable

    print("=" * 50)
    print("  LMT RENDER TIMER")
    print("=" * 50)
    print(f"  Config: {config}")
    print(f"  Started: {time.strftime('%I:%M:%S %p')}")
    print("=" * 50)
    print()

    start = time.time()

    proc = subprocess.Popen(
        [python, script, config],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
        bufsize=1
    )

    # Print output in real time while showing elapsed time
    last_clock = 0
    for line in proc.stdout:
        elapsed = time.time() - start
        # Print clock update every line
        print(f"  [{format_time(elapsed)}] {line.rstrip()}")

    proc.wait()
    total = time.time() - start

    print()
    print("=" * 50)
    if proc.returncode == 0:
        print(f"  RENDER COMPLETE")
    else:
        print(f"  RENDER FAILED (exit code {proc.returncode})")
    print(f"  Total time: {format_time(total)}")
    print(f"  Finished: {time.strftime('%I:%M:%S %p')}")
    print("=" * 50)

if __name__ == "__main__":
    main()
