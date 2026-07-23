## 2024-03-31 - [Initial Entry]
**Learning:** Virtual environment has been successfully configured and tests run smoothly using `uv run python -m pytest`. `storage/temp` has been verified to exist.
**Action:** Always verify with local test run.

## 2024-03-31 - [Cached Pillow Font Loading]
**Learning:** Under video/subtitle generation loops, Pillow's `ImageFont.truetype` is repeatedly called to load and parse font files from disk for measuring and drawing text. Caching the `ImageFont` instances with `@lru_cache` eliminates redundant disk I/O and font-parsing overhead.
**Action:** Always check loop constructs that parse resources/files, and cache them with `lru_cache` or a global dictionary where safe to do so.
