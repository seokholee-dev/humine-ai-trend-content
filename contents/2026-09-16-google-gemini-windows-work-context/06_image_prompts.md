# Gemini Windows와 업무 맥락 — 시각 자료 제작 기록

- 작성일: 2026-09-16
- 조사 기준일: 2026-09-16
- 상태: 8종 제작·저장·내용 확인 완료 / 최종 카드 시각 검수 보류
- 입력 원고: 03_column.md, 04_cardnews.md
- 규격: 카드 1080×1350, split 이미지 1080:650 비율
- 스타일: ../../style/cardnews.css, ../../style/humine_visual_guide.md

## 공통 방향
기존 글자 위치와 여백을 유지한다. 네이비·따뜻한 종이색·차분한 청록으로 통일하되 8개 독립 자산을 사용한다. 실제 제품 UI를 생성하거나 모사하지 않는다. 제목·본문은 HTML로 별도 배치하고 도식의 정확한 라벨은 로컬 렌더링한다.
외부 후보 I1은 이번 패키지의 이용 범위 미확정으로 제외했다. 05_sources.md 참조. Data Diving 로고는 기존 사용자 제공 자산을 그대로 적용한다.
생성 사진은 가상 장면이며 종이에 보이는 차트·문구는 실제 데이터가 아니다. 칼럼의 대표 이미지로 표지를 재사용하는 이유는 동일한 자료 검토 메시지를 전달하기 위함이다.

## 01 — desk-concept
- 자산 ID: google-gemini-work-context-01-desk-concept-v1
- 목적·대체 텍스트: 문서와 노트북을 함께 검토하는 담당자, AI 생성 가상 장면
- 확보 방식: 내장 생성
- 레이아웃: cover
- 사용 채널·목적: 기업 업무·교육 HTML 시안, 향후 SNS용. 외부 게시 없음.
- 이용 기록: 자체 제작, 외부 사진·아이콘 미사용. 02장은 I1의 자체 도식 대안.
- 배치: split은 상단 650px, cover·gradient는 상단 시각 자료와 하단 문구 여백, CTA는 가운데 패널을 위한 여백 확보.
- 인접 장과 차이: 담당자 장면·키보드·선별 도식·네 단계 흐름·자료 대조·역량 그리드·비교 실습·워크숍을 장별로 구분.
- 별도로 배치할 정확한 한국어 문구: 04_cardnews.md 해당 장 제목·본문.
- 공통 토큰: 기존 CSS의 여백·글자 위치·크기 유지, 장별 예외 없음.
- 예정 파일명: images/google-gemini-work-context-01-desk-concept-v1.png
- 실제 경로: 저장 확인: images/google-gemini-work-context-01-desk-concept-v1.png
- 제작 상태: 생성·저장 완료
- 출처: 01·02장은 S1·S3, 03~05장은 S2·S5, 06~08장은 휴마인의 업무·교육 제안. 실제 제품 화면·실제 수치 차트 아님.
- 확보 불가 시 대안: 자체 개념도. 기획만으로 완료 표시하지 않음.

### 실제 생성 프롬프트
```text
Use case: photorealistic-natural. Asset: editorial illustration for a Korean enterprise AI educational card, NOT a real company case or product screenshot. Premium natural editorial photography, warm ivory paper, deep ink navy and muted teal details, subtle film grain, realistic materials, calm professional atmosphere. No text, no logos, no watermarks, no recognizable software UI, no robots, no holograms. Portrait 4:5 composition. Over-the-shoulder view of a Korean office project manager seated at a light oak desk, gathering a few printed project documents beside a neutral unbranded laptop. Laptop display is softly out of focus and not readable. Upper 55 percent holds the person, laptop and a small amber desk lamp. Bottom 40 percent is quiet dark navy foreground with no objects, for a headline added later. Intent: AI help arriving alongside real daily work, grounded in source documents. Anatomically realistic hands, understated business casual clothes.
```

