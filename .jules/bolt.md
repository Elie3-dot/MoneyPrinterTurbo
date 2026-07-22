## 2026-07-22 - [Pillow Font Loading Optimization]
**Learning:** Instantiating `ImageFont.truetype` inside subtitle word wrapping or layout calculations introduces significant file I/O and font parsing overhead when executed on every text wrap check or frame. Caching these `FreeTypeFont` objects drastically speeds up subtitle rendering.
**Action:** Use an `lru_cache` helper function like `_get_cached_font` to look up or cache font objects instead of instantiating `ImageFont.truetype` directly.
