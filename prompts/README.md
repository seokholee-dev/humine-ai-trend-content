# 단계별 콘텐츠 제작 프롬프트

AGENTS.md의 공통 규칙을 실제 작업 단계로 나눈 실행 지침입니다. 파일을 저장하는 것만으로 자동 실행되지는 않습니다.

## 사용 순서

API 키 없이 현재 대화에서 원고부터 이미지까지 진행하려면 [chat_workflow.md](chat_workflow.md)를 사용합니다. 이미지 생성까지 요청한 경우 도구로 실제 생성하고 저장·합성 상태를 구분합니다.

1. [research.md](research.md): 트렌드 탐색·선정 → 01_research.md, 05_sources.md
2. [core_brief.md](core_brief.md): 공통 기획 요약 → 02_core_brief.md
3. [column_writer.md](column_writer.md): 칼럼 → 03_column.md
4. [cardnews_writer.md](cardnews_writer.md): 장별 카드뉴스 원고 → 04_cardnews.md
5. [visual_planner.md](visual_planner.md): 이미지·레이아웃 계획 → 06_image_prompts.md
6. [fact_check.md](fact_check.md): 검수·수정 → 07_review.md 및 관련 원고 갱신

칼럼과 카드뉴스는 같은 Core Brief에서 갈라지는 형제 산출물입니다. 요청된 형식만 만듭니다. 시각 자료 생성 전에 원고를 검수하고, 실제 이미지나 HTML이 만들어지면 해당 범위를 다시 검수합니다.

## 공통 기준

출처·검수·비용·기존 작업 보존 규칙은 루트 AGENTS.md를 따른다. 양식은 templates/, 시각 기준은 style/를 참조한다. 카드 기본 장수와 구성은 cardnews_writer.md에서 관리한다. 제작 상태는 주제별 07_review.md에서 확인한다.
