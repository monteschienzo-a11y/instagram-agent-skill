#!/usr/bin/env python3
"""
render_reel.py - turn a reel's on-screen card spec into a 1080x1920 MP4.

    python3 tools/reels/render_reel.py tools/reels/specs/sallloja-roblox.json

Each card is drawn with Chromium and held for its duration; ffmpeg joins
them into H.264/yuv420p at 30 fps with no audio track (music is added in
the Instagram app). Text stays inside the Reel safe zone: y 230-1440 on a
1080x1920 frame, with the right 230 px clear for the action rail.

If real footage exists at assets/reels/<name>/<NN>.(mp4|mov|jpg|png) it is
not used yet: the output is the text layer on the brand colour, and the
script says so. Never substitute stock or generic footage.

Needs: Chromium (see tools/stories/render.py) and an ffmpeg with libx264
(pip install imageio-ffmpeg provides one).
"""

import html
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "stories"))
from render import find_chrome  # noqa: E402

W, H = 1080, 1920
SAFE_TOP, SAFE_BOTTOM_Y, SAFE_RIGHT = 230, 1440, 230
FPS = 30


def find_ffmpeg():
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        exe = shutil.which("ffmpeg")
        if not exe:
            sys.exit("ffmpeg with libx264 not found: pip install imageio-ffmpeg")
        return exe


def card_html(spec, card):
    lines = "".join(
        f'<div class="{cls}">{html.escape(text)}</div>'
        for cls, text in (("title", card["text"]), ("sub", card.get("sub", "")))
        if text)
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{W}px;height:{H}px;overflow:hidden}}
body{{background:{spec['paper']};color:{spec['ink']};font-family:'{spec.get('font', 'Liberation Sans')}',sans-serif;position:relative}}
.box{{position:absolute;left:72px;right:{SAFE_RIGHT}px;top:{SAFE_TOP + 120}px;bottom:{H - SAFE_BOTTOM_Y + 60}px;
  display:flex;flex-direction:column;justify-content:center;gap:32px}}
.rule{{width:120px;height:12px;background:{spec['accent']}}}
.title{{font-size:{card.get('size', 104)}px;line-height:1.02;font-weight:700;text-transform:uppercase;letter-spacing:-1px}}
.sub{{font-size:56px;font-weight:700;color:{spec['accent']}}}
</style></head><body><div class="box"><div class="rule"></div>{lines}</div></body></html>"""


def main():
    spec_path = Path(sys.argv[1])
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    chrome, ffmpeg = find_chrome(), find_ffmpeg()
    out = ROOT / "out" / "reels" / f"{spec['name']}.mp4"
    out.parent.mkdir(parents=True, exist_ok=True)
    footage = ROOT / "assets" / "reels" / spec["name"]
    if footage.exists() and any(footage.iterdir()):
        print(f"aviso: há material em {footage.relative_to(ROOT)}, mas este script "
              "só gera a camada de texto; a composição com o vídeo real é feita na edição.")
    with tempfile.TemporaryDirectory() as tmp:
        concat = []
        for i, card in enumerate(spec["cards"], 1):
            page = Path(tmp) / f"{i:02d}.html"
            png = Path(tmp) / f"{i:02d}.png"
            page.write_text(card_html(spec, card), encoding="utf-8")
            subprocess.run([chrome, "--headless=new", "--no-sandbox", "--disable-gpu",
                            "--hide-scrollbars", "--force-device-scale-factor=1",
                            f"--window-size={W},{H}", f"--screenshot={png}", page.as_uri()],
                           check=True, capture_output=True)
            dur = card["end"] - card["start"]
            concat.append(f"file '{png}'\nduration {dur}")
        concat.append(f"file '{png}'")          # concat demuxer needs the last frame repeated
        listfile = Path(tmp) / "list.txt"
        listfile.write_text("\n".join(concat), encoding="utf-8")
        subprocess.run([ffmpeg, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
                        "-i", str(listfile), "-vf", f"fps={FPS},format=yuv420p",
                        "-c:v", "libx264", "-crf", "18", "-preset", "medium",
                        "-movflags", "+faststart", "-t", str(spec["cards"][-1]["end"]), str(out)],
                       check=True)
    print(out.relative_to(ROOT))


if __name__ == "__main__":
    main()
