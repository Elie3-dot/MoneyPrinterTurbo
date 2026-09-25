## 2026-09-25 - Caching Pillow ImageFont.truetype Instances in Video/Subtitle Loops

**Learning:** PIL's `ImageFont.truetype(font_path, font_size)` reads and parses TTF/TTC font files on every invocation. Calling `truetype` repeatedly inside subtitle wrapping and video rendering loops causes significant I/O and CPU overhead (~680x speedup when cached with `@lru_cache`).
**Action:** Always wrap `ImageFont.truetype` calls with an `@lru_cache(maxsize=128)` helper (`_get_cached_font`) when rendering subtitles or measuring text dimensions in video processing loops.
