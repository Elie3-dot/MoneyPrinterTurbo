# Bolt's Journal

## 2025-02-21 - SRT Subtitle Parsing and Levenshtein Distance Optimization
**Learning:** Checking for standard text indicators (like `"-->"` in SRT timestamp lines) before executing regex matching on every line in a file avoids running regex engines on non-matching lines (subtitle text, blank lines, index numbers), yielding a ~4x performance improvement. In dynamic programming string algorithms (Levenshtein distance), pre-allocating flat row lists and swapping them eliminates inner-loop list allocation garbage collection overhead.
**Action:** Always pre-screen text lines with string containment before running regexes over large files or loops, and use pre-allocated flat arrays with swapping for DP matrix calculations.
