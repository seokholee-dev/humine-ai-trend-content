# Humine AI Trend Content

휴마인 AI 트렌드 콘텐츠 자동화를 위한 작업공간입니다.
최신 AI 트렌드를 기업의 업무와 교육 관점에서 해석하고, 하나의 리서치를 카드뉴스와 칼럼으로 확장합니다.

**Trend → Work → Skill → Education**

## 현재 상태

- Private 저장소의 기본 파일 구조 구성 완료
- AI 작업 규칙, 단계별 프롬프트 6종, 콘텐츠 양식 7종, 문체·비주얼 가이드와 공통 CSS 준비 완료
- 참고한 5종 카드뉴스 레이아웃: 표지 / 전체 그라데이션 / 하단 분할 / 중앙 오버레이 / CTA
- 줄바꿈·넘침 검수: 사용자 요청에 따라 후속 단계로 보류
- 실제 주제의 원고·이미지와 자동 실행·최종 이미지 출력 기능은 아직 생성하지 않았습니다.

## 파일 구조

~~~text
humine-ai-trend-content/
├── README.md
├── AGENTS.md
├── prompts/
│   ├── README.md
│   ├── research.md
│   ├── core_brief.md
│   ├── column_writer.md
│   ├── cardnews_writer.md
│   ├── visual_planner.md
│   └── fact_check.md
├── templates/
│   ├── README.md
│   ├── research_template.md
│   ├── core_brief_template.md
│   ├── column_template.md
│   ├── cardnews_template.md
│   ├── sources_template.md
│   ├── image_prompts_template.md
│   └── review_template.md
├── style/
│   ├── README.md
│   ├── humine_content_guide.md
│   ├── humine_visual_guide.md
│   ├── cardnews.css
│   └── layout-preview.html
└── contents/
    └── README.md
~~~

## 파일별 역할

| 위치 | 용도 |
| --- | --- |
| [AGENTS.md](AGENTS.md) | AI 작업 순서, 출처·품질 기준, 보류 항목 |
| [prompts/README.md](prompts/README.md) | 단계별 실행 지침과 요청 예시 |
| [templates/README.md](templates/README.md) | 실제 원고에 사용할 양식과 저장 파일명 |
| [콘텐츠 가이드](style/humine_content_guide.md) | 한국어 문체, 업무·교육 연결, 브랜드 표현 |
| [비주얼 가이드](style/humine_visual_guide.md) | 5종 텍스트 위치·정렬·분량 기준 |
| [공통 CSS](style/cardnews.css) | padding·gap·글자 크기·레이아웃 공통 값 |
| [contents/README.md](contents/README.md) | 주제별 저장 구조와 첫 콘텐츠 시작 방법 |

## 콘텐츠 제작 순서

리서치·출처 → Core Brief → 칼럼·카드뉴스 → 시각 자료 기획 → 사실·내용 검수.

실제 콘텐츠를 시작하면 contents/YYYY-MM-DD-topic-slug/에 다음 파일을 필요한 순서대로 생성합니다.

~~~text
01_research.md
02_core_brief.md
03_column.md
04_cardnews.md
05_sources.md
06_image_prompts.md
07_review.md
images/   # 실제 이미지 생성 시
output/   # 실제 최종 결과물 출력 시
~~~

이 주제 폴더는 첫 작업 때 생성합니다. 템플릿이나 빈 폴더를 완성 콘텐츠로 취급하지 않습니다.
칼럼과 카드뉴스는 같은 Core Brief와 출처 ID를 공유하며 요청된 형식만 작성합니다.

## 카드뉴스 스타일

제목·본문 위치와 공통 여백을 먼저 고정합니다. 5종은 유형의 수이며 전체 장수 제한이 아닙니다.
현재 시안은 1080×1350, 좌우 여백 80px, 본문 제목 60px, 본문 40px이며 역할별 예외는 CSS 토큰으로 관리합니다.
색상·글꼴·브랜드 자산은 후속 확정 항목입니다.

[HTML 미리보기](style/layout-preview.html)는 CSS와 같은 폴더에 내려받아 브라우저에서 엽니다. GitHub에서는 코드로 표시됩니다.

## 검수와 후속 작업

파일 구조, 양식의 필수 항목, 입출력 이름과 공통 스타일 연결을 점검했습니다.
줄바꿈·넘침 검수는 지금 수행하지 않으며 07_review.md에서 보류로 관리합니다. 사실·내용 검수 완료와 최종 이미지 검수 완료를 구분합니다.

다음은 첫 주제를 정해 리서치와 카드뉴스 원고를 만드는 단계입니다. 파일만 저장하면 자동으로 실행되지는 않습니다.

## 첫 요청 예시

> 최근 7일 AI 트렌드를 조사하고 추천 주제로 Core Brief와 카드뉴스 원고를 만들어줘. prompts/와 templates/를 사용하고, 줄바꿈·넘침 검수와 이미지 출력은 이번에는 제외해줘.
