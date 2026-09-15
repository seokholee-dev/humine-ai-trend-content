# 단계별 콘텐츠 제작 프롬프트

AGENTS.md의 공통 규칙을 실제 작업 단계로 나눈 실행 지침입니다. 파일을 저장하는 것만으로 자동 실행되지는 않습니다.

## 사용 순서

1. [research.md](research.md): 트렌드 탐색·선정 → 01_research.md, 05_sources.md
2. [core_brief.md](core_brief.md): 공통 기획 요약 → 02_core_brief.md
3. [column_writer.md](column_writer.md): 칼럼 → 03_column.md
4. [cardnews_writer.md](cardnews_writer.md): 장별 카드뉴스 원고 → 04_cardnews.md
5. [visual_planner.md](visual_planner.md): 이미지·레이아웃 계획 → 06_image_prompts.md
6. [fact_check.md](fact_check.md): 검수·수정 → 07_review.md 및 관련 원고 갱신

칼럼과 카드뉴스는 같은 Core Brief에서 갈라지는 형제 산출물입니다. 요청된 형식만 만듭니다. 시각 자료 생성 전에 원고를 검수하고, 실제 이미지나 HTML이 만들어지면 해당 범위를 다시 검수합니다.

## 공통 실행 규칙

- 사용자의 현재 요청과 AGENTS.md를 따릅니다. 각 프롬프트를 사용할 때 입력 파일을 실제로 읽습니다.
- 주제 폴더는 contents/YYYY-MM-DD-topic-slug/입니다. 출력 이름은 단계 간 동일하게 유지합니다.
- templates/가 없으면 각 프롬프트의 출력 항목을 임시 양식으로 사용합니다. 없던 템플릿을 적용했다고 보고하지 않습니다.
- 출처 [S1], [S2]는 주제 폴더 안에서 공유하며 기존 ID를 다른 출처에 재사용하지 않습니다.
- 기본값은 사용자 지정이 없을 때만 적용하고, 원고에 적용한 가정과 상태를 기록합니다.
- 필수 근거가 부족하면 검수 필요로 표시합니다. 요청한 단계에서 멈추되 매 단계 불필요한 승인을 반복 요청하지 않습니다.

## 카드뉴스 레이아웃

사용자가 제공한 참고 이미지의 5가지 유형을 사용합니다.
- cover: 표지·하단 제목
- gradient: 본문·전체 그라데이션
- split: 본문·하단 분할
- overlay: 본문·중앙 오버레이
- cta: 마무리·중앙 패널

5종은 레이아웃 유형이며 카드뉴스 총 장수와는 별개입니다. 이미지보다 제목·본문의 위치와 공통 여백을 우선합니다.
공통 CSS와 위치 기준은 style/cardnews.css, style/humine_visual_guide.md를 확인합니다. 파일이 아직 준비되지 않은 작업 시점에는 미구현으로 표시합니다.

## 요청 예시

> prompts/research.md에 따라 최근 7일의 AI 트렌드 후보 5개를 조사해줘. 기업 실무자 관점에서 비교하고 추천 주제와 출처를 저장해줘.

> 이 주제 폴더의 리서치를 기반으로 prompts/core_brief.md에 따라 Core Brief를 작성해줘.

> Core Brief로 칼럼과 카드뉴스를 작성하고 검수해줘. 카드뉴스는 참고한 5종 레이아웃에서 골라 사용하고, 이미지 제작은 기획까지만 해줘.

## 다음 단계

templates/의 공통 양식과 style/의 브랜드 가이드를 확장한 뒤 실제 주제로 첫 콘텐츠를 만들어 검증합니다. 현재 예시 문구와 디자인 값은 검토용 초안입니다.