## 02 — shortcut
- 자산 ID: google-gemini-work-context-02-shortcut-v1
- 목적·대체 텍스트: Alt와 Space 키를 연결한 단축키 개념도
- 확보 방식: 도식 직접 제작
- 레이아웃: gradient
- 사용 채널·목적: 기업 업무·교육 HTML 시안, 향후 SNS용. 외부 게시 없음.
- 이용 기록: 자체 제작, 외부 사진·아이콘 미사용. 02장은 I1의 자체 도식 대안.
- 배치: split은 상단 650px, cover·gradient는 상단 시각 자료와 하단 문구 여백, CTA는 가운데 패널을 위한 여백 확보.
- 인접 장과 차이: 담당자 장면·키보드·선별 도식·네 단계 흐름·자료 대조·역량 그리드·비교 실습·워크숍을 장별로 구분.
- 별도로 배치할 정확한 한국어 문구: 04_cardnews.md 해당 장 제목·본문.
- 공통 토큰: 기존 CSS의 여백·글자 위치·크기 유지, 장별 예외 없음.
- 예정 파일명: images/google-gemini-work-context-02-shortcut-v1.png
- 실제 경로: 저장 확인: images/google-gemini-work-context-02-shortcut-v1.png
- 제작 상태: 생성·저장 완료
- 출처: 01·02장은 S1·S3, 03~05장은 S2·S5, 06~08장은 휴마인의 업무·교육 제안. 실제 제품 화면·실제 수치 차트 아님.
- 확보 불가 시 대안: 자체 개념도. 기획만으로 완료 표시하지 않음.

### 제작 명세
Alt와 Space 키를 연결한 단축키 개념도. 도형·화살표·한국어 라벨을 직접 배치. 편집 가능한 제작 소스는 images/render-diagrams.swift에 보관한다.

## 03 — context-selection
- 자산 ID: google-gemini-work-context-03-context-selection-v1
- 목적·대체 텍스트: 여러 문서에서 목적·범위·최신성 기준으로 근거를 선택하는 도식
- 확보 방식: 도식 직접 제작
- 레이아웃: split
- 사용 채널·목적: 기업 업무·교육 HTML 시안, 향후 SNS용. 외부 게시 없음.
- 이용 기록: 자체 제작, 외부 사진·아이콘 미사용. 02장은 I1의 자체 도식 대안.
- 배치: split은 상단 650px, cover·gradient는 상단 시각 자료와 하단 문구 여백, CTA는 가운데 패널을 위한 여백 확보.
- 인접 장과 차이: 담당자 장면·키보드·선별 도식·네 단계 흐름·자료 대조·역량 그리드·비교 실습·워크숍을 장별로 구분.
- 별도로 배치할 정확한 한국어 문구: 04_cardnews.md 해당 장 제목·본문.
- 공통 토큰: 기존 CSS의 여백·글자 위치·크기 유지, 장별 예외 없음.
- 예정 파일명: images/google-gemini-work-context-03-context-selection-v1.png
- 실제 경로: 저장 확인: images/google-gemini-work-context-03-context-selection-v1.png
- 제작 상태: 생성·저장 완료
- 출처: 01·02장은 S1·S3, 03~05장은 S2·S5, 06~08장은 휴마인의 업무·교육 제안. 실제 제품 화면·실제 수치 차트 아님.
- 확보 불가 시 대안: 자체 개념도. 기획만으로 완료 표시하지 않음.

### 제작 명세
여러 문서에서 목적·범위·최신성 기준으로 근거를 선택하는 도식. 도형·화살표·한국어 라벨을 직접 배치. 편집 가능한 제작 소스는 images/render-diagrams.swift에 보관한다.

## 04 — brief-workflow
- 자산 ID: google-gemini-work-context-04-brief-workflow-v1
- 목적·대체 텍스트: 자료 지정·초안 요청·원문 대조·공유 판단의 네 단계
- 확보 방식: 도식 직접 제작
- 레이아웃: split
- 사용 채널·목적: 기업 업무·교육 HTML 시안, 향후 SNS용. 외부 게시 없음.
- 이용 기록: 자체 제작, 외부 사진·아이콘 미사용. 02장은 I1의 자체 도식 대안.
- 배치: split은 상단 650px, cover·gradient는 상단 시각 자료와 하단 문구 여백, CTA는 가운데 패널을 위한 여백 확보.
- 인접 장과 차이: 담당자 장면·키보드·선별 도식·네 단계 흐름·자료 대조·역량 그리드·비교 실습·워크숍을 장별로 구분.
- 별도로 배치할 정확한 한국어 문구: 04_cardnews.md 해당 장 제목·본문.
- 공통 토큰: 기존 CSS의 여백·글자 위치·크기 유지, 장별 예외 없음.
- 예정 파일명: images/google-gemini-work-context-04-brief-workflow-v1.png
- 실제 경로: 저장 확인: images/google-gemini-work-context-04-brief-workflow-v1.png
- 제작 상태: 생성·저장 완료
- 출처: 01·02장은 S1·S3, 03~05장은 S2·S5, 06~08장은 휴마인의 업무·교육 제안. 실제 제품 화면·실제 수치 차트 아님.
- 확보 불가 시 대안: 자체 개념도. 기획만으로 완료 표시하지 않음.

