## 2025-05-18 - PIL ImageFont caching in video subtitle rendering
**Learning:** `ImageFont.truetype` parses TrueType/OpenType font files and font tables from disk on every invocation. In subtitle rendering and text wrapping loops, calling `ImageFont.truetype` repeatedly for each subtitle segment or word length measurement introduces significant disk I/O and parsing overhead (~0.5ms vs ~0.005ms per lookup, >100x speedup).
**Action:** Wrap `ImageFont.truetype` with `@lru_cache` for immutable font path and size arguments in rendering loops.
