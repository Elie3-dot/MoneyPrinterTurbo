## 2026-07-17 - [Cache PIL Font loading to reduce disk I/O]
**Learning:** Pillow (PIL) font loading with ImageFont.truetype inside loops can cause significant disk I/O and parsing overhead. Caching these font instances using `functools.lru_cache` optimizes subtitle rendering performance significantly.
**Action:** Use a cached font retrieval helper `_get_font` decorated with `@lru_cache(maxsize=128)` instead of calling `ImageFont.truetype` directly.
