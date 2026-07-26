# Bolt's Journal

## 2024-11-20 - Subtitle Generation Font Caching
**Learning:** Found that pillow's `ImageFont.truetype` inside subtitle and video generation loops parses and performs disk I/O repeatedly for the same font file, causing severe overhead during bulk rendering of subtitle frames. Caching `ImageFont.truetype` instances prevents redundant disk IO and font object parsing overhead.
**Action:** Created `_get_cached_font` with `@lru_cache` in `app/services/video.py`.
