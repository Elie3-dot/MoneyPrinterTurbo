## 2026-10-25 - Pillow Font Loading Caching in Video Subtitle Generation

**Learning:** Calling `ImageFont.truetype()` inside video/subtitle generation loops repeatedly opens and parses TTF/TTC font files on disk, introducing significant disk I/O and CPU parsing overhead during subtitle layout and word wrapping (~300x speedup when cached).
**Action:** Always wrap `ImageFont.truetype()` calls with a string-path `@lru_cache` helper (`_get_cached_font`) when rendering text or measuring bounds repeatedly across video frame or subtitle cue loops.
