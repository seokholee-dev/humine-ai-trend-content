#!/usr/bin/env python3
"""Render the repository's card-news Markdown into self-contained HTML, optionally PNG."""
import argparse
import base64
import hashlib
from datetime import datetime, timezone
from html import escape
import json
from pathlib import Path
import re
import shutil
import tempfile

LAYOUTS = {"cover", "gradient", "split", "overlay", "cta"}
FIELD = re.compile(r"^\s*-\s*([^:]+):\s*(.*)$")
HEADING = re.compile(r"^##\s+(\d+)\s*[—–-]\s*(.+)$")
MIMES = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp"}


def parse_cards(text):
    cards = []
    current = None
    field = None
    for line in text.splitlines():
        heading = HEADING.match(line)
        if heading:
            current = {"number": int(heading[1]), "role": heading[2].strip()}
            cards.append(current)
            field = None
        elif line.startswith("## "):
            current = None
            field = None
        elif current is not None:
            match = FIELD.match(line)
            if match:
                field = match[1].strip()
                if field in current:
                    raise ValueError(f"{current['number']}장에 중복 항목이 있습니다: {field}")
                current[field] = match[2].strip()
            elif field and line.strip() and not line.lstrip().startswith(">"):
                current[field] += "\n" + line.strip()
    if not cards:
        raise ValueError("'## 01 — 표지' 형식의 장 제목이 없습니다.")
    for expected, card in enumerate(cards, 1):
        if card["number"] != expected:
            raise ValueError("장 번호는 01부터 빠짐없이 이어져야 합니다.")
        if card.get("레이아웃") not in LAYOUTS:
            raise ValueError(f"{expected}장 레이아웃을 명시하세요: {', '.join(sorted(LAYOUTS))}")
        if not card.get("제목", "").strip():
            raise ValueError(f"{expected}장 제목이 비어 있습니다.")
        if any("{{" in str(v) or "}}" in str(v) for v in card.values()):
            raise ValueError(f"{expected}장에 미작성 자리표시자가 있습니다.")
        if card["레이아웃"] in {"gradient", "split", "overlay"} and not card.get("본문"):
            raise ValueError(f"{expected}장 본문이 비어 있습니다.")
    if cards[0]["레이아웃"] != "cover" or cards[-1]["레이아웃"] != "cta":
        raise ValueError("첫 장은 cover, 마지막 장은 cta로 지정하세요.")
    return cards


def safe_text(text):
    # Content is data, not executable HTML. Newlines are the only formatting syntax.
    return escape(text, quote=True).replace("\n", "<br>")


def image_uri(path):
    path = Path(path)
    mime = MIMES.get(path.suffix.lower())
    if not mime or not path.is_file():
        raise ValueError(f"지원하는 이미지 파일이 아닙니다: {path.name}")
    return "data:" + mime + ";base64," + base64.b64encode(path.read_bytes()).decode("ascii")


def background_uri(topic, relative):
    if not relative or relative in {"없음", "해당 없음", "미생성"}:
        return None
    image_root = (topic / "images").resolve()
    path = (topic / relative).resolve()
    try:
        image_root.relative_to(topic.resolve())
        path.relative_to(image_root)
    except ValueError as exc:
        raise ValueError("배경 이미지는 해당 주제의 images/ 아래 파일만 사용하세요.") from exc
    return image_uri(path)


def card_html(card, total, logo, background=None):
    layout = card["레이아웃"]
    title = safe_text(card["제목"])
    body = card.get("본문", "") if layout != "cta" else card.get("보조 문구", "")
    if body in {"없음", "해당 없음"}:
        body = ""
    body_html = f'<p class="card-body">{safe_text(body)}</p>' if body else ""
    notes = [card.get(key, "") for key in ("보조 문구·조건·한계", "사례 구분", "CTA 링크")]
    notes = [n for n in notes if n and n not in {"없음", "해당 없음", "사용 안 함"}]
    body_html += "".join(f'<p class="card-note">{safe_text(n)}</p>' for n in notes)
    media = f'<img src="{background}" alt="">' if background else ""
    logo_html = f'<div class="brand-logo"><img src="{logo}" alt="Data Diving"></div>'
    if layout == "cta":
        copy = f'<section class="cta-panel"><h2 class="card-title">{title}</h2>{body_html}<div class="cta-brand">{logo_html}</div></section>'
        footer = ""
    else:
        kicker = card.get("상단 보조 문구", "")
        kicker_html = f'<p class="card-kicker">{safe_text(kicker)}</p>' if kicker and kicker not in {"없음", "해당 없음"} else ""
        copy = f'<section class="card-copy">{kicker_html}<h2 class="card-title">{title}</h2>{body_html}</section>'
        if layout == "cover":
            footer = f'<footer class="card-footer">{logo_html}</footer>'
        else:
            source = card.get("화면용 짧은 출처", "")
            if source in {"없음", "해당 없음"}:
                source = ""
            footer = f'<footer class="card-footer"><span>{safe_text(source)}</span><span>{card["number"]:02d} / {total:02d}</span></footer>'
    return f'<article class="humine-card card--{layout}"><div class="card-media">{media}</div><div class="card-shade"></div>{copy}{footer}</article>'


