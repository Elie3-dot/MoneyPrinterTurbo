## 2026-09-23 - Subtitle SRT Parsing and Levenshtein Distance Optimization
**Learning:** SRT parsing performs regex evaluations across all text lines unless pre-screened with `"-->" in line`. Additionally, Levenshtein distance computations during subtitle correction allocate $O(N)$ list objects on every loop step unless flat pre-allocated row buffers are reused with row swapping.
**Action:** Pre-screen lines with `"-->" in line` before regex execution in `file_to_subtitles`, and use `@lru_cache` alongside pre-allocated flat row list swapping for DP-based string comparison functions.
