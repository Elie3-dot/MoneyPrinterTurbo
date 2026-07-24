## 2023-11-23 - Pillow (PIL) font loading inside video/subtitle generation loops
**Learning:** Pillow's `ImageFont.truetype` loads and parses the font files from disk repeatedly during text wrapping or subtitle box measurement calculations. For large font files (such as Chinese TTC/TTF fonts), doing this in a loop for each subtitle can lead to significant disk I/O and CPU overhead.
**Action:** Always cache font instances loaded via PIL using a helper function wrapped in `@lru_cache(maxsize=128)` when font files are accessed repetitively with identical font paths and sizes in hot paths.
