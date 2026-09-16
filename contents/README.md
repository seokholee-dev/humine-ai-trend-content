# 주제별 콘텐츠 보관

이 폴더에는 실제로 조사·작성한 콘텐츠를 주제별로 저장합니다. 현재 발행 콘텐츠는 없습니다.

## 주제 폴더

폴더명: YYYY-MM-DD-topic-slug. 날짜는 작업 시작일이며 조사 대상 기간은 본문에 따로 씁니다.
topic-slug는 `zendesk-specialized-agents`처럼 회사·제품·이슈를 담습니다. 여러 기업을 다루면 공통 이슈로 이름을 정합니다. 이미지 원본은 `zendesk-specialized-agents-02-concept-v2.png`처럼 내용을 드러내고, 도구가 읽는 `04_cardnews.md` 등의 원고 이름은 유지합니다. 기존 폴더·파일은 자동으로 바꾸지 않습니다.

후보만 조사할 때는 YYYY-MM-DD-topic-candidates를 사용하고 미선정으로 기록합니다.

~~~text
contents/
├── README.md
└── YYYY-MM-DD-topic-slug/       # 주제 작업을 시작할 때 생성
    ├── 01_research.md
    ├── 02_core_brief.md
    ├── 03_column.md
    ├── 04_cardnews.md
    ├── 05_sources.md
    ├── 06_image_prompts.md
    ├── 07_review.md
    └── images/                 # 실제 생성·확보한 이미지 원본
~~~

위 폴더는 구조 예시입니다. 실제 제작물은 [첫 주제 검수 기록](2026-09-16-agent-work-delegation/07_review.md)에서 확인할 수 있습니다.

## 새 콘텐츠 시작

1. 루트 AGENTS.md, prompts/README.md, style/humine_content_guide.md를 읽습니다.
2. 주제를 지정하거나 research 프롬프트로 후보를 조사합니다.
3. 주제 폴더를 만들고 ../templates/의 필요한 양식을 복사해 위 이름으로 저장합니다.
4. 리서치·출처 → Core Brief → 요청한 칼럼·카드뉴스 → 시각 자료 기획 순으로 작성합니다.
5. 카드뉴스는 cover / gradient / split / overlay / cta 중 적절한 틀을 사용합니다. 공통 CSS의 위치·여백을 유지합니다.
6. 실제 검수를 수행할 때 07_review.md를 작성합니다. 줄바꿈·넘침 검수는 현재 사용자 요청에 따라 보류합니다.
7. 이미지가 실제로 생성되었을 때 images/에, 합성 결과는 저장소 최상위 output/주제명/build-실행시각/에 저장합니다. 기획 Markdown은 결과물에 복사하지 않습니다.

## 관리 원칙

- 필요한 파일만 생성합니다. 미작성 양식·빈 폴더를 완성 콘텐츠로 세지 않습니다.
- 작성일, 조사 기준일, 상태를 원고 상단에 기록합니다.
- 동일한 주제는 출처 ID와 Core Brief를 공유합니다. 수정 시 관련 원고를 함께 동기화합니다.
- 원고 검수 완료, 이미지 생성 완료, 최종 출력 완료, 게시 완료를 구분합니다.
- 줄바꿈·넘침은 후속 작업으로 기록하며 통과로 표시하지 않습니다.
- 기존 주제와 사용자의 수정 내용을 보존합니다.

## 첫 실행 요청 예시

> 최근 7일 AI 트렌드를 조사하고 추천 주제로 Core Brief와 카드뉴스 원고를 만들어줘. prompts/와 templates/를 사용하고, 줄바꿈·넘침 검수와 이미지 출력은 이번에는 제외해줘.

기존 주제 내부 output/은 과거 결과로 보존합니다. 새 출력 구조는 [출력 안내](../output/README.md)를 참조하세요.
