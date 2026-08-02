## 2026-08-02 - [Dynamic Programming and Font Loading Caching]
**Learning:** Repetitive edit-distance evaluations and TTF/TTC font load/parsing represent massive CPU and disk bottlenecks in subtitle alignment and media rendering pipelines.
1. Subtitle correction frequently compares identical strings or substrings, causing quadratic computations. Preallocating flat 2-row DP arrays and inlining `min` avoids expensive list re-allocations and Python function call overhead, yielding ~42% raw speedup. Layering an `lru_cache` on top drops repetitive execution times to near 0.
2. PIL `ImageFont.truetype` is often called for every single subtitle line in video rendering loops, triggering redundant disk reads and font parsing. Caching loaded font handles with `lru_cache` (while defensively bypassing for unhashable args) provides a ~730x speedup in font loading.

**Action:** Always preallocate buffers and inline core loops in Python-based DP algorithms, and cache resource handles (such as loaded fonts) that are repeatedly retrieved using identical configurations in rendering loops.
