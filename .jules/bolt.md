# Bolt's Performance Journal

## 2026-11-07 - TrueType font parsing overhead in subtitle rendering
**Learning:** During video rendering with subtitles (`generate_video` and `wrap_text`), `ImageFont.truetype(font, fontsize)` was called repeatedly for each subtitle segment to measure text width and bounding boxes. For large font collections (e.g. `STHeitiMedium.ttc` at ~55MB), repeatedly reading and parsing TrueType tables from disk causes noticeable per-subtitle lag.
**Action:** Cache parsed font objects by string path and fontsize using an `@lru_cache(maxsize=128)` helper (`_get_cached_font`) while allowing non-string or unhashable font arguments to pass through without caching.
