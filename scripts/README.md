# 로컬 제작 도구

원고·이미지 제작은 VS Code 대화에서 Codex가 수행합니다. Python 3.9 이상을 사용하는 아래 도구는 파일 준비와 로컬 합성만 담당합니다. 별도 유료 API 실행 코드와 옵션은 제거했습니다.

## 1. 주제 폴더 준비

```sh
python3 scripts/generate_content.py --topic "AI 에이전트와 업무" --slug ai-agent --format both --images chat
```

날짜를 생략하면 실행일을 사용합니다. `--format`은 `column`, `cardnews`, `both` 중 선택합니다. `--images chat`은 작업 요청에 내장 이미지 생성을 포함하고, 기본값 `plan`은 기획까지만 요청합니다. 명령 자체가 원고나 이미지를 생성하지는 않습니다.

생성된 `00_task.md`를 실행해 달라고 대화에서 요청하세요. 기존 주제는 새로 만들지 않고 이어서 작업합니다. 같은 이름의 폴더는 덮어쓰지 않습니다. 아래 출력 예시는 `contents/2026-09-15-ai-agent`를 실제 주제 경로로 바꿔 사용하세요.

## 2. 작성된 카드뉴스를 HTML로 출력

```sh
python3 scripts/build_cardnews.py contents/2026-09-15-ai-agent
```

`04_cardnews.md`를 읽어 저장소 최상위 `output/주제폴더명/build-실행시각/`에 결과물을 저장합니다. 장별 HTML은 `html/`, PNG 요청 시 장별 이미지는 `png/`, 사용한 배경 원본은 `assets/`에 모읍니다. 전체 보기 `index.html`과 상태 기록 `manifest.json`은 실행 폴더 최상위에 둡니다. 매번 새 폴더를 만들므로 이전 출력은 보존됩니다.

파일명에는 주제 폴더명을 붙입니다. 예를 들어 `2026-09-16-zendesk-specialized-agents-card-01.html`과 같은 이름을 사용하며 PNG도 같은 이름을 씁니다. `assets/`에는 주제명·장 번호·원본 이름을 함께 붙이고, `manifest.json`에 장별 실제 경로를 기록합니다. 새 주제의 `--slug`는 회사·제품·이슈를 나타내는 이름으로 지정하세요.

- 기존 `style/cardnews.css`의 1080×1350, padding, 글자 위치를 사용합니다.
- 사용자 제공 투명 Data Diving 로고와 축소된 로고 크기를 적용합니다.
- CSS와 로고·배경을 HTML 안에 포함해 출력 파일을 옮겨도 연결이 유지됩니다.
- 배경이 없으면 임시 색상 배경을 사용합니다. 이미지 생성 완료로 기록하지 않습니다.
- 줄바꿈·넘침과 사실 검수는 수행하지 않으며, 상태 기록에도 구분해 남깁니다.

### 별도 출력 폴더

```sh
python3 scripts/build_cardnews.py contents/2026-09-15-ai-agent --output-root /원하는/배포폴더
```

`--output-root` 아래에도 주제명/실행시각별로 저장합니다. 외부 폴더는 쓰기 권한이 필요하며, 원고 폴더와 겹치는 출력 위치는 거부합니다. 상대 경로는 명령을 실행한 현재 폴더 기준입니다.

결과물에는 기획·검수 Markdown을 복사하지 않습니다. HTML에는 이미지·CSS·로고가 포함되어 실행 폴더를 옮겨도 열 수 있습니다. `assets/`는 이번 합성에 실제 사용한 배경만 중복 없이 복사하며, 장별 대응과 원고 해시는 manifest.json에 기록합니다. 출력 성공은 배포 승인이나 시각 검수 완료가 아니며 기본 상태는 `preview_not_approved`입니다. 출처·이미지 사용 조건은 원본 작업 문서에서 관리합니다.

기존 contents/주제/output/은 과거 결과물로 보존하며 새 결과는 만들지 않습니다. 칼럼 배포용 변환은 아직 이 카드 합성 도구의 범위에 포함하지 않습니다.

