# 콘텐츠 양식 사용 안내

각 양식의 {{자리표시자}}를 실제 내용으로 채우고, 필요한 파일만 주제 폴더에 저장합니다. 템플릿 자체와 미작성 항목을 완성 콘텐츠로 취급하지 않습니다.

| 양식 | 저장할 파일 | 연결 프롬프트 |
| --- | --- | --- |
| [research_template.md](research_template.md) | 01_research.md | ../prompts/research.md |
| [core_brief_template.md](core_brief_template.md) | 02_core_brief.md | ../prompts/core_brief.md |
| [column_template.md](column_template.md) | 03_column.md | ../prompts/column_writer.md |
| [cardnews_template.md](cardnews_template.md) | 04_cardnews.md | ../prompts/cardnews_writer.md |
| [sources_template.md](sources_template.md) | 05_sources.md | 리서치·작성·검수 공통 |
| [image_prompts_template.md](image_prompts_template.md) | 06_image_prompts.md | ../prompts/visual_planner.md |
| [review_template.md](review_template.md) | 07_review.md | ../prompts/fact_check.md |

## 작성 순서

리서치·출처 → Core Brief → 요청한 칼럼·카드뉴스 → 시각 자료 기획 → 검수.
원고 작성 전에 AGENTS.md와 관련 프롬프트, style/humine_content_guide.md를 읽습니다.
카드뉴스는 style/humine_visual_guide.md의 5종과 style/cardnews.css를 따릅니다.

## 상태와 경로

- 저장 위치: contents/YYYY-MM-DD-topic-slug/
- 템플릿 안의 ../../style/ 경로는 위 주제 폴더로 복사한 이후 기준입니다.
- 같은 주제의 출처 ID와 핵심 메시지를 공유합니다.
- 해당하지 않는 항목은 해당 없음으로 표시하고, 미확인 항목은 숨기지 않습니다.
- 실제 원고 작성 전의 템플릿 상태는 콘텐츠 검수 완료를 의미하지 않습니다.
- 줄바꿈·넘침 검수는 사용자 요청에 따라 후속 단계로 보류합니다. 사실·내용 검수와 분리해 상태를 관리합니다.
