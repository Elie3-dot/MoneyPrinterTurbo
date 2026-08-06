import unittest
import os
import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

# Add project root to python path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from app.services.video import _get_cached_font, _load_font_cached
from app.utils import utils

class TestFontCache(unittest.TestCase):
    def setUp(self):
        # Clear LRU cache before each test to ensure reliable asserts
        _load_font_cached.cache_clear()

    def test_cache_hits_for_same_arguments(self):
        """
        Verify that multiple calls with the exact same font path and size
        hit the cache and return the exact same object, avoiding re-loading.
        """
        font_path = os.path.join(utils.font_dir(), "STHeitiMedium.ttc")

        # We mock ImageFont.truetype so we don't necessarily need the file to exist on disk
        with patch("app.services.video.ImageFont.truetype") as mock_truetype:
            mock_font_instance = MagicMock()
            mock_truetype.return_value = mock_font_instance

            font1 = _get_cached_font(font_path, 24)
            font2 = _get_cached_font(font_path, 24)

            # Assert that truetype was only called once
            mock_truetype.assert_called_once_with(font_path, 24)
            # Assert they return the exact same instance
            self.assertIs(font1, font2)

    def test_cache_miss_for_different_arguments(self):
        """
        Verify that calls with different size or path are treated as cache misses.
        """
        font_path = os.path.join(utils.font_dir(), "STHeitiMedium.ttc")

        with patch("app.services.video.ImageFont.truetype") as mock_truetype:
            mock_font_instance1 = MagicMock()
            mock_font_instance2 = MagicMock()
            mock_truetype.side_effect = [mock_font_instance1, mock_font_instance2]

            font1 = _get_cached_font(font_path, 24)
            font2 = _get_cached_font(font_path, 28)

            self.assertEqual(mock_truetype.call_count, 2)
            self.assertIsNot(font1, font2)

    def test_bypasses_cache_for_unhashable_arguments(self):
        """
        Verify that if an unhashable argument (e.g. list or unhashable file-like object)
        is passed, the cache is bypassed gracefully and it doesn't crash with TypeError.
        """
        unhashable_font = ["not-a-string-path"]

        with patch("app.services.video.ImageFont.truetype") as mock_truetype:
            mock_font_instance1 = MagicMock()
            mock_font_instance2 = MagicMock()
            mock_truetype.side_effect = [mock_font_instance1, mock_font_instance2]

            font1 = _get_cached_font(unhashable_font, 24)
            font2 = _get_cached_font(unhashable_font, 24)

            # Should not hit cache because it is unhashable, so it should be called twice
            self.assertEqual(mock_truetype.call_count, 2)
            self.assertIsNot(font1, font2)

if __name__ == "__main__":
    unittest.main()
