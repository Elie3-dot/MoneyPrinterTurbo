## 2025-05-18 - Pillow Font Loading Caching in Subtitle/Video Rendering Loop

**Learning:** MoviePy subtitle wrapping (`wrap_text`) and rounded background bounding box measurements invoke `ImageFont.truetype` on every subtitle phrase or line measurement. Re-reading and re-parsing font files (TTF/TTC) from disk takes ~0.25ms per call (~50ms for 200 calls), whereas caching `ImageFont` instances with `@lru_cache(maxsize=128)` drops the overhead to ~0.001ms per lookup (~200x speedup).

**Action:** Wrap `ImageFont.truetype` calls with a defensive cached helper (`_get_cached_font`) that uses `@lru_cache` for path strings while falling back to direct calls for unhashable input types.
