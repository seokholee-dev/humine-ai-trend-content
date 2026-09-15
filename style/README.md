# 콘텐츠 스타일

카드뉴스의 제목·본문 위치와 공통 여백을 정의하고, 사용자가 제공한 Data Diving 로고를 적용합니다.

- [humine_content_guide.md](humine_content_guide.md): 문체·업무·교육·브랜드 표현 기준
- [humine_visual_guide.md](humine_visual_guide.md): 참고한 5종의 위치·분량·유형 선택 기준
- [cardnews.css](cardnews.css): 공통 padding·gap·글자 크기·레이아웃·로고 표시 영역
- [layout-preview.html](layout-preview.html): 예시 문구와 Data Diving 로고를 넣은 미리보기
- [assets/datadiving-logo.png](assets/datadiving-logo.png): 사용자 제공 원본 로고

## 사용

style/ 폴더 전체를 내려받고 layout-preview.html을 브라우저에서 엽니다. CSS와 assets/의 상대 위치를 유지합니다. GitHub 파일 화면에서는 HTML 코드로 표시됩니다.

기준: 1080×1350, 좌우 여백 80px, 본문 제목 60px, 본문 40px. 표지·CTA는 역할별 크기를 따릅니다.
cover / gradient / split / overlay / cta는 레이아웃 유형이며 전체 장수를 의미하지 않습니다.

## 로고와 상태

표지 하단과 CTA 패널 하단에 같은 Data Diving 원본을 사용합니다. 임시 HUMINE 로고를 만들지 않습니다.
로고의 픽셀·색상·문구는 변경하지 않았으며 정사각형 이미지의 넓은 흰 여백만 CSS 표시 영역에서 줄여 보입니다.
나머지 배경·색상·글꼴·예시 문구는 시안입니다. 줄바꿈·넘침 검수는 사용자 요청에 따라 후속 관리합니다.
최종 이미지 자동 출력 기능은 아직 구현하지 않았습니다.
