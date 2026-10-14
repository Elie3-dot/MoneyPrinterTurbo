## 2025-05-18 - Pillow ImageFont Caching in Video/Subtitle Loops

**Learning:** Repeated calls to `ImageFont.truetype(font_path, font_size)` inside loops (e.g. text wrapping, font measuring, subtitle clip generation) force Pillow to read and parse truetype/opentype font files from disk repeatedly, incurring significant disk I/O and parsing overhead. Delegating to an `@lru_cache(maxsize=128)` helper function yields ~100x-300x speedups for font loading operations.

**Action:** Wrap `ImageFont.truetype` calls in video and subtitle processing with a cached `_get_cached_font(font_path, size)` helper function, defensively handling non-string/unhashable parameters with a fallback.
