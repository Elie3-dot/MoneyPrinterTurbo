## 2025-01-01 - [Font Caching Optimization]
**Learning:** Pillow (PIL) font loading with ImageFont.truetype inside video/subtitle generation loops can cause significant disk I/O and parsing overhead. Caching these font instances using functools.lru_cache optimizes performance significantly.
**Action:** Implement `lru_cache` for ImageFont.truetype font loaders.
