#!/usr/bin/env python3
"""
render.py - turn a day's story spec into 1080x1920 PNGs.

    python3 tools/stories/render.py tools/stories/specs/2026-10-05.json

For each screen it looks for a real photo or print at
assets/stories/<date>/<brand>/<NN>.(jpg|jpeg|png|webp) and uses it as the
background. Screens without one are rendered with type and the brand colour
only; they are listed at the end so nobody mistakes them for finished art.
Never put stock or generic product images in assets/: only the real thing.

Sticker spots are drawn as dashed boxes with the sticker's name, because
stickers are placed in the Instagram app, not baked into the image.

Safe area: nothing in the top 250 px or the bottom 340 px.
"""

import html
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

W, H = 1080, 1920
SAFE_TOP, SAFE_BOTTOM = 250, 340
ROOT = Path(__file__).resolve().parents[2]
CHROME_CANDIDATES = [
    "/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
    "/opt/pw-browsers/chromium/chrome-linux/chrome",
    "chromium", "chromium-browser", "google-chrome",
]
IMAGE_EXTS = ("jpg", "jpeg", "png", "webp")


def find_chrome():
    for c in CHROME_CANDIDATES:
        p = shutil.which(c) or (c if Path(c).exists() else None)
        if p:
            return p
    sys.exit("chromium not found")


def find_background(date, brand, n):
    folder = ROOT / "assets" / "stories" / date / brand
    for ext in IMAGE_EXTS:
        for name in (f"{n:02d}.{ext}", f"{n:02d}.{ext.upper()}"):
            if (folder / name).exists():
                return folder / name
    return None


def esc(text):
    return html.escape(text).replace("\n", "<br>")


def screen_html(brand, screen, bg):
    accent, ink, paper = brand["accent"], brand["ink"], brand["paper"]
    font = brand.get("font", "Liberation Sans")
    blocks = []
    for b in screen["blocks"]:
        kind = b.get("kind", "title")
        if kind == "title":
            blocks.append(f'<div class="title">{esc(b["text"])}</div>')
        elif kind == "kicker":
            blocks.append(f'<div class="kicker">{esc(b["text"])}</div>')
        elif kind == "sub":
            blocks.append(f'<div class="sub">{esc(b["text"])}</div>')
        elif kind == "sign":
            blocks.append(f'<div class="sign">{esc(b["text"])}</div>')
        elif kind == "progress":
            pct = int(b["percent"])
            blocks.append(
                f'<div class="bar"><div class="fill" style="width:{pct}%"></div></div>'
                f'<div class="sub">{esc(b["label"])}</div>')
    stickers = []
    for s in screen.get("stickers", []):
        top = s.get("top", 1180)
        height = s.get("height", 200)
        assert SAFE_TOP <= top and top + height <= H - SAFE_BOTTOM, s
        stickers.append(
            f'<div class="sticker" style="top:{top}px;height:{height}px">'
            f'<span>{esc(s["label"])}</span></div>')
    background = (f"background:{paper} url('file://{bg}') center/cover no-repeat;"
                  if bg else f"background:{paper};")
    shade = ('<div class="shade"></div>' if bg else "")
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{W}px;height:{H}px;overflow:hidden}}
body{{{background}font-family:'{font}',sans-serif;color:{ink};position:relative}}
.shade{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.55),rgba(0,0,0,.35) 45%,rgba(0,0,0,.65))}}
.rule{{position:absolute;left:72px;top:{SAFE_TOP + 70}px;width:120px;height:12px;background:{accent}}}
.handle{{position:absolute;left:72px;top:{SAFE_TOP}px;font-size:48px;font-weight:700;opacity:.55;letter-spacing:.5px}}
.safe{{position:absolute;left:72px;right:72px;top:{SAFE_TOP + 140}px;bottom:{SAFE_BOTTOM + 40}px;
  display:flex;flex-direction:column;justify-content:{screen.get('align', 'center')};gap:36px}}
.kicker{{font-size:64px;font-weight:700;color:{accent};letter-spacing:2px}}
.title{{font-size:{screen.get('size', 112)}px;line-height:1.02;font-weight:700;letter-spacing:-1px;text-transform:uppercase}}
.sub{{font-size:56px;line-height:1.15;font-weight:700;opacity:.85}}
.sign{{font-size:56px;line-height:1.15;font-weight:700;color:{accent}}}
.bar{{width:100%;height:44px;border:4px solid {ink};border-radius:22px;overflow:hidden}}
.fill{{height:100%;background:{accent}}}
.sticker{{position:absolute;left:140px;right:140px;border:6px dashed {accent};border-radius:28px;
  display:flex;align-items:center;justify-content:center;text-align:center;padding:0 24px}}
.sticker span{{font-size:48px;font-weight:700;color:{accent};line-height:1.15}}
</style></head><body>{shade}
<div class="handle">{esc(brand['handle'])}</div><div class="rule"></div>
<div class="safe">{''.join(blocks)}</div>{''.join(stickers)}
</body></html>"""


def main():
    spec_path = Path(sys.argv[1])
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    date = spec["date"]
    chrome = find_chrome()
    typographic = []
    with tempfile.TemporaryDirectory() as tmp:
        for key, brand in spec["brands"].items():
            out_dir = ROOT / "out" / "stories" / date / key
            out_dir.mkdir(parents=True, exist_ok=True)
            for i, screen in enumerate(brand["screens"], 1):
                bg = find_background(date, key, i)
                if not bg:
                    typographic.append(f"{key}/{i:02d}")
                page = Path(tmp) / f"{key}-{i:02d}.html"
                page.write_text(screen_html(brand, screen, bg), encoding="utf-8")
                out = out_dir / f"{i:02d}.png"
                subprocess.run(
                    [chrome, "--headless=new", "--no-sandbox", "--disable-gpu",
                     "--hide-scrollbars", "--force-device-scale-factor=1",
                     f"--window-size={W},{H}", f"--screenshot={out}", page.as_uri()],
                    check=True, capture_output=True)
                print(f"{out.relative_to(ROOT)}  {'foto: ' + str(bg.relative_to(ROOT)) if bg else 'só tipografia'}")
    if typographic:
        print("\nSem imagem (só tipografia e cor):", ", ".join(typographic))


if __name__ == "__main__":
    main()
