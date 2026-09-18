## 2026-09-18 - Pillow Font Instance Caching in Video Generation
**Learning:** Pillow (`PIL.ImageFont.truetype`) re-opens and parses TrueType/OpenType font files on every call. In video generation loops that process each subtitle line, text wrapping (`wrap_text`) and width measurements repeatedly invoke `ImageFont.truetype`, incurring unnecessary file I/O and TTF table parsing (~100x slower per font lookup).
**Action:** Always wrap `ImageFont.truetype` calls in a helper function (`_get_cached_font`) backed by `@lru_cache(maxsize=128)` when rendering text or subtitles in loops.
