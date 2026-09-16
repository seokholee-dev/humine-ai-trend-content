"""Prepare chat image tasks by default; API calls require --mode api --execute."""
import argparse
import base64
import hashlib
import json
from pathlib import Path
import re
from openai_client import post


def read_assets(topic, max_images):
    topic = Path(topic).resolve()
    plan = json.loads((topic / 'image_plan.json').read_text(encoding='utf-8'))
    assets = plan['assets']
    if not isinstance(assets, list) or not 1 <= len(assets) <= max_images:
        raise ValueError('이미지 계획 수가 비어 있거나 호출 상한을 초과합니다.')
    ids = set()
    for asset in assets:
        if not re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*', asset['id']) or asset['id'] in ids:
            raise ValueError('이미지 ID가 잘못되었거나 중복됩니다.')
        ids.add(asset['id'])
        if not isinstance(asset['prompt'], str) or not asset['prompt'].strip():
            raise ValueError('이미지 프롬프트가 비어 있습니다.')
    return assets


def chat_tasks(topic, max_images=4):
    topic = Path(topic).resolve()
    assets = read_assets(topic, max_images)
    return {
        'mode': 'chat', 'status': 'planned', 'api_called': False,
        'instructions': '현재 대화의 이미지 생성 도구로 생성하세요. Python은 도구를 호출하지 않습니다. '
            '생성 결과를 확인하고 images/에 저장한 뒤 원고에 실제 경로를 연결하세요. '
            '기존 파일은 덮어쓰지 마세요. 로컬 저장 불가 시 저장 미완료로 기록하세요. '
            '유료 API로 자동 전환하지 마세요. 줄바꿈·넘침 검수는 보류합니다.',
        'assets': [dict(id=a['id'], prompt=a['prompt'] +
            '\nNo lettering, captions, logos, watermarks, or imitation product UI. Keep the designated text area simple.',
            planned_path='images/' + a['id'] + '.png') for a in assets],
    }


def generate(topic, execute=False, max_images=4, model='gpt-image-2.5-flare'):
    topic = Path(topic).resolve()
    assets = read_assets(topic, max_images)
    directory = topic / 'images'
    if directory.is_symlink():
        raise ValueError('images 심볼릭 링크는 사용할 수 없습니다.')
    directory.mkdir(exist_ok=True)
    manifest_path = directory / 'manifest.json'
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    report = []
    for asset in assets:
        prompt = asset['prompt'] + '\nNo lettering, captions, logos, watermarks, or imitation product UI. Keep the designated text area simple.'
        payload = dict(model=model, prompt=prompt, n=1, quality='medium', size='1024x1536', output_format='png')
        signature = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
        dest = directory / (asset['id'] + '.png')
        if dest.exists():
            prior = manifest.get(asset['id'], {})
            actual = hashlib.sha256(dest.read_bytes()).hexdigest()
            if prior.get('signature') != signature or prior.get('sha256') != actual:
                raise ValueError('기존 이미지와 계획이 다릅니다. 새 ID로 계획해 기존 자산을 보존하세요.')
            report.append({'id':asset['id'], 'status':'reused'})
            continue
        if not execute:
            report.append({'id':asset['id'], 'status':'planned', 'model':model})
            continue
        response = post('images/generations', payload)
        data = base64.b64decode(response['data'][0]['b64_json'], validate=True)
        if not data.startswith(b'\x89PNG\r\n\x1a\n'):
            raise ValueError('PNG 응답이 아닙니다.')
        with dest.open('xb') as f:
            f.write(data)
        manifest[asset['id']] = dict(signature=signature, sha256=hashlib.sha256(data).hexdigest(),
            model=model, prompt=prompt, path='images/'+dest.name, status='generated',
            visual_review='not_performed', usage=response.get('usage'))
        temp = directory / 'manifest.tmp'
        temp.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
        temp.replace(manifest_path)
        report.append({'id':asset['id'], 'status':'generated'})
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('topic', type=Path)
    parser.add_argument('--mode', choices=('chat', 'api'), default='chat',
                        help='기본 chat: 대화 도구용 요청 출력 / api: 별도 API 사용')
    parser.add_argument('--execute', action='store_true', help='실제 유료 API 호출')
    parser.add_argument('--max-images', type=int, default=4)
    parser.add_argument('--model', default='gpt-image-2.5-flare')
    args = parser.parse_args()
    if args.mode == 'chat' and args.execute:
        parser.error('--execute는 --mode api와 함께 사용하세요. chat 모드는 대화에서 실행합니다.')
    try:
        result = (chat_tasks(args.topic, args.max_images) if args.mode == 'chat'
                  else generate(args.topic, args.execute, args.max_images, args.model))
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (ValueError, OSError, KeyError, TypeError, IndexError) as exc:
        parser.exit(1, f'이미지 생성 중단: {exc}\n')

if __name__ == '__main__':
    main()
