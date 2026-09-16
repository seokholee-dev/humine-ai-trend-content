# 콘텐츠 제작 실행 파일

Python 3.9 이상을 사용합니다. 명령은 저장소를 내려받은 뒤 저장소 루트에서 실행합니다.
작업 폴더 준비와 HTML 생성은 추가 패키지나 API 키 없이 실행할 수 있습니다.

## 권장: 현재 대화에서 원고와 이미지까지

```sh
python3 scripts/generate_content.py --topic "AI 에이전트와 업무" --slug ai-agent --format both --images chat
```

생성된 `00_task.md`를 현재 대화에서 실행해 달라고 요청하면 됩니다. [대화 실행 지침](../prompts/chat_workflow.md)에 따라 Codex가 웹 조사·원고 작성·이미지 도구 실행을 진행합니다. 스크립트 자체는 작업 준비만 수행합니다. 별도 API 키는 필요하지 않으며 이미지 도구의 제공 여부·한도는 현재 환경에 따릅니다. 기본 `--images plan`은 기획까지만 요청합니다.

이미지 기획 후 `image_plan.json`이 있으면 다음으로 도구용 요청을 확인합니다.

```sh
python3 scripts/generate_images.py contents/생성된-폴더
```

기본 `--mode chat`은 API 호출 없이 요청을 출력합니다. 실제 생성은 대화 도구로 수행하고, 결과 파일을 `images/`에 저장·연결한 후 기존 합성 도구로 HTML을 만듭니다. 최종 카드 PNG는 별도 렌더링 단계입니다. 도구가 결과 파일을 로컬로 전달하지 못하면 저장·합성은 미완료로 기록합니다.

## 1. 주제 작업 폴더 준비

```sh
python3 scripts/generate_content.py --topic "AI 에이전트와 업무" --slug ai-agent --date 2026-09-15 --format cardnews
```

`contents/2026-09-15-ai-agent/`에 `00_task.md`, 리서치·Core Brief·카드뉴스·출처·이미지 기획·검수 양식과 `images/`, `output/`을 생성합니다. `--format both`는 칼럼도 추가하고 `column`은 칼럼용으로 준비합니다. 날짜 생략 시 실행일을 사용합니다. 같은 폴더가 있으면 덮어쓰지 않고 중단합니다.

**generate_content.py는 작업 준비 도구입니다. AI 호출이나 사실 조사 자체를 실행하지 않습니다.** 생성된 `00_task.md`의 요청을 Codex에 전달해 저장소 규칙에 따른 원고 작성을 진행하세요. 별도 API 방식은 아래 5절을 참조하세요.

## 2. 작성된 카드뉴스를 HTML로 출력

```sh
python3 scripts/build_cardnews.py contents/2026-09-15-ai-agent
```

`04_cardnews.md`를 읽어 `output/build-실행시각/`에 장별 `01.html`부터 마지막 장까지, 전체 보기 `index.html`, 상태 기록 `manifest.json`을 저장합니다. 매번 새 폴더를 만들므로 이전 출력은 보존됩니다.

- 기존 `style/cardnews.css`의 1080×1350, padding, 글자 위치를 사용합니다.
- 사용자 제공 투명 Data Diving 로고와 축소된 로고 크기를 적용합니다.
- CSS와 로고·배경을 HTML 안에 포함해 출력 파일을 옮겨도 연결이 유지됩니다.
- 배경이 없으면 임시 색상 배경을 사용합니다. 이미지 생성 완료로 기록하지 않습니다.
- 줄바꿈·넘침과 사실 검수는 수행하지 않으며, 상태 기록에도 구분해 남깁니다.

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

## 5. OpenAI API 연결 (기본은 무료 실행 계획 확인)

`write_content.py`는 웹 검색 후 리서치를 기반으로 Core Brief·칼럼·7장 카드뉴스·출처·이미지 계획을 새 주제 폴더에 생성합니다. 기본 모델은 `gpt-5.4-mini`이며 `--model`로 변경합니다. 출력은 검수 전 초안입니다. 실제 검색 응답·출처 주석과 사용량도 보존합니다.

```sh
python3 scripts/write_content.py --topic "AI 에이전트와 기업 업무"
```

위 명령은 API 호출 없이 계획만 확인합니다. 실제 호출은 키를 설정한 환경에서 `--execute`를 명시해야 합니다. **ChatGPT 구독과 API 요금은 별도입니다.** 웹 검색·텍스트·이미지 호출마다 비용이 발생할 수 있습니다. 현재 실계정 유료 호출은 검증하지 않았습니다.

키는 `OPENAI_API_KEY` 환경 변수로 전달합니다. 키를 원고, GitHub, 채팅에 기록하지 마세요. `.env` 자동 로딩은 하지 않습니다. 다음은 macOS/Linux에서 값을 화면에 표시하지 않고 입력하는 방법입니다.

```sh
read -s OPENAI_API_KEY
export OPENAI_API_KEY
python3 scripts/write_content.py --topic "AI 에이전트와 기업 업무" --execute
```

표시된 주제 폴더의 `image_plan.json`을 검토한 뒤 이미지 생성 계획을 확인합니다.

```sh
python3 scripts/generate_images.py contents/생성된-폴더 --mode api
# 아래 명령부터 이미지 API 비용 발생
python3 scripts/generate_images.py contents/생성된-폴더 --mode api --execute
python3 scripts/build_cardnews.py contents/생성된-폴더
```

이미지 모델 기본값은 `gpt-image-2.5-flare`, 기본 호출 상한은 계획당 4개입니다. 상한은 비용 금액 상한이 아닙니다. 자동 유료 재시도는 하지 않습니다. 성공한 동일 계획의 이미지는 재사용하고, 프롬프트나 모델을 바꿀 때는 새 자산 ID를 사용해 원본을 보존합니다. 카드 원고에 기록된 이미지 경로와 계획 ID가 연결됩니다. 이미지 생성 후 사실·구도 확인과 보류 중인 시각 검수는 별도로 진행합니다.

API 키가 없거나 계정에 해당 모델 권한이 없으면 실제 생성은 실행되지 않습니다. 일부 호출 성공 후 실패할 수 있으므로 실패 시에도 사용량을 확인하세요. 원고 생성의 후속 단계 실패 시 성공한 리서치는 `-failed` 폴더에 보존합니다.

공식 문서: [Responses](https://developers.openai.com/api/docs/guides/text) · [이미지 생성](https://developers.openai.com/api/docs/guides/image-generation)
