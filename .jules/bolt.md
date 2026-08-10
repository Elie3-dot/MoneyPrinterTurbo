# Bolt's Journal

## 2026-08-10 - Pillow (PIL) Font Loading Bottleneck in Subtitle Generation Loops
**Learning:** In video rendering pipelines with subtitle overlays, generating subtitle clips and text-wrapping involves measuring text width and height repeatedly (often twice or more per subtitle block). Loading the TrueType/OpenType font file from disk and parsing it via `ImageFont.truetype(...)` inside loops of dozens or hundreds of subtitle items introduces severe, redundant disk I/O and parsing overhead, particularly with large CJK font packages. Caching font instances using `lru_cache` based on the path and size parameters completely eliminates this bottleneck.
**Action:** Always use a cached font helper (like `_get_cached_font`) rather than directly calling `ImageFont.truetype(...)` in hot paths such as loop iterations, text measurement, or clip creation. Bypassing the cache defensively for any unhashable arguments avoids exceptions if a file-like object is passed.
