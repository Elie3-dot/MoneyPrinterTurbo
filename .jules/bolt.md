# Bolt Optimization Journal

## 2025-02-15 - Pillow Font Loading Performance Optimization
**Learning:** Pillow's (PIL) font loading `ImageFont.truetype` inside video/subtitle generation loops can cause significant disk I/O and parsing overhead. Caching these font instances using `functools.lru_cache` optimizes performance significantly.
**Action:** Implement `lru_cache` decoration for font loading in video/subtitle processing pipeline.
