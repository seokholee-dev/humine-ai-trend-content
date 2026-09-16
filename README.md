# Humaiin AI Trend Content

AI 트렌드를 기업 업무와 교육 관점에서 해석하고, 하나의 리서치를 카드뉴스와 칼럼으로 확장하는 Private 작업공간입니다.

**Trend → Work → Skill → Education**

## 현재 상태

- 기본 파일 구조 구성 완료: 작업 규칙, 단계별 프롬프트 6종과 대화 실행 지침, 양식 7종, 문체·시각 가이드, 공통 CSS, 콘텐츠 보관 안내
- 콘텐츠 로고: 사용자가 제공한 투명 배경 Data Diving PNG
- 로고 표시 영역: 360×80. 표지 하단과 CTA 패널 하단에 동일 자산 사용
- 줄바꿈·넘침 검수: 사용자 요청에 따라 후속 단계로 보류
- scripts/ 실행 코드 반영 완료: 작업 폴더 준비, API 리서치·원고 생성, AI 이미지 생성, HTML 및 선택적 PNG 출력.
- 로컬 기능 테스트 18개 통과. 내장 이미지 도구로 실제 이미지 2종 생성·저장·연결 완료. 별도 유료 API 호출·최종 카드 PNG 출력 검증은 미실시.
- [첫 주제 콘텐츠](contents/2026-09-16-agent-work-delegation/07_review.md): 칼럼·8장 카드뉴스 원고와 이미지 2종, HTML 합성 완료. 원고 사실·내용 검수 완료, 카드 시각 검수 보류.
- 대화 제작 경로를 추가했으며, 이미지 명령은 기본적으로 대화 도구용 요청만 출력합니다. 별도 API 실행 옵션에서 비용이 발생합니다.

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
│   ├── layout-preview.html
│   └── assets/
│       ├── README.md
│       └── datadiving-logo.png
├── scripts/
│   ├── README.md
│   ├── generate_content.py
│   ├── write_content.py
│   ├── generate_images.py
│   ├── openai_client.py
│   ├── build_cardnews.py
│   ├── requirements-render.txt
│   ├── cardnews.example.md
│   ├── test_pipeline.py
│   └── test_api.py
└── contents/
    └── README.md
~~~

## 사용 안내

| 위치 | 용도 |
| --- | --- |
| [AGENTS.md](AGENTS.md) | 작업 순서, 출처·품질 기준, 검수 보류 항목 |
| [prompts/README.md](prompts/README.md) | 단계별 실행 지침과 요청 예시 |
| [templates/README.md](templates/README.md) | 원고 양식과 저장 파일명 |
| [콘텐츠 가이드](style/humine_content_guide.md) | 한국어 문체와 업무·교육·브랜드 표현 |
| [비주얼 가이드](style/humine_visual_guide.md) | 5종 텍스트 위치·정렬·분량·로고 기준 |
| [공통 CSS](style/cardnews.css) | padding·gap·글자 크기·레이아웃·로고 표시 크기 |
| [콘텐츠 보관 안내](contents/README.md) | 주제별 폴더 구성과 시작 방법 |

## 콘텐츠 제작

리서치·출처 → Core Brief → 요청한 칼럼·카드뉴스 → 시각 자료 기획 → 사실·내용 검수.
주제 작업을 시작하면 contents/YYYY-MM-DD-topic-slug/에 필요한 파일을 순서대로 생성합니다.

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

템플릿과 빈 폴더를 완성 콘텐츠로 취급하지 않습니다. 같은 주제의 칼럼·카드뉴스는 Core Brief와 출처 ID를 공유합니다.

## 카드뉴스 스타일과 로고

참고 이미지의 표지·전체 그라데이션·하단 분할·중앙 오버레이·CTA 유형을 사용합니다. 5종은 틀의 종류이며 전체 장수와는 별개입니다.
제목·본문 위치와 여백을 먼저 고정합니다. 1080×1350, 좌우 padding 80px, 본문 제목 60px, 본문 40px이 현재 시안 기준입니다.