### 제작 명세
자료 지정·초안 요청·원문 대조·공유 판단의 네 단계. 도형·화살표·한국어 라벨을 직접 배치. 편집 가능한 제작 소스는 images/render-diagrams.swift에 보관한다.

## 05 — evidence-concept
- 자산 ID: google-gemini-work-context-05-evidence-concept-v1
- 목적·대체 텍스트: 초안과 원본 문서를 연필로 대조하는 손, AI 생성 가상 장면
- 확보 방식: 내장 생성
- 레이아웃: split
- 사용 채널·목적: 기업 업무·교육 HTML 시안, 향후 SNS용. 외부 게시 없음.
- 이용 기록: 자체 제작, 외부 사진·아이콘 미사용. 02장은 I1의 자체 도식 대안.
- 배치: split은 상단 650px, cover·gradient는 상단 시각 자료와 하단 문구 여백, CTA는 가운데 패널을 위한 여백 확보.
- 인접 장과 차이: 담당자 장면·키보드·선별 도식·네 단계 흐름·자료 대조·역량 그리드·비교 실습·워크숍을 장별로 구분.
- 별도로 배치할 정확한 한국어 문구: 04_cardnews.md 해당 장 제목·본문.
- 공통 토큰: 기존 CSS의 여백·글자 위치·크기 유지, 장별 예외 없음.
- 예정 파일명: images/google-gemini-work-context-05-evidence-concept-v1.png
- 실제 경로: 저장 확인: images/google-gemini-work-context-05-evidence-concept-v1.png
- 제작 상태: 생성·저장 완료
- 출처: 01·02장은 S1·S3, 03~05장은 S2·S5, 06~08장은 휴마인의 업무·교육 제안. 실제 제품 화면·실제 수치 차트 아님.
- 확보 불가 시 대안: 자체 개념도. 기획만으로 완료 표시하지 않음.

### 실제 생성 프롬프트
```text
Use case: photorealistic-natural. Asset: editorial illustration for a Korean enterprise AI educational card, NOT a real company case or product screenshot. Premium natural editorial photography, warm ivory paper, deep ink navy and muted teal details, subtle film grain, realistic materials, calm professional atmosphere. No text, no logos, no watermarks, no recognizable software UI, no robots, no holograms. Landscape 1080:650 composition. Close high-angle editorial still life of hands auditing a draft report: one hand holds a pencil pointing between two clearly different printed sheets, one sheet with simple unlabeled timeline marks, the other with small non-readable grey typesetting. A closed navy folder and a plain laptop corner at edge. Soft side daylight, meaningful evidence comparison, tactile paper, focus on source-versus-draft review. No checkmark that implies confirmed accuracy; no legible invented data. Different scene from cover, no face, no background office. Keep all important objects within central 80 percent.
```

