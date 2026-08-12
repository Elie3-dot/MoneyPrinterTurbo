## 2026-10-24 - Optimized Pillow TrueType Font Loading Inside Video Generation
**Learning:** `ImageFont.truetype` inside video/subtitle generation and text wrapping loops results in repeated disk I/O and parsing of identical font files. Caching `ImageFont` instances by `(font_path, font_size)` saves significant CPU and file system overhead. Defensively wrapping the cached function with unhashable checks ensures stability regardless of input types.
**Action:** Use a decorated `@lru_cache` helper function with defensive hashability verification to cache font objects safely inside loops.
