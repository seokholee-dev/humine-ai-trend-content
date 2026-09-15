# 콘텐츠 스타일

카드뉴스의 제목·본문 위치와 공통 여백을 정의하고, 사용자가 제공한 투명 배경 Data Diving 로고를 적용합니다.

- [humine_content_guide.md](humine_content_guide.md): 문체·업무·교육·브랜드 표현 기준
- [humine_visual_guide.md](humine_visual_guide.md): 5종 위치·분량·유형 선택 기준
- [cardnews.css](cardnews.css): 공통 padding·gap·글자 크기·레이아웃·로고 크기
- [layout-preview.html](layout-preview.html): Data Diving 로고를 넣은 미리보기
- [assets/datadiving-logo.png](assets/datadiving-logo.png): 사용자 제공 투명 원본 로고

## 사용

style/ 폴더 전체를 내려받아 layout-preview.html을 브라우저에서 엽니다. CSS와 assets/의 상대 위치를 유지합니다. GitHub 화면에서는 HTML 코드로 표시됩니다.

캔버스 1080×1350, 좌우 여백 80px, 본문 제목 60px, 본문 40px을 기본으로 합니다.
cover / gradient / split / overlay / cta는 유형이며 전체 장수 제한이 아닙니다.

## 로고와 상태

표지와 CTA에 같은 투명 PNG를 사용하며 표시 영역은 360×80으로 축소했습니다. 로고 원본은 바꾸지 않습니다.
CTA는 배경 없이, 어두운 표지는 검정 글자 가독성을 위한 작은 밝은 받침과 함께 배치합니다.
나머지 배경·색상·글꼴·예시 문구는 시안입니다. 줄바꿈·넘침 검수는 사용자 요청에 따라 후속 관리합니다.
최종 이미지 자동 출력 기능은 아직 구현하지 않았습니다.