## 06 — review-skills
- 자산 ID: google-gemini-work-context-06-review-skills-v1
- 목적·대체 텍스트: 자료 선택·요청 설계·근거 검증·공유 판단의 네 역량
- 확보 방식: 도식 직접 제작
- 레이아웃: split
- 사용 채널·목적: 기업 업무·교육 HTML 시안, 향후 SNS용. 외부 게시 없음.
- 이용 기록: 자체 제작, 외부 사진·아이콘 미사용. 02장은 I1의 자체 도식 대안.
- 배치: split은 상단 650px, cover·gradient는 상단 시각 자료와 하단 문구 여백, CTA는 가운데 패널을 위한 여백 확보.
- 인접 장과 차이: 담당자 장면·키보드·선별 도식·네 단계 흐름·자료 대조·역량 그리드·비교 실습·워크숍을 장별로 구분.
- 별도로 배치할 정확한 한국어 문구: 04_cardnews.md 해당 장 제목·본문.
- 공통 토큰: 기존 CSS의 여백·글자 위치·크기 유지, 장별 예외 없음.
- 예정 파일명: images/google-gemini-work-context-06-review-skills-v1.png
- 실제 경로: 저장 확인: images/google-gemini-work-context-06-review-skills-v1.png
- 제작 상태: 생성·저장 완료
- 출처: 01·02장은 S1·S3, 03~05장은 S2·S5, 06~08장은 휴마인의 업무·교육 제안. 실제 제품 화면·실제 수치 차트 아님.
- 확보 불가 시 대안: 자체 개념도. 기획만으로 완료 표시하지 않음.

### 제작 명세
자료 선택·요청 설계·근거 검증·공유 판단의 네 역량. 도형·화살표·한국어 라벨을 직접 배치. 편집 가능한 제작 소스는 images/render-diagrams.swift에 보관한다.

## 07 — comparison-exercise
- 자산 ID: google-gemini-work-context-07-comparison-exercise-v1
- 목적·대체 텍스트: 자유 요청과 범위 지정 요청의 결과를 비교하는 실습 도식
- 확보 방식: 도식 직접 제작
- 레이아웃: split
- 사용 채널·목적: 기업 업무·교육 HTML 시안, 향후 SNS용. 외부 게시 없음.
- 이용 기록: 자체 제작, 외부 사진·아이콘 미사용. 02장은 I1의 자체 도식 대안.
- 배치: split은 상단 650px, cover·gradient는 상단 시각 자료와 하단 문구 여백, CTA는 가운데 패널을 위한 여백 확보.
- 인접 장과 차이: 담당자 장면·키보드·선별 도식·네 단계 흐름·자료 대조·역량 그리드·비교 실습·워크숍을 장별로 구분.
- 별도로 배치할 정확한 한국어 문구: 04_cardnews.md 해당 장 제목·본문.
- 공통 토큰: 기존 CSS의 여백·글자 위치·크기 유지, 장별 예외 없음.
- 예정 파일명: images/google-gemini-work-context-07-comparison-exercise-v1.png
- 실제 경로: 저장 확인: images/google-gemini-work-context-07-comparison-exercise-v1.png
- 제작 상태: 생성·저장 완료
- 출처: 01·02장은 S1·S3, 03~05장은 S2·S5, 06~08장은 휴마인의 업무·교육 제안. 실제 제품 화면·실제 수치 차트 아님.
- 확보 불가 시 대안: 자체 개념도. 기획만으로 완료 표시하지 않음.

### 제작 명세
자유 요청과 범위 지정 요청의 결과를 비교하는 실습 도식. 도형·화살표·한국어 라벨을 직접 배치. 편집 가능한 제작 소스는 images/render-diagrams.swift에 보관한다.

## 08 — workshop-concept
- 자산 ID: google-gemini-work-context-08-workshop-concept-v1
- 목적·대체 텍스트: 네 사람이 테이블 주변에서 자료를 정리하는 AI 생성 워크숍 장면
- 확보 방식: 내장 생성
- 레이아웃: cta
- 사용 채널·목적: 기업 업무·교육 HTML 시안, 향후 SNS용. 외부 게시 없음.
- 이용 기록: 자체 제작, 외부 사진·아이콘 미사용. 02장은 I1의 자체 도식 대안.
- 배치: split은 상단 650px, cover·gradient는 상단 시각 자료와 하단 문구 여백, CTA는 가운데 패널을 위한 여백 확보.
- 인접 장과 차이: 담당자 장면·키보드·선별 도식·네 단계 흐름·자료 대조·역량 그리드·비교 실습·워크숍을 장별로 구분.
- 별도로 배치할 정확한 한국어 문구: 04_cardnews.md 해당 장 제목·본문.
- 공통 토큰: 기존 CSS의 여백·글자 위치·크기 유지, 장별 예외 없음.
- 예정 파일명: images/google-gemini-work-context-08-workshop-concept-v1.png
- 실제 경로: 저장 확인: images/google-gemini-work-context-08-workshop-concept-v1.png
- 제작 상태: 생성·저장 완료
- 출처: 01·02장은 S1·S3, 03~05장은 S2·S5, 06~08장은 휴마인의 업무·교육 제안. 실제 제품 화면·실제 수치 차트 아님.
- 확보 불가 시 대안: 자체 개념도. 기획만으로 완료 표시하지 않음.

