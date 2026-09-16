import base64
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import generate_images as images
from openai_client import output_text, post

class ApiTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)
        (self.root/'image_plan.json').write_text(json.dumps({'assets':[{'id':'hero','prompt':'office scene'}]}))
    def test_dry_run_does_not_call_api(self):
        with patch.object(images,'post') as call:
            self.assertEqual(images.generate(self.root)[0]['status'],'planned')
            call.assert_not_called()
    def test_success_reuses_and_changed_prompt_preserves_asset(self):
        png=b'\x89PNG\r\n\x1a\nfixture'
        with patch.object(images,'post',return_value={'data':[{'b64_json':base64.b64encode(png).decode()}]}) as call:
            self.assertEqual(images.generate(self.root,True)[0]['status'],'generated')
            self.assertEqual(images.generate(self.root,True)[0]['status'],'reused')
            self.assertEqual(call.call_count,1)
            with self.assertRaises(ValueError): images.generate(self.root,True,model='different')
        self.assertEqual((self.root/'images/hero.png').read_bytes(),png)
    def test_limit_and_path_rejected_before_call(self):
        with patch.object(images,'post') as call:
            with self.assertRaises(ValueError): images.generate(self.root,True,max_images=0)
            (self.root/'image_plan.json').write_text(json.dumps({'assets':[{'id':'../escape','prompt':'x'}]}))
            with self.assertRaises(ValueError): images.generate(self.root,True)
            call.assert_not_called()
    def test_missing_key_stops_network(self):
        with patch.dict('os.environ',{},clear=True), patch('openai_client.urlopen') as network:
            with self.assertRaises(ValueError): post('responses',{})
            network.assert_not_called()
    def test_incomplete_text_is_not_saved(self):
        with self.assertRaises(ValueError): output_text({'status':'incomplete','output':[]})
        self.assertEqual(output_text({'status':'completed','output':[{'type':'message','content':[{'type':'output_text','text':'완료'}]}]}),'완료')
if __name__=='__main__': unittest.main()
