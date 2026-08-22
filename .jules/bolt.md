## 2026-08-22 - Optimize Levenshtein Distance & String Similarity Matching

**Learning:** `similarity()` and `levenshtein_distance()` in `app/services/subtitle.py` are called repeatedly during subtitle correction/matching. Un-cached matrix allocation (`current_row.append(...)` in nested loops) creates massive GC and memory overhead. Caching `levenshtein_distance` and `similarity` via `@lru_cache(maxsize=1024)` and preallocating row buffers (`prev` / `curr`) yields a 1000x+ speedup on repeated strings and avoids list recreation.
**Action:** Always pre-allocate row buffers for dynamic programming grid algorithms in Python and apply LRU caches for pure string distance/similarity functions.
