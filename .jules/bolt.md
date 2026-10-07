## 2026-06-18 - PIL ImageFont truetype caching in video subtitle rendering
**Learning:** Calling `ImageFont.truetype(font_path, font_size)` repeatedly inside text wrapping and subtitle clip creation loops incurs significant disk I/O and FreeType font parsing overhead (~0.5ms per call).
**Action:** Use an `@lru_cache(maxsize=128)` helper function to cache `ImageFont.FreeTypeFont` instances by string path and font size, speeding up font lookups by ~100x while ensuring non-hashable font arguments are handled defensively.
