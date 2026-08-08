## 2025-08-08 - [Font cache optimization]
**Learning:** Found that when generating subtitles/videos, the app repeatedly parses and loads TTF/TTC fonts via Pillow's ImageFont.truetype inside loops or per subtitle line, leading to high disk I/O and processing overhead. Caching `ImageFont.truetype` with `@lru_cache` on string paths prevents redundant loading.
**Action:** Implemented caching for TTF/TTC font loading using standard python functools.lru_cache.
