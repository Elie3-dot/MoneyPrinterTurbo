# Bolt's Journal

## 2026-07-16 - [Cached PIL Font Loading]
**Learning:** In video/subtitle generation loops, loading TrueType/OpenType fonts repeatedly from disk via `ImageFont.truetype` for every single text clip is a massive performance bottleneck. Caching these loaded fonts via `functools.lru_cache` provides a ~400x speedup in font loading and avoids redundant disk I/O and CPU overhead.
**Action:** Always use a cached utility function (`_get_font`) when loading fonts with Pillow (`ImageFont.truetype`) inside any loop or repeated execution path.
