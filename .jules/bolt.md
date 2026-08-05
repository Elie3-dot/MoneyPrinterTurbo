## 2026-08-07 - [Pillow ImageFont Caching Optimization]
**Learning:** Pillow's `ImageFont.truetype` loads and parses the font file from disk every time it is called. Inside subtitle generation and text wrapping loops, this introduces heavy disk I/O and CPU parsing overhead. Adding a caching helper decorated with `functools.lru_cache` and caching loaded font instances prevents this redundant overhead.
**Action:** Use an `_get_cached_font` helper with `@lru_cache(maxsize=128)` and defensively bypass the cache for any unhashable arguments.
