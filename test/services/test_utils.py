import os
import unittest
from pathlib import Path

from app.utils import utils


class TestUtils(unittest.TestCase):
    def test_root_dir(self):
        root = utils.root_dir()
        self.assertTrue(os.path.isabs(root))
        self.assertTrue(os.path.isdir(root))
        # Ensure it matches expected root containing app and test directories
        self.assertTrue((Path(root) / "app").is_dir())
        self.assertTrue((Path(root) / "test").is_dir())

    def test_str_contains_punctuation(self):
        self.assertFalse(utils.str_contains_punctuation("hello"))
        self.assertFalse(utils.str_contains_punctuation("helloworld123"))
        self.assertTrue(utils.str_contains_punctuation("hello!"))
        self.assertTrue(utils.str_contains_punctuation("what?"))
        self.assertTrue(utils.str_contains_punctuation("你好，世界"))
        self.assertTrue(utils.str_contains_punctuation("مرحبا،"))
        self.assertTrue(utils.str_contains_punctuation("test..."))

    def test_split_string_by_punctuations(self):
        self.assertEqual(utils.split_string_by_punctuations(""), [])
        self.assertEqual(utils.split_string_by_punctuations("   "), [])

        text = "Hello world! This is a test. Another sentence? Yes; absolutely!"
        expected = [
            "Hello world",
            "This is a test",
            "Another sentence",
            "Yes",
            "absolutely",
        ]
        self.assertEqual(utils.split_string_by_punctuations(text), expected)

    def test_split_string_preserves_numbers_with_period_and_comma(self):
        text = "Withdraw 10,000, charged at 2.5% fee! It takes 1,000 years."
        expected = [
            "Withdraw 10,000",
            "charged at 2.5% fee",
            "It takes 1,000 years",
        ]
        self.assertEqual(utils.split_string_by_punctuations(text), expected)

    def test_split_string_handles_newlines_and_arabic(self):
        text = "مرحبا بالعالم،\nكيف حالك؟ هذا اختبار؛ يعمل بشكل جيد."
        expected = [
            "مرحبا بالعالم",
            "كيف حالك",
            "هذا اختبار",
            "يعمل بشكل جيد",
        ]
        self.assertEqual(utils.split_string_by_punctuations(text), expected)


if __name__ == "__main__":
    unittest.main()
