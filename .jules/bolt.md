## 2026-07-31 - [Optimize PIL font loading in video/subtitle generation loops]
**Learning:** Instantiating `ImageFont.truetype` on every single iteration inside loops (e.g. text layout or sub-clip generation) introduces significant file system I/O and font file parsing overhead. Caching these with `@lru_cache(maxsize=128)` speeds up execution. Unhashable parameters should be bypassed defensively.
**Action:** Use a caching helper function `_get_cached_font` delegated to an `@lru_cache` implementation to retrieve truetype fonts in the video and subtitle loops.
