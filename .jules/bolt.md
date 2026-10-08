## 2025-05-20 - Caching PIL ImageFont instances in Video Service
**Learning:** Loading `ImageFont.truetype` font instances repeatedly from disk and parsing glyph structures inside subtitle wrapping and clip creation loops adds significant disk I/O and font parsing overhead (~476 ms vs ~124 ms for 500 calls).
**Action:** Wrap `ImageFont.truetype(font, size)` calls in an `@lru_cache(maxsize=128)` helper in video/subtitle generation pipelines.
