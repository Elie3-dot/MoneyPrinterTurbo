# Bolt's Journal - Performance Optimization Learnings

## 2025-02-18 - Optimized Levenshtein Distance for Subtitle Alignment
**Learning:** During subtitle alignment and matching in `app/services/subtitle.py`, `levenshtein_distance` is repeatedly called on similar and identical substrings. Using `@lru_cache(maxsize=2048)` provides dramatic performance wins by bypassing computation for identical comparisons. Additionally, refactoring the DP table from dynamic allocations (appending to list on every inner loop iteration) to a fixed 2-row buffer swapping mechanism (`r0` and `r1`) drastically reduces Python memory allocation overhead and function call overhead.
**Action:** Always look for O(N*M) dynamic programming algorithms on strings or data sequences that are called repeatedly. Apply `lru_cache` and pre-allocate flat arrays/buffers for swapping to maximize speed.
