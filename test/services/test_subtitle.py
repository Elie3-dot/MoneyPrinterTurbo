import sys
import tempfile
import unittest
from pathlib import Path

# 测试文件直接运行时，也能从仓库根目录导入 app 包。
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from app.services import subtitle
from app.utils import utils


class TestUtilsPunctuation(unittest.TestCase):
    def test_str_contains_punctuation(self):
        self.assertTrue(utils.str_contains_punctuation("hello,"))
        self.assertTrue(utils.str_contains_punctuation("world!"))
        self.assertTrue(utils.str_contains_punctuation("测试。"))
        self.assertFalse(utils.str_contains_punctuation("hello"))
        self.assertFalse(utils.str_contains_punctuation("12345"))

    def test_split_string_by_punctuations(self):
        text = "Hello world! How are you? Withdraw 10,000, charged at 2.5% fee."
        expected = [
            "Hello world",
            "How are you",
            "Withdraw 10,000",
            "charged at 2.5% fee",
        ]
        self.assertEqual(utils.split_string_by_punctuations(text), expected)

    def test_split_string_by_punctuations_cjk(self):
        text = "床前明月光，疑是地上霜。举头望明月，低头思故乡。"
        expected = [
            "床前明月光",
            "疑是地上霜",
            "举头望明月",
            "低头思故乡",
        ]
        self.assertEqual(utils.split_string_by_punctuations(text), expected)

    def test_root_dir(self):
        self.assertTrue(Path(utils.root_dir()).exists())
        self.assertEqual(utils.root_dir(), utils.root_dir())


class TestSubtitleService(unittest.TestCase):
    def test_correct_ignores_markdown_separator_lines(self):
        """
        Whisper fallback 校正阶段也必须忽略 `---` 这类不可发声脚本行。

        如果这里继续保留 Markdown 分隔符，`correct()` 会认为脚本行数多于
        字幕行数，并补出 `00:00:00,000 --> 00:00:00,000`，剪辑软件会把
        生成的 SRT 判定为不可导入。
        """
        original_srt = (
            "1\n"
            "00:00:00,100 --> 00:00:01,000\n"
            "第一段\n\n"
            "2\n"
            "00:00:01,100 --> 00:00:02,000\n"
            "第二段\n\n"
        )

        with tempfile.TemporaryDirectory() as tmp_dir:
            subtitle_file = Path(tmp_dir) / "subtitle.srt"
            subtitle_file.write_text(original_srt, encoding="utf-8")

            subtitle.correct(
                subtitle_file=str(subtitle_file),
                video_script="第一段\n---\n第二段",
            )

            corrected_srt = subtitle_file.read_text(encoding="utf-8")

        self.assertIn("第一段", corrected_srt)
        self.assertIn("第二段", corrected_srt)
        self.assertNotIn("---", corrected_srt)
        self.assertNotIn("00:00:00,000 --> 00:00:00,000", corrected_srt)

    def test_file_to_subtitles_keeps_last_block_without_trailing_newline(self):
        """
        The final subtitle must be parsed even when the SRT file does not end
        with a trailing blank line. Many tools omit it, and previously the last
        block was silently dropped because only a blank line flushed a block.
        """
        srt_without_trailing_blank = (
            "1\n"
            "00:00:00,000 --> 00:00:01,000\n"
            "Hello\n\n"
            "2\n"
            "00:00:01,000 --> 00:00:02,000\n"
            "World"
        )

        with tempfile.TemporaryDirectory() as tmp_dir:
            subtitle_file = Path(tmp_dir) / "subtitle.srt"
            subtitle_file.write_text(srt_without_trailing_blank, encoding="utf-8")

            items = subtitle.file_to_subtitles(str(subtitle_file))

        self.assertEqual(len(items), 2)
        self.assertEqual(items[0][2], "Hello")
        self.assertEqual(items[1][2], "World")

    def test_file_to_subtitles_parses_blocks_with_trailing_newline(self):
        """A normal SRT ending in a blank line still parses all blocks."""
        srt_with_trailing_blank = (
            "1\n"
            "00:00:00,000 --> 00:00:01,000\n"
            "Hello\n\n"
            "2\n"
            "00:00:01,000 --> 00:00:02,000\n"
            "World\n\n"
        )

        with tempfile.TemporaryDirectory() as tmp_dir:
            subtitle_file = Path(tmp_dir) / "subtitle.srt"
            subtitle_file.write_text(srt_with_trailing_blank, encoding="utf-8")

            items = subtitle.file_to_subtitles(str(subtitle_file))

        self.assertEqual([item[2] for item in items], ["Hello", "World"])


if __name__ == "__main__":
    unittest.main()