### 원고 입력 규칙

기존 `templates/cardnews_template.md`를 채웁니다. 완성된 문법 예시는 [cardnews.example.md](cardnews.example.md)에 있습니다. 이 예시는 실제 트렌드 콘텐츠가 아닙니다.

- 장 제목: `## 01 — 표지`처럼 숫자와 대시를 사용합니다. 번호는 1부터 연속입니다.
- 첫 장은 `cover`, 마지막은 `cta`, 본문은 `gradient`, `split`, `overlay`입니다. 5종은 장수 제한이 아닙니다.
- 항목은 `- 제목: 문구` 형식입니다. 다음 줄을 두 칸 들여쓰면 같은 항목의 줄바꿈으로 출력합니다.
- `제목`, `본문`, `상단 보조 문구`, `보조 문구·조건·한계`, `사례 구분`, `화면용 짧은 출처`, CTA의 `보조 문구`·`CTA 링크`를 표시합니다. 링크는 카드 이미지에 맞게 텍스트로 표시합니다.
- `핵심 메시지`, `시각 자료 지시`, `관련 출처 ID` 등은 제작 참고 정보입니다. 최종 화면에는 표시하지 않습니다.
- 배경 파일이 있으면 각 장에 `- 이미지 경로: images/파일명.png`를 추가합니다. PNG·JPEG·WebP를 지원하며 해당 주제의 images 폴더 아래 파일만 사용합니다.
- 본문의 조건·한계와 가상 사례 표시는 출력에 유지합니다. 출처는 별도 `05_sources.md`에도 기록합니다.
- `{{자리표시자}}`와 중복 항목, 누락된 제목·본문, 잘못된 번호·레이아웃은 출력 전 오류로 알립니다. Markdown 강조·임의 HTML은 해석하지 않습니다.

## 3. 선택적 PNG 출력

```sh
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r scripts/requirements-render.txt
python3 -m playwright install chromium
python3 scripts/build_cardnews.py contents/2026-09-15-ai-agent --png
```

위 활성화 명령은 macOS/Linux 기준입니다. Windows는 `.venv\Scripts\activate`를 사용합니다.
PNG 옵션은 Chromium으로 장별 HTML을 1080×1350 이미지로 저장합니다. 필요한 한글 글꼴이 실행 환경에 설치되어 있어야 합니다. PNG 출력 코드는 준비했으며, 현재 환경의 실제 PNG 출력 및 시각 검수는 아직 실행하지 않았습니다. 실패하면 해당 실행의 미완성 출력 폴더를 정리합니다.

## 4. 기능 확인

```sh
python3 -m unittest discover -s scripts -p 'test_*.py'
```

작업 폴더 생성, 기존 작업 보존, 잘못된 입력, 5종 레이아웃의 HTML 생성, 문구 보존, HTML 이스케이프, 이미지 경로 제한, 출력 실패 처리를 확인합니다. 브라우저·실제 PNG·줄바꿈·넘침 검수는 이 테스트에 포함하지 않습니다.


## 제거된 API 경로

`write_content.py`, `generate_images.py`, `openai_client.py`는 제거했습니다. 이전 `--execute`, `--mode api` 명령은 더 이상 지원하지 않습니다. 과거 구현은 Git 이력에 있으며 기존 콘텐츠와 이미지 파일은 보존했습니다.

이미지 제작 지시는 `06_image_prompts.md`에 기록하고 Codex가 내장 도구에 전달합니다. 새 콘텐츠에는 별도 `image_plan.json`을 만들 필요가 없습니다. 기존 JSON은 당시 제작 기록으로 유지합니다.

## 읽기용 전체 보기
새 index.html은 최대 648px 너비의 큰 카드를 한 장씩 보여줍니다. 크게 읽기 / 모아 보기 버튼으로 전환하며 창 너비에 맞춰 비례 축소합니다. 원본 카드 규격과 개별 HTML·PNG용 CSS는 유지합니다. 이 미리보기 동작에는 JavaScript가 필요합니다.