def document(title, css, body, gallery=False):
    extra = "body{margin:0;background:#11151d}.card-media{background:linear-gradient(135deg,#697f92,#304359)}.card-note{margin-top:var(--space-3)!important;font-size:var(--label-size);line-height:1.4}"
    if gallery:
        extra += "body{background:#e9edf2;padding:24px;font-family:sans-serif}.page-title{font-size:24px;margin:0 0 20px}.cards{display:flex;flex-direction:column;align-items:center;gap:32px}.frame{width:min(100%,648px);aspect-ratio:4/5;position:relative}.frame .humine-card{position:absolute;transform:scale(.6);transform-origin:top left}.view-controls{margin:0 0 24px;display:flex;gap:12px}.view-controls button{font:inherit;padding:10px 16px;border:1px solid #64748b;border-radius:8px;background:white;color:#17212e;cursor:pointer}.view-controls button[aria-pressed=true]{background:#17212e;color:white}.overview .cards{flex-direction:row;flex-wrap:wrap;justify-content:center}.overview .frame{width:min(100%,324px)}@media(max-width:600px){body{padding:12px}.page-title{font-size:20px}}"
        controls = '<nav class="view-controls" aria-label="카드 보기 방식"><button type="button" data-overview="false" aria-pressed="true">크게 읽기</button><button type="button" data-overview="true" aria-pressed="false">모아 보기</button></nav>'
        script = """<script>
const frames = document.querySelectorAll('.frame');
function fit(frame) { frame.querySelector('.humine-card').style.transform = 'scale(' + frame.clientWidth / 1080 + ')'; }
const observer = new ResizeObserver(entries => entries.forEach(entry => fit(entry.target)));
frames.forEach(frame => { fit(frame); observer.observe(frame); });
document.querySelectorAll('[data-overview]').forEach(button => button.addEventListener('click', () => {
  document.body.classList.toggle('overview', button.dataset.overview === 'true');
  document.querySelectorAll('[data-overview]').forEach(item => item.setAttribute('aria-pressed', String(item === button)));
  frames.forEach(fit);
}));
</script>"""
        body = '<h1 class="page-title">' + escape(title) + '</h1>' + controls + '<div class="cards">' + body + '</div>' + script
    return '<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>' + escape(title) + '</title><style>' + css + '\n' + extra + '</style></head><body>' + body + '</body></html>'


def card_basename(topic_name, number):
    slug = re.sub(r"[^a-z0-9-]+", "-", topic_name.lower()).strip("-") or "cardnews"
    return f"{slug}-card-{number:02d}"


def export_png(directory, count, topic_name):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        raise ValueError("PNG 출력은 scripts/requirements-render.txt 설치와 playwright install chromium이 필요합니다.") from exc
    png_directory = directory / "png"
    png_directory.mkdir()
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        try:
            page = browser.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
            for number in range(1, count + 1):
                page.goto((directory / "html" / (card_basename(topic_name, number) + ".html")).as_uri(), wait_until="load")
                page.evaluate("() => document.fonts.ready")
                page.locator(".humine-card").screenshot(path=str(png_directory / (card_basename(topic_name, number) + ".png")))
        finally:
            browser.close()


