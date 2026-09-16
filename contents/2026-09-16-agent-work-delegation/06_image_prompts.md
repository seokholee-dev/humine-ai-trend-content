# 업무 위임 설계 — 시각 자료 기획

- 작성일: 2026-09-16
- 조사 기준일: 2026-09-16
- 상태: 생성 완료 / 이미지 내용·구도 확인 완료 / 카드 시각 검수 보류
- 입력 원고: 03_column.md, 04_cardnews.md
- 대상 규격: 카드 1080×1350 / 생성 배경은 세로 4:5 요청
- 적용 스타일: ../../style/cardnews.css
- 적용 가이드: ../../style/humine_visual_guide.md
- 도구: 현재 대화의 내장 image_gen. 별도 API 호출 없음.

## 공통 방향
생성 일러스트 2종을 반복 사용해 한 묶음의 시각적 일관성을 유지한다. 남색·백색·청색, 승인 지점을 표시하는 작은 호박색 강조는 이번 콘텐츠의 임시 시안이며 공식 브랜드 규정이 아니다. 글자와 Data Diving 원본 로고는 HTML/CSS로 별도 합성한다. 실사 제품 화면과 수치 차트는 만들지 않는다.

## hero — 카드 1·2·4·7장 / 칼럼 도입 이후
- 목적·유형: 업무 모듈과 판단 지점을 보여주는 생성 개념 일러스트
- 구성·정보 위계: 상단 절반에 핵심 오브젝트, 하단 45%는 어두운 문구 여백.
- 레이아웃: cover / gradient / split / overlay
- 별도로 배치할 정확한 한국어 문구: 04_cardnews.md의 연결된 장 제목·본문을 그대로 합성.
- 실제 화면·데이터 출처 ID: 해당 없음. 원고 해석의 시각화이며 실제 화면이 아님.
- 공통 토큰·예외 이유: --card-padding, --title-size, --body-size 및 레이아웃별 위치 토큰. 예외 없음.
- 예정 파일명: images/hero.png (실제 반환 형식에 따라 확장자 확인)
- 대체 텍스트: 연결된 업무 모듈 사이에 사람의 판단 지점을 상징하는 호박색 구조물이 놓인 개념 일러스트
- 제작 상태: 생성 완료 (내용·구도 확인 완료)
- 실제 생성 경로: images/hero.png
- 실제 크기: 1122×1402 PNG

### 최종 제작 프롬프트
Use case: stylized-concept. Asset type: editorial illustration for a Korean enterprise AI column and a 4:5 vertical card-news background. Create a refined, tactile 3D editorial scene about designing bounded workflows for AI agents. A small arrangement of ceramic-white and translucent ice-blue architectural task modules connected by thin luminous blue paths on a deep navy surface; one deliberate amber checkpoint in the route symbolizes a human decision. Distinct sculptural shapes, physically plausible soft shadows, premium editorial art direction, generous restraint, no robot, no sci-fi city. Place the entire focal arrangement in the upper half of the portrait canvas, with the lower 45 percent fading to quiet solid midnight navy so Korean copy can be added later. Intended portrait aspect ratio 4:5. No text, numbers, letters, captions, logos, watermark, charts, or product UI. This is a conceptual illustration, not a real interface or performance diagram.

## approval — 카드 3·5·6·8장 / 칼럼 가상 실습 앞
- 목적·유형: 실행 전에 사람이 확인하는 장면을 보여주는 생성 개념 일러스트
- 구성·정보 위계: 상단 절반에 핵심 오브젝트, 하단 45%는 어두운 문구 여백.
- 레이아웃: overlay / split / gradient / cta
- 별도로 배치할 정확한 한국어 문구: 04_cardnews.md의 연결된 장 제목·본문을 그대로 합성.
- 실제 화면·데이터 출처 ID: 해당 없음. 원고 해석의 시각화이며 실제 화면이 아님.
- 공통 토큰·예외 이유: --card-padding, --title-size, --body-size 및 레이아웃별 위치 토큰. 예외 없음.
- 예정 파일명: images/approval.png (실제 반환 형식에 따라 확장자 확인)
- 대체 텍스트: 승인 지점 앞에서 작업 카드를 멈추고 검토하는 손을 표현한 개념 일러스트
- 제작 상태: 생성 완료 (내용·구도 확인 완료)
- 실제 생성 경로: images/approval.png
- 실제 크기: 1122×1402 PNG

### 최종 제작 프롬프트
Use case: stylized-concept. Asset type: matching 4:5 vertical editorial card background and column illustration. Create a premium tactile editorial 3D scene illustrating a human review checkpoint in an AI-assisted work process. On a midnight navy tabletop, several small ivory paper-like task tiles travel on a simple pale blue path toward a single amber translucent gate. A natural, anatomically correct adult human hand gently holds the last tile just before the gate, conveying considered approval. No dramatic danger, no red alerts, no robot hands. Matte ceramic textures, translucent blue details, soft studio light, carefully restrained composition. All important objects and the hand in the upper half; lower 45 percent plain deep navy negative space for later Korean typesetting. Portrait 4:5. No writing, numbers, captions, logos, watermarks, product UI, charts or implied statistics. A conceptual illustration, not a photo of an actual deployment.

## CSS·시각 검수
- 레이아웃 위치·로고 참조: 기존 CSS 사용.
- 이미지 내용·구도: 도구가 반환한 실제 이미지 2종을 확인. 상단의 업무/승인 장면과 하단 여백, 문자·제품 UI 부재 확인. 칼럼에는 생성 일러스트 표기. 카드의 최종 대비·잘림 판정은 미실시.
- padding·gap의 화면상 일치, 글꼴 로딩, 출처 가독성, 대비, 실제 한글 줄바꿈·넘침: 미실시/보류.
- 최종 카드 PNG: 별도 요청·렌더링 단계. 현재 범위는 이미지 생성과 HTML 합성.

## 미확정 항목
채널, 공식 브랜드 색상·글꼴. 생성 원본 크기는 자산별 항목에 기록했다. 원본을 직접 변형하지 않고 CSS에서 배치한다.
