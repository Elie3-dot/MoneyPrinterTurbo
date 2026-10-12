## 2025-02-18 - PIL ImageFont Caching in Video Generation
**Learning:** `ImageFont.truetype` performs disk I/O and TTF/TTC file parsing on every call. In video text processing loops (such as text wrapping and bounding box measurements for each subtitle line), calling `ImageFont.truetype` directly creates a major CPU and disk I/O bottleneck (~300x slower compared to cached instances).
**Action:** Always wrap `ImageFont.truetype` calls in video rendering loops with an `@lru_cache` helper function (`_get_cached_font`), and defensively handle unhashable parameters like file-like streams.
