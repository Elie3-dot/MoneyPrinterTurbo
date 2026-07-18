## 2025-02-18 - PIL ImageFont Caching
**Learning:** Pillow (PIL) font loading with ImageFont.truetype inside video/subtitle generation loops causes significant disk I/O and parsing overhead. Caching these font instances using `functools.lru_cache` optimizes font resolution performance significantly, avoiding repeated parsing and disk access.
**Action:** Always cache loaded font instances via `functools.lru_cache` when rendering subtitles or text wraps in video generation pipelines.
