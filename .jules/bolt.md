## 2026-06-18 - PIL ImageFont caching
**Learning:** In the video/subtitle generation loops, Pillow (PIL) font loading with `ImageFont.truetype` causes redundant disk I/O and parsing overhead because the same font file and font size are loaded repeatedly for every text/subtitle chunk. Wrapping font loading with `@lru_cache` greatly improves performance.
**Action:** Use a cached font loading helper `_get_cached_font` to reuse `ImageFont.truetype` instances.