[투명 Data Diving 로고](style/assets/datadiving-logo.png)는 원본 픽셀과 비율을 유지합니다. 이전 미리보기보다 실제 보이는 폭을 약 20% 줄였습니다.
CTA에는 별도 배경 없이 배치하고, 어두운 표지에서는 검정 글자 가독성을 위한 작은 밝은 받침을 둡니다.
나머지 색상·글꼴·예시 문구는 시안입니다.

[HTML 미리보기](style/layout-preview.html)는 style/ 전체를 내려받아 브라우저에서 엽니다. CSS와 assets/의 위치를 유지합니다. GitHub에서는 코드로 표시됩니다.

## 검수와 다음 단계

파일 구조, 양식의 필수 항목·입출력 연결, 공통 스타일·로고 참조를 점검했습니다.
줄바꿈·넘침 검수는 수행하지 않았으며 07_review.md에서 보류로 관리합니다. 원고 검수와 최종 이미지 검수를 구분합니다.
첫 주제의 원고·생성 이미지·HTML은 위 콘텐츠 폴더에 저장했습니다. 다음 단계는 보류된 시각 검수와 최종 카드 PNG 출력입니다. 파일만 저장하면 자동으로 실행되지는 않습니다.

## 첫 요청 예시

> 최근 7일 AI 트렌드를 조사하고 추천 주제로 Core Brief와 카드뉴스 원고를 만들어줘. prompts/와 templates/를 사용하고, 줄바꿈·넘침 검수와 이미지 출력은 이번에는 제외해줘.

## 현재 대화에서 바로 제작

별도 API 키 없이 이 대화에서 리서치·원고 작성·이미지 도구를 통한 생성까지 진행할 수 있습니다. 도구의 이용 한도는 현재 환경에 따릅니다. Python은 작업 준비와 로컬 합성을 담당하며 대화 도구를 직접 호출하지 않습니다.

```sh
python3 scripts/generate_content.py --topic "AI 에이전트와 업무" --slug ai-agent --format both --images chat
```

생성된 `00_task.md`를 실행해 달라고 요청하거나, 아래처럼 이 대화에 바로 요청하세요.

> 최근 7일 AI 트렌드에서 주제를 선정해 칼럼·카드뉴스와 배경 이미지까지 만들어줘. 별도 API 없이 prompts/chat_workflow.md에 따라 진행하고 HTML로 합성해줘. 줄바꿈·넘침 검수는 보류해줘.

이미지 생성, 로컬 파일 저장, 최종 카드 PNG 출력은 별도 상태로 기록합니다. 상세 절차는 [대화 실행 지침](prompts/chat_workflow.md)과 [실행 가이드](scripts/README.md)를 참조하세요.

## 실행 방법과 API 비용

[실행 가이드](scripts/README.md)를 따릅니다. Python 3.9 이상이 필요합니다. 기본 모델은 원고 gpt-5.4-mini, 이미지 gpt-image-2.5-flare이며 명령 옵션으로 변경할 수 있습니다. 계정의 모델 사용 권한과 결제 설정은 별도 확인이 필요합니다.

- API 키 없는 작업 폴더 준비·HTML 출력: 추가 API 요금 없음.
- write_content.py / generate_images.py: --execute 없이 계획 확인만 실행.
- write_content.py의 --execute, generate_images.py의 --mode api --execute: OPENAI_API_KEY가 설정된 환경에서 실제 API 호출. ChatGPT 구독과 별도 과금.
- 이미지·원고·사실 검수·시각 검수·외부 게시의 완료 상태는 각각 구분합니다.
- 저장소 URL과 기존 경로명은 호환성을 위해 유지하며 브랜드 영문 표기는 Humaiin을 사용합니다. 카드 로고는 Data Diving 원본입니다.
