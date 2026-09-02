## 2026-09-02 - Optimize Levenshtein distance calculation in subtitle service

**Learning:** During subtitle correction (`correct()` in `app/services/subtitle.py`), `similarity()` repeatedly computes Levenshtein distances for candidate subtitle line mergers. The default algorithm created new list buffers (`current_row = [i + 1]`) and executed `list.append()` inside nested loops for every character pair, incurring high allocation and GC overhead. Pre-allocating two flat DP row buffers, swapping references (`previous_row, current_row = current_row, previous_row`), and caching comparisons via `@lru_cache(maxsize=1024)` improved uncached execution speed by ~1.8x and cached execution speed by >10,000x.

**Action:** When performing dynamic programming string matching on hot execution paths, use pre-allocated fixed-size list buffers with reference swapping and `@lru_cache` to minimize memory allocations and garbage collection overhead.
