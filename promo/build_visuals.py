#!/usr/bin/env python3
"""Build social preview images and evidence cards without third-party Python packages.

The make-project-promo renderer needs Pillow + fontTools, which are unavailable in
this environment. This script keeps the same brief contract, output names and card
dimensions, but renders the pixels with the locally installed headless Chrome.
"""
from __future__ import annotations

import base64
import hashlib
import html
import json
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMO = ROOT / "promo"
OUT = PROMO / "out"
TMP = PROMO / ".render"
CHROME = Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
SHOT = ROOT / "assets" / "demo-screenshot.png"
FONT = '"Noto Sans SC", "Microsoft YaHei", "Segoe UI", Arial, sans-serif'


def render(name: str, css: str, body: str, width: int, height: int, target: Path) -> None:
    TMP.mkdir(parents=True, exist_ok=True)
    page = TMP / f"{name}.html"
    page.write_text(
        '<!doctype html><meta charset="utf-8"><style>'
        + css
        + "</style>"
        + body,
        encoding="utf-8",
    )
    cmd = [
        str(CHROME),
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--force-device-scale-factor=1",
        "--virtual-time-budget=2500",
        f"--window-size={width},{height}",
        f"--screenshot={target.resolve()}",
        page.as_uri(),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
    if result.returncode != 0 or not target.exists():
        raise RuntimeError(f"Chrome render failed for {name}: {result.stderr[-1000:]}")


def png_size(path: Path) -> tuple[int, int]:
    raw = path.read_bytes()[:24]
    if raw[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"Not a PNG: {path}")
    return int.from_bytes(raw[16:20], "big"), int.from_bytes(raw[20:24], "big")


def social_css(width: int, left_w: int, font_title: int) -> str:
    return f"""
*{{box-sizing:border-box}}
html,body{{margin:0;width:{width}px;height:640px;overflow:hidden}}
body{{background:radial-gradient(circle at 78% 18%,rgba(46,138,117,.42),transparent 46%),
linear-gradient(135deg,#061619 0%,#0b2a2c 58%,#071d20 100%);
color:#eef8f3;font-family:{FONT}}}
.wrap{{height:100%;display:flex;gap:34px;padding:52px 54px;align-items:stretch}}
.left{{width:{left_w}px;display:flex;flex-direction:column;justify-content:center}}
.kicker{{font-size:19px;letter-spacing:5px;color:#79d4ae;font-weight:700}}
h1{{font-size:{font_title}px;line-height:1.02;letter-spacing:-2px;margin:20px 0 18px}}
h1 em{{font-style:normal;color:#79d4ae}}
.sub{{font-size:23px;line-height:1.5;color:#c0d8d2;max-width:{left_w - 10}px}}
.pills{{display:flex;flex-wrap:wrap;gap:10px;margin-top:26px}}
.pill{{border:1px solid rgba(121,212,174,.45);border-radius:999px;padding:8px 15px;font-size:17px;color:#d9f1e7}}
.url{{margin-top:30px;font-size:18px;color:#8fe0bc;word-break:break-all}}
.shot{{flex:1;position:relative;border-radius:22px;overflow:hidden;
border:1px solid rgba(150,220,200,.28);background:#0d2225;
box-shadow:0 26px 70px rgba(0,0,0,.45)}}
.shot img{{width:100%;height:100%;object-fit:cover;object-position:100% 30%}}
.badge{{position:absolute;top:18px;left:18px;background:rgba(6,24,26,.88);
border:1px solid rgba(121,212,174,.5);border-radius:999px;padding:8px 14px;
font-size:15px;letter-spacing:2px;color:#9ee4c3}}
.footer{{position:absolute;bottom:0;left:0;right:0;padding:16px 22px;
background:linear-gradient(transparent,rgba(4,18,20,.94));font-size:16px;color:#d6ebe4}}
"""


def social_body(embed: str, og: bool = False) -> str:
    sub = (
        "An eco-friendly Pomodoro timer where focus grows a living pond. "
        "Single HTML file, offline, local-first."
    )
    title = "Eco-Pomodoro" if og else "Eco-Pomodoro"
    return f"""
<div class="wrap">
  <div class="left">
    <div class="kicker">FOCUS THAT GROWS</div>
    <h1>{title}<br><em>Eco Pond</em></h1>
    <div class="sub">{html.escape(sub)}</div>
    <div class="pills">
      <span class="pill">Single file</span><span class="pill">Offline</span>
      <span class="pill">Local-first</span><span class="pill">MIT</span>
    </div>
    <div class="url">timyin7.github.io/Eco-Pomodoro/</div>
  </div>
  <div class="shot">
    <img src="{embed}">
    <div class="footer">25:00 focus &middot; pond vitals &middot; species guide</div>
  </div>
</div>
"""


def card_css() -> str:
    return """
*{box-sizing:border-box}
html,body{margin:0;width:1080px;height:1440px;overflow:hidden}
body{background:#f6f4ee;color:#172e32;font-family:"Noto Sans SC","Microsoft YaHei","Segoe UI",Arial,sans-serif;
border-left:20px solid #156d64;padding:64px 72px}
small{display:block;font-size:32px;color:#156d64;font-weight:700}
h1{font-size:72px;line-height:1.25;margin:72px 0 0;max-width:936px;overflow-wrap:anywhere}
p{font-size:42px;line-height:1.5;color:#34474a;margin:38px 0 0;max-width:936px;white-space:pre-wrap;overflow-wrap:anywhere}
img{position:absolute;left:92px;top:820px;width:936px;height:480px;object-fit:contain;
border:1px solid rgba(21,109,100,.25);border-radius:12px;background:#0b2024}
footer{position:absolute;left:92px;bottom:50px;font-size:28px;color:#156d64}
"""


def card_body(project: str, title: str, body: str, image: str | None, index: int, total: int) -> str:
    img = f'<img src="{image}">' if image else ""
    return (
        f"<small>{html.escape(project)}</small>"
        f"<h1>{html.escape(title)}</h1>"
        f"<p>{html.escape(body)}</p>"
        f"{img}"
        f"<footer>{index:02d} / {total:02d}</footer>"
    )


def main() -> None:
    if OUT.exists() and any(OUT.iterdir()):
        raise ValueError("Output directory is not empty; refuse to overwrite a previous delivery")
    if not SHOT.exists():
        raise FileNotFoundError(SHOT)
    brief_path = PROMO / "brief.json"
    brief = json.loads(brief_path.read_text(encoding="utf-8"))

    embed = "data:image/png;base64," + base64.b64encode(SHOT.read_bytes()).decode()
    render("github-social", social_css(1280, 510, 64), social_body(embed), 1280, 640, ROOT / "assets" / "github-social.png")
    render("og-image", social_css(1200, 470, 60), social_body(embed, og=True), 1200, 630, ROOT / "assets" / "og-image.png")

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "assets").mkdir()
    for i, card in enumerate(brief["cards"], 1):
        image_for_card = None
        if card.get("image"):
            image_path = (PROMO / card["image"]).resolve()
            raw = base64.b64encode(image_path.read_bytes()).decode()
            image_for_card = "data:image/png;base64," + raw
            shutil.copyfile(image_path, OUT / "assets" / f"{i:02d}.png")
        render(
            f"card-{i:02d}",
            card_css(),
            card_body(brief["project"], card["title"], card["body"], image_for_card, i, len(brief["cards"])),
            1080,
            1440,
            OUT / f"{i:02d}.png",
        )

    delivered_brief = json.loads(json.dumps(brief))
    for card in delivered_brief["cards"]:
        if card.get("image"):
            card["image"] = "assets/03.png"
    (OUT / "brief.json").write_text(
        json.dumps(delivered_brief, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (OUT / "post.md").write_text(
        "\n".join(f"- {t}" for t in brief["titles"]) + "\n\n" + brief["post"] + "\n",
        encoding="utf-8",
    )

    esc = html.escape
    sections = []
    for i, card in enumerate(brief["cards"], 1):
        img_tag = (
            f'<img src="data:image/png;base64,{base64.b64encode((PROMO / card["image"]).read_bytes()).decode()}">'
            if card.get("image")
            else ""
        )
        sections.append(
            "<section><small>"
            + esc(brief["project"])
            + "</small><h1>"
            + esc(card["title"])
            + "</h1><p>"
            + esc(card["body"])
            + "</p>"
            + img_tag
            + f"<footer>{i:02d} / {len(brief['cards']):02d}</footer></section>"
        )
    css = card_css().replace("html,body{", "section{").replace("body{", "section{")
    css += " main{contenteditable:true} section{position:relative;margin:0 0 40px;min-height:1440px}"
    (OUT / "cards.html").write_text(
        '<!doctype html><meta charset="utf-8"><title>Eco-Pomodoro cards</title><style>'
        + css
        + "</style><main>"
        + "".join(sections)
        + "</main>",
        encoding="utf-8",
    )

    sizes = {
        "github-social.png": png_size(ROOT / "assets" / "github-social.png"),
        "og-image.png": png_size(ROOT / "assets" / "og-image.png"),
        **{f"{i:02d}.png": png_size(OUT / f"{i:02d}.png") for i in range(1, len(brief["cards"]) + 1)},
    }
    expected = {"github-social.png": (1280, 640), "og-image.png": (1200, 630)}
    expected.update({f"{i:02d}.png": (1080, 1440) for i in range(1, 6)})
    if sizes != expected:
        raise ValueError(f"Unexpected image dimensions: {sizes}")

    manifest = {
        "schema": 1,
        "renderer": "make-project-promo/1.0.0 (Chrome fallback; Pillow/fontTools unavailable)",
        "brief_sha256": hashlib.sha256(brief_path.read_bytes()).hexdigest(),
        "cards": len(brief["cards"]),
        "dimensions": [1080, 1440],
        "claims": brief["claims"],
        "files": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in OUT.iterdir() if p.is_file()},
    }
    (OUT / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps({"status": "ok", "cards": len(brief["cards"]), "sizes": sizes, "out": str(OUT)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
