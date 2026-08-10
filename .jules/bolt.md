# Bolt Journal

## 2025-02-14 - Pillow ImageFont Loading Overhead in Subtitle Rendering
**Learning:** During video and subtitle generation, functions like text wrapping (`wrap_text`) and text clip creation (`create_text_clip`) are executed repeatedly for each subtitle cue/segment. Standard calls to `ImageFont.truetype(font_path, font_size)` load and parse the font file from disk every single time. This introduces substantial disk I/O and CPU parsing overhead, especially with large font files (such as CJK fonts like `STHeitiMedium.ttc` or `MicrosoftYaHeiNormal.ttc`).
**Action:** Always cache loaded `ImageFont` instances using `@lru_cache` and ensure a defensive fallback wrapper handles potential `TypeError` (for unhashable font arguments like file streams) to prevent redundant loads and I/O bottleneck in rendering loops.
