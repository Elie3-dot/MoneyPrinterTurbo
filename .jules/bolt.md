## 2025-05-18 - Optimize Punctuation Checking, Sentence Splitting, and Root Directory Resolution

**Learning:** `split_string_by_punctuations` and `str_contains_punctuation` are frequently invoked throughout script preprocessing, subtitle generation, and TTS text alignment loops. Performing string concatenation in character iteration loops and linear scans over tuple/list punctuation sequences creates unnecessary runtime and garbage collection overhead. Pre-computing a module-level `PUNCTUATION_SET` allows $O(1)$ set disjointness checks (`not PUNCTUATION_SET.isdisjoint(word)`) and $O(N)$ string accumulation via list `.append()` and `"".join()`. Additionally, caching static module paths like `_ROOT_DIR` avoids redundant `os.path.realpath` disk stat lookups.

**Action:** Prefer `set.isdisjoint()` for checking string character containment against fixed character sets, accumulate string characters in lists before joining, and precompute constant module-level directory paths.
