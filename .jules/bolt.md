# Bolt's Journal

## 2026-08-03 - [Python Levenshtein DP Loop Optimization]
**Learning:** In Python, a naive flat-array Levenshtein implementation using `for j in range(m): ... s2[j]` is actually slower than the original `for j, c2 in enumerate(s2):` because list index lookups (`s2[j]`) and `range()` iterator overhead in Python are slow. However, we can achieve maximum speed by combining `enumerate(s2)` with a pre-allocated 2-row buffer swapping mechanism to avoid dynamic list allocation overhead (`list.append`).
**Action:** Always combine `enumerate()` iterator unpacking with flat array buffer reuse when optimizing Python loops, and use `@lru_cache` to bypass the calculation entirely on repeat strings.
