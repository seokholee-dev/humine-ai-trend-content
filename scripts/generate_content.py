#!/usr/bin/env python3
"""Prepare a topic workspace and an agent task; this does not call an LLM."""
import argparse
from datetime import date
from pathlib import Path
import re
import shutil
import tempfile

TEMPLATES = {
    "research_template.md": "01_research.md",
    "core_brief_template.md": "02_core_brief.md",
    "column_template.md": "03_column.md",
    "cardnews_template.md": "04_cardnews.md",
    "sources_template.md": "05_sources.md",
    "image_prompts_template.md": "06_image_prompts.md",
    "review_template.md": "07_review.md",
}


def prepare(root, topic, slug, work_date, formats="cardnews", images="plan"):
    root = Path(root).resolve()
    date.fromisoformat(work_date)
    if images not in {"plan", "chat"}:
        raise ValueError("이미지 작업은 plan, chat 중 선택하세요.")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
        raise ValueError("slug는 소문자 영문·숫자·하이픈만 사용하세요.")
    if not topic.strip() or any(c in topic for c in "\r\n"):
        raise ValueError("주제는 한 줄의 비어 있지 않은 문장이어야 합니다.")
    selected = dict(TEMPLATES)
    if formats == "cardnews":
        selected.pop("column_template.md")
    elif formats == "column":
        selected.pop("cardnews_template.md")
    elif formats != "both":
        raise ValueError("형식은 cardnews, column, both 중 선택하세요.")
    for filename in selected:
        if not (root / "templates" / filename).is_file():
            raise ValueError(f"양식이 없습니다: templates/{filename}")
    if not (root / "AGENTS.md").is_file():
        raise ValueError("AGENTS.md가 있는 저장소를 지정하세요.")
    contents = root / "contents"
    if contents.is_symlink():
        raise ValueError("contents는 실제 저장소 폴더여야 합니다.")
    contents.mkdir(exist_ok=True)
    target = contents / f"{work_date}-{slug}"
    if target.exists():
        raise ValueError(f"이미 존재하는 주제 폴더입니다: {target.name}")
    temporary = Path(tempfile.mkdtemp(prefix=".prepare-", dir=contents))
    try:
        for template, output in selected.items():
            text = (root / "templates" / template).read_text(encoding="utf-8")
            for key in ("{{주제}}", "{{주제 또는 후보 조사}}"):
                text = text.replace(key, topic)
            text = text.replace("{{YYYY-MM-DD}}", work_date)
            (temporary / output).write_text(text, encoding="utf-8")
        for folder in ("images",):
            (temporary / folder).mkdir()
            (temporary / folder / "README.md").write_text(
                "# 작업 예정 영역\n\n현재 생성된 결과물은 없습니다. 실제 제작 후 상태를 갱신하세요.\n",
                encoding="utf-8",
            )
        task = f"""# {topic} — 작업 요청

- 작업 시작일: {work_date}
- 산출물 형식: {formats}
- 실행 방식: 현재 대화에서 작성 / 별도 API 호출 없음
- 이미지 작업: {images} (plan: 기획까지, chat: 대화 도구로 실제 생성)
- 상태: 작업 준비 완료 / 원고 미작성

## Codex에 전달할 요청

이 폴더의 주제는 '{topic}'입니다. 루트 AGENTS.md, prompts/README.md,
관련 prompts/ 파일, templates/ 양식과 style/ 가이드를 읽고 요청된 형식의
콘텐츠를 작성하세요. 리서치와 출처를 먼저 확인하고 Core Brief로 정리한 뒤
요청한 원고와 시각 자료 기획을 작성하세요. 두 형식이면 칼럼을 먼저 작성·검수하고
그 칼럼을 카드뉴스로 요약하세요. 카드뉴스만 요청했다면 Core Brief에서 작성하세요.
확인되지 않은 사실은 단정하지 마세요.
모든 자리표시자를 실제 내용 또는 해당 없음으로 정리하세요.
자료의 실제 조사 기준일을 원고 상단에 갱신하세요.

사실·내용 검수를 수행하고 07_review.md에 기록하세요.
줄바꿈·넘침 검수는 사용자 요청에 따라 보류합니다.
prompts/chat_workflow.md를 따라 이미지 작업 범위를 처리하세요.
chat이면 이미지 생성 도구로 생성하고, 접근 가능한 결과 파일을 images/에
저장한 뒤 원고에 실제 경로를 연결하세요. 도구가 없거나 파일을 옮길 수 없으면
해당 단계를 미완료로 기록하고 유료 API로 자동 전환하지 마세요.
plan이면 이미지 기획까지만 수행하세요.
실제로 생성하지 않은 이미지나 외부 게시를 완료했다고 주장하지 마세요.
이 작업 준비 파일은 완성 원고가 아닙니다.

## 카드뉴스 HTML 생성

카드뉴스가 작성된 경우 저장소 루트에서 다음을 실행합니다.

    python3 scripts/build_cardnews.py contents/{target.name}

실제 이미지가 있으면 해당 장의 '이미지 경로' 항목에 images/ 아래 상대 경로를
기록하세요. 이미지가 없으면 기본 배경을 사용하며 이미지 생성 완료로 세지 않습니다.
결과물은 저장소 루트 output/{target.name}/build-실행시각/에 생성됩니다.
다른 출력 루트를 사용하려면 --output-root 경로를 지정하세요.
"""
        (temporary / "00_task.md").write_text(task, encoding="utf-8")
        # The target is never replaced; preexisting user work is preserved.
        if target.exists():
            raise ValueError("작업 중 같은 이름의 폴더가 생성되었습니다.")
        temporary.rename(target)
    except Exception:
        shutil.rmtree(temporary, ignore_errors=True)
        raise
    return target


def main():
    parser = argparse.ArgumentParser(description="새 주제 작업 폴더·양식·Codex 요청 파일 준비")
    parser.add_argument("--topic", required=True)
    parser.add_argument("--slug", required=True, help="회사·제품·이슈를 나타내는 영문 이름 (예: zendesk-specialized-agents)")
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--format", choices=("cardnews", "column", "both"), default="cardnews")
    parser.add_argument("--images", choices=("plan", "chat"), default="plan",
                        help="plan: 이미지 기획까지 / chat: Codex 대화 도구로 이미지 생성 요청")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        path = prepare(args.root, args.topic, args.slug, args.date, args.format, args.images)
    except (ValueError, OSError) as exc:
        parser.exit(1, f"준비 실패: {exc}\n")
    print(f"작업 파일 준비 완료: {path}\n00_task.md의 요청으로 원고 작성을 시작하세요. AI 생성은 실행하지 않았습니다.")


if __name__ == "__main__":
    main()
