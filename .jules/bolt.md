## 2026-06-18 - Pillow Font Loading Optimization in Video Service
**Learning:** `PIL.ImageFont.truetype` reads and parses font files (TTF/TTC) from disk on every invocation. When called inside subtitle wrapping and text width measurement loops for each subtitle item, this introduces hundreds of redundant disk reads and font table parsing operations.
**Action:** Wrap `ImageFont.truetype` with `@lru_cache(maxsize=128)` via a helper function (`_get_cached_font`) whenever fonts are loaded repeatedly during video/subtitle rendering.
