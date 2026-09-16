"""Small standard-library client; never retries billable requests automatically."""
import json
import os
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError


def post(endpoint, payload):
    key = os.environ.get('OPENAI_API_KEY', '').strip()
    if not key:
        raise ValueError('OPENAI_API_KEY가 없습니다. 키는 채팅이나 저장소에 넣지 마세요.')
    if endpoint not in {'responses', 'images/generations'}:
        raise ValueError('지원하지 않는 API 경로')
    request = Request('https://api.openai.com/v1/' + endpoint,
                      data=json.dumps(payload).encode(),
                      headers={'Authorization': 'Bearer ' + key, 'Content-Type': 'application/json'})
    try:
        with urlopen(request, timeout=240) as response:
            return json.load(response)
    except HTTPError as exc:
        raise ValueError(f'OpenAI HTTP {exc.code}: 결제·모델 권한·요청 설정을 확인하세요. 자동 재시도하지 않았습니다.') from None
    except (URLError, TimeoutError) as exc:
        raise ValueError('API 응답을 확인하지 못했습니다. 중복 과금을 피하려면 사용 내역 확인 후 재시도하세요.') from None


def output_text(response):
    if response.get('status') != 'completed':
        raise ValueError('응답이 완료되지 않았습니다. 생성 결과를 최종본으로 저장하지 않습니다.')
    result = '\n'.join(c['text'] for item in response.get('output', [])
                       if item.get('type') == 'message' for c in item.get('content', [])
                       if c.get('type') == 'output_text')
    if not result.strip():
        raise ValueError('텍스트 응답이 없습니다.')
    return result
