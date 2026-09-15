# Humine AI Trend Content

휴마인 AI 트렌드 콘텐츠 자동화를 위한 작업공간입니다.
최신 AI 트렌드를 기업의 업무와 교육 관점에서 해석하고, 하나의 리서치를 카드뉴스와 칼럼으로 확장합니다.

## 콘텐츠 제작 흐름

AI 트렌드 리서치 → Core Brief(핵심 기획 요약) → 카드뉴스·칼럼 원고 → 이미지 → 최종 콘텐츠

콘텐츠의 기본 메시지: **Trend → Work → Skill → Education**

## 현재 상태

- 저장소 공개 범위: Private
- 현재 구성: README.md, [AGENTS.md](AGENTS.md), [prompts/](prompts/), [style/](style/)
- 완료: AI 작업 규칙, 단계별 작업 프롬프트 6종, 참고 기반 5종 텍스트 레이아웃·공통 CSS 초안
- 자동화 구현 전, 작성 규칙과 템플릿을 단계적으로 준비하는 단계입니다.

## 추가 예정 구조

README.md, AGENTS.md, prompts/, style/은 작성했습니다. templates/와 contents/는 다음 단계에서 추가합니다.

```text
humine-ai-trend-content/
├── README.md
├── AGENTS.md    # AI 작업 규칙
├── prompts/    # 리서치·기획·작성·검수 프롬프트
├── templates/  # Core Brief·카드뉴스·칼럼 템플릿
├── style/      # 휴마인 문체·디자인 가이드
└── contents/   # 주제별 리서치·원고·이미지·최종 결과물
```

## 다음 단계

1. templates/에 Core Brief·칼럼·카드뉴스 공통 양식 추가
2. style/에 문체·브랜드 가이드 보완 및 레이아웃 확인
3. contents/에서 첫 번째 주제의 콘텐츠 제작·검수
4. 실제 원고를 넣어 줄바꿈·넘침·이미지 출력 흐름 검증

## 프롬프트 사용

[prompts/README.md](prompts/README.md)에 실행 순서와 요청 예시가 있습니다. 리서치 → Core Brief → 칼럼·카드뉴스 → 시각 자료 → 검수로 이어집니다. 파일만 저장하면 자동으로 실행되는 구조는 아니며, 이미지 자동 출력은 후속 단계입니다.

## 텍스트 레이아웃과 CSS

참고 이미지의 5종: 표지·전체 그라데이션·하단 분할·중앙 오버레이·CTA 패널. 5종은 유형의 수이며 총 장수와는 별개입니다.
현재 시안은 1080×1350, 좌우 여백 80px, 본문 제목 60px, 본문 40px입니다. 제목과 본문의 위치를 먼저 고정하고 공통 값은 [cardnews.css](style/cardnews.css)에서 관리합니다.

[레이아웃 가이드](style/humine_visual_guide.md)와 [HTML 미리보기](style/layout-preview.html)를 확인하세요. HTML과 CSS를 같은 폴더에 내려받아 HTML을 브라우저에서 엽니다. GitHub에서는 코드로 표시됩니다.

파일 연결·공통 토큰·5종 클래스는 점검했습니다. 브라우저 화면 검수, 실제 원고의 넘침, 최종 이미지 출력 검수는 미실시입니다. 현재 색상·글꼴·문구는 검토용 초안입니다.
