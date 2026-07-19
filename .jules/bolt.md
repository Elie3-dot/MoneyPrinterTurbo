# Bolt's Journal - Critical Learnings Only

## 2026-07-19 - PIL ImageFont.truetype Caching Optimization
**Learning:** In video subtitle generation, Pillow's `ImageFont.truetype` is loaded repeatedly during loops or text processing. Since font loading involves disk I/O and parsing, caching font instances via `lru_cache` yields significant performance speedups when processing subtitles.
**Action:** Use an `lru_cache` decorated helper to load/cache `ImageFont.truetype` objects with keys based on `(font_path, font_size)`.
