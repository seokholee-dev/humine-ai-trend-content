"""Generate planned image assets. Default is a free dry-run; --execute calls API."""
import argparse
import base64
import hashlib
import json
from pathlib import Path
import re
from openai_client import post


def generate(topic, execute=False, max_images=4, model='gpt-image-2.5-flare'):
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
    parser.add_argument('--execute', action='store_true', help='실제 유료 API 호출')
    parser.add_argument('--max-images', type=int, default=4)
    parser.add_argument('--model', default='gpt-image-2.5-flare')
    args = parser.parse_args()
    try:
        print(json.dumps(generate(args.topic, args.execute, args.max_images, args.model), ensure_ascii=False, indent=2))
    except (ValueError, OSError, KeyError, TypeError, IndexError) as exc:
        parser.exit(1, f'이미지 생성 중단: {exc}\n')

if __name__ == '__main__':
    main()