def build(topic, root, png=False, output_root=None):
    topic = Path(topic).resolve()
    root = Path(root).resolve()
    source = (topic / "04_cardnews.md").read_text(encoding="utf-8")
    cards = parse_cards(source)
    css = (root / "style/cardnews.css").read_text(encoding="utf-8")
    logo = image_uri(root / "style/assets/datadiving-logo.png")
    # Resolve all assets before writing any output.
    backgrounds = [background_uri(topic, c.get("이미지 경로", "")) for c in cards]
    destination = Path(output_root) if output_root is not None else root / "output"
    if destination.is_symlink():
        raise ValueError("출력 루트에 심볼릭 링크를 사용할 수 없습니다.")
    destination = destination.resolve()
    if destination == topic or topic in destination.parents:
        raise ValueError("출력 루트는 원고 주제 폴더 밖으로 지정하세요.")
    output = destination / topic.name
    if output.is_symlink():
        raise ValueError("주제 출력 폴더에 심볼릭 링크를 사용할 수 없습니다.")
    if output == topic or topic in output.parents:
        raise ValueError("결과 폴더가 원고 주제 폴더와 겹칩니다.")
    output.mkdir(parents=True, exist_ok=True)
    run_name = datetime.now(timezone.utc).strftime("build-%Y%m%dT%H%M%S-%fZ")
    temporary = Path(tempfile.mkdtemp(prefix=".build-", dir=output))
    final = output / run_name
    try:
        (temporary / "html").mkdir()
        (temporary / "assets").mkdir()
        assets = []
        copied = {}
        for card, bg in zip(cards, backgrounds):
            if bg is None:
                continue
            original = (topic / card["이미지 경로"]).resolve()
            if original not in copied:
                stem = re.sub(r"[^a-z0-9-]+", "-", original.stem.lower()).strip("-") or "image"
                filename = f"{card_basename(topic.name, card['number'])}-{stem}{original.suffix.lower()}"
                data = original.read_bytes()
                (temporary / "assets" / filename).write_bytes(data)
                copied[original] = "assets/" + filename
            assets.append({"card": card["number"], "file": copied[original],
                           "source": card["이미지 경로"],
                           "sha256": hashlib.sha256(original.read_bytes()).hexdigest()})
        html_cards = []
        for card, bg in zip(cards, backgrounds):
            markup = card_html(card, len(cards), logo, bg)
            html_cards.append('<div class="frame">' + markup + '</div>')
            (temporary / "html" / (card_basename(topic.name, card["number"]) + ".html")).write_text(document(card["제목"], css, markup), encoding="utf-8")
        (temporary / "index.html").write_text(document(topic.name, css, "".join(html_cards), True), encoding="utf-8")
        if png:
            export_png(temporary, len(cards), topic.name)
        manifest = {
            "topic": topic.name, "source": "04_cardnews.md",
            "source_sha256": hashlib.sha256(source.encode("utf-8")).hexdigest(),
            "source_status": next((line[5:].strip() for line in source.splitlines()
                                   if line.startswith("- 상태:")), "unknown"),
            "build_status": "preview_not_approved", "assets": assets,
            "cards": [{"number": c["number"],
                       "html": "html/" + card_basename(topic.name, c["number"]) + ".html",
                       "png": "png/" + card_basename(topic.name, c["number"]) + ".png" if png else None}
                      for c in cards],
            "card_count": len(cards), "canvas": [1080, 1350],
            "html": "generated", "png": "generated" if png else "not_requested",
            "visual_review": "deferred", "fact_review": "not_performed_by_renderer",
            "generated_background_images": False,
            "missing_backgrounds": [c["number"] for c, b in zip(cards, backgrounds) if b is None],
        }
        (temporary / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
        temporary.rename(final)
    except Exception:
        shutil.rmtree(temporary, ignore_errors=True)
        raise
    return final


def main():
    parser = argparse.ArgumentParser(description="카드뉴스 Markdown → 공통 스타일 HTML 및 선택적 PNG 출력")
    parser.add_argument("topic", type=Path)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--png", action="store_true")
    parser.add_argument("--output-root", type=Path,
                        help="결과물 전용 루트 (기본: 저장소/output). 주제/실행시각으로 분리")
    args = parser.parse_args()
    try:
        result = build(args.topic, args.root, args.png, args.output_root)
    except (ValueError, OSError) as exc:
        parser.exit(1, f"출력 실패: {exc}\n")
    print(f"생성 완료: {result}\n줄바꿈·넘침 및 사실 검수는 이 명령에서 수행하지 않았습니다.")


if __name__ == "__main__":
    main()
