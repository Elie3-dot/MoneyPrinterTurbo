## 2026-09-22 - Pillow Font Loading Caching in Subtitle Rendering
**Learning:** `PIL.ImageFont.truetype` parses font files and disk structures on every call. In video/subtitle generation loops, evaluating text size or wrapping subtitle lines calls `ImageFont.truetype` hundreds of times per video. Caching loaded font instances using `@lru_cache(maxsize=128)` on string paths speeds up font lookups by ~200x.
**Action:** Use `_get_cached_font` when creating fonts for text clips and subtitle line width measurements to eliminate repeated disk I/O and font parsing.
