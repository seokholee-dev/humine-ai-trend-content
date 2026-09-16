"""Non-browser checks. Run: python3 -m unittest discover -s scripts -p 'test_*.py'"""
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_cardnews as renderer
from generate_content import prepare

ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = (ROOT / "scripts/cardnews.example.md").read_text(encoding="utf-8")


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        shutil.copytree(ROOT / "templates", self.root / "templates")
        shutil.copytree(ROOT / "style", self.root / "style")
        (self.root / "AGENTS.md").write_text("# Test fixture rules\n", encoding="utf-8")

    def topic(self):
        return prepare(self.root, "테스트 주제", "test-topic", "2026-09-15")

    def test_prepare_preserves_existing_work(self):
        topic = self.topic()
        self.assertTrue((topic / "00_task.md").is_file())
        self.assertFalse((topic / "03_column.md").exists())
        draft = topic / "04_cardnews.md"
        self.assertIn("테스트 주제", draft.read_text(encoding="utf-8"))
        draft.write_text("사용자 수정", encoding="utf-8")
        with self.assertRaises(ValueError):
            self.topic()
        self.assertEqual(draft.read_text(encoding="utf-8"), "사용자 수정")

    def test_invalid_input_leaves_no_topic(self):
        for slug in ("../escape", "UPPER", ""):
            with self.assertRaises(ValueError):
                prepare(self.root, "주제", slug, "2026-09-15")
        with self.assertRaises(ValueError):
            prepare(self.root, "주제", "topic", "2026-02-30")
        (self.root / "templates/research_template.md").unlink()
        with self.assertRaises(ValueError):
            self.topic()
        self.assertFalse((self.root / "contents").exists())

    def test_both_formats(self):
        topic = prepare(self.root, "주제", "both", "2026-09-15", "both")
        self.assertTrue((topic / "03_column.md").is_file())
        self.assertTrue((topic / "04_cardnews.md").is_file())

    def test_chat_image_request_and_column_only_scope(self):
        topic = prepare(self.root, "주제", "column-chat", "2026-09-16", "column", "chat")
        task = (topic / "00_task.md").read_text(encoding="utf-8")
        self.assertIn("이미지 작업: chat", task)
        self.assertIn("유료 API로 자동 전환하지", task)
        self.assertTrue((topic / "03_column.md").is_file())
        self.assertFalse((topic / "04_cardnews.md").exists())
        with self.assertRaises(ValueError):
            prepare(self.root, "주제", "invalid-mode", "2026-09-16", images="api")

    def test_chat_image_request_preserves_preparation_boundary(self):
        topic = prepare(self.root, "주제", "chat", "2026-09-16", "both", "chat")
        task = (topic / "00_task.md").read_text(encoding="utf-8")
        self.assertIn("이미지 작업: chat", task)
        self.assertIn("prompts/chat_workflow.md", task)
        self.assertFalse(list((topic / "images").glob("*.png")))
        with self.assertRaises(ValueError):
            prepare(self.root, "주제", "invalid", "2026-09-16", images="api")

    def test_parser_rejects_unfinished_or_invalid_cards(self):
        self.assertEqual(len(renderer.parse_cards(EXAMPLE)), 5)
        for invalid in (EXAMPLE.replace("overlay", "unknown"),
                        EXAMPLE.replace("## 03", "## 09"),
                        EXAMPLE.replace("변화의 의미를 읽습니다", "{{제목}}")):
            with self.assertRaises(ValueError):
                renderer.parse_cards(invalid)

    def test_html_preserves_notes_and_escapes_content(self):
        topic = self.topic()
        text = EXAMPLE.replace("변화의 의미를 읽습니다", '<script>alert("x")</script>')
        (topic / "04_cardnews.md").write_text(text, encoding="utf-8")
        result = renderer.build(topic, self.root)
        page = (result / "02.html").read_text(encoding="utf-8")
        self.assertIn("&lt;script&gt;", page)
        self.assertNotIn("<script>", page)
        self.assertIn("기능 확인용 예시입니다.", page)
        self.assertIn("가상 활용 예시", (result / "03.html").read_text(encoding="utf-8"))
        cover = (result / "01.html").read_text(encoding="utf-8")
        self.assertIn("data:image/png;base64,", cover)
        self.assertIn("AI 트렌드를<br>업무의 언어로", cover)
        manifest = json.loads((result / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["visual_review"], "deferred")
        self.assertEqual(manifest["png"], "not_requested")
        self.assertEqual(len(list(result.glob("*.html"))), 6)
        self.assertNotEqual(renderer.build(topic, self.root), result)

    def test_asset_escape_is_rejected(self):
        topic = self.topic()
        for path in ("../outside.png", "/tmp/outside.png"):
            with self.assertRaises(ValueError):
                renderer.background_uri(topic, path)

    def test_png_failure_removes_partial_build(self):
        topic = self.topic()
        (topic / "04_cardnews.md").write_text(EXAMPLE, encoding="utf-8")
        with patch.object(renderer, "export_png", side_effect=ValueError("fixture failure")):
            with self.assertRaises(ValueError):
                renderer.build(topic, self.root, png=True)
        self.assertEqual(list((topic / "output").glob("*build-*")), [])


if __name__ == "__main__":
    unittest.main()
