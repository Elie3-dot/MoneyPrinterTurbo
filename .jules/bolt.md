## 2026-10-03 - Cache Pillow `ImageFont.truetype` Instances
**Learning:** Calling Pillow's `ImageFont.truetype` inside video and subtitle creation loops parses TTF/TTC binary font headers and performs repeated disk I/O for every line or word length measurement during `wrap_text` and `create_text_clip`.
**Action:** Wrap string-based font loading in an `@lru_cache(maxsize=128)` helper (`_get_cached_font`) while defensively bypassing the cache for any unhashable arguments. This speeds up 200 font load iterations from ~104ms to ~0.5ms (~200x speedup).