### 실제 생성 프롬프트
```text
Use case: photorealistic-natural. Asset: editorial illustration for a Korean enterprise AI educational card, NOT a real company case or product screenshot. Premium natural editorial photography, warm ivory paper, deep ink navy and muted teal details, subtle film grain, realistic materials, calm professional atmosphere. No text, no logos, no watermarks, no recognizable software UI, no robots, no holograms. Portrait 4:5 composition. Top-down collaborative workshop table with four adult colleagues' forearms at the outer edges, three small groups of muted teal and ochre sticky notes, pens, a plain notebook, a coffee mug at the edge. Centre 65 percent must remain visually quiet light oak for an opaque text panel added later. Realistic hands, warm collaborative mood, actual physical learning materials. Distinct from solitary desk and source-auditing closeup. No screens, no writing or logos.
```


## 제작 확인
- 내장 생성 3종의 피사체·구도·손·여백 확인. 실제 인물·제품 화면으로 사용하지 않음.
- 도식 5종의 한국어 라벨·흐름·이미지 크기를 열어 확인. 최종 카드의 줄바꿈·넘침 검수와 구분.
- 첫 로컬 도식 렌더링에서 Swift·SDK 버전 불일치 발생. 설치된 MacOSX15.4 SDK를 명시해 렌더링 성공. 추가 설치·외부 서비스 미사용.
- 도식 재제작 명령: `swift -sdk /Library/Developer/CommandLineTools/SDKs/MacOSX15.4.sdk -module-cache-path /tmp/humaiin-swift-cache15 images/render-diagrams.swift images` (이 주제 폴더에서 실행, macOS용).

## 실제 자산 크기·해시
- google-gemini-work-context-01-desk-concept-v1.png: 1122×1402, SHA256 `02f46e322538dca74fe7c6d22ee5e7c583855fd69d2b5cf51695af115626c425`
- google-gemini-work-context-02-shortcut-v1.png: 1080×1350, SHA256 `0bea84eaab8ecd5dfa4f63122d3040c150e68b8de6748d613c859640af7a327a`
- google-gemini-work-context-03-context-selection-v1.png: 1080×650, SHA256 `e10c12f7e201d596cfd351dd61f76afd62f7600d414c218d4eba525ea42ef536`
- google-gemini-work-context-04-brief-workflow-v1.png: 1080×650, SHA256 `0626405f524a29f12b7e6b07d512a2b7d4a6c138d3eaa77189b9edd510413ad5`
- google-gemini-work-context-05-evidence-concept-v1.png: 1617×972, SHA256 `65c6f6024b86317e15c2bd0868950ebf86c79af5ce21ea7f07b5d27db4879624`
- google-gemini-work-context-06-review-skills-v1.png: 1080×650, SHA256 `245cff5b4f31c7732861dc887f25f70c4b1c5b66c13ba891ce13a3e365d2069b`
- google-gemini-work-context-07-comparison-exercise-v1.png: 1080×650, SHA256 `56f2a7717c2f37c4d22c02cf94796dca910c9a82e0220972b2a4cbc49dcf2e09`
- google-gemini-work-context-08-workshop-concept-v1.png: 1122×1402, SHA256 `060fb55bd60867ab13044a999a6c9ac899d5bd11f8c84bb61dc9bee7e43a88ee`

## 원고 흐름 v2 반영
실제 시각 자산은 기존 8종 유지. 03장의 자료 선택 도식은 주간 보고에 쓸 자료를 고르는 장면으로, 04장의 업무 흐름도는 요청 예시가 전체 업무에서 차지하는 위치로 연결했다. 05장의 문서 대조 장면에는 가상 일정 충돌을 설명하는 문구를 배치한다. 도식 라벨 자체는 변경하지 않았으며 새 이미지를 생성했다고 표시하지 않는다.
