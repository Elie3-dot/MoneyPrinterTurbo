## 2025-05-20 - O(1) Punctuation Lookups & Disk Stat Elimination in Path Utilities

**Learning:** `split_string_by_punctuations` in `app/utils/utils.py` previously performed repeated string `+=` operations and $O(N)$ linear scans against `const.PUNCTUATIONS` tuple on every character loop, while `root_dir()` executed expensive `os.path.realpath` disk `stat` system calls repeatedly.

**Action:**
1. Pre-compute `PUNCTUATION_SET = set("".join(const.PUNCTUATIONS))` at module load time for $O(1)$ character checks and `isdisjoint()` calls.
2. Accumulate character lists `txt_chars` instead of string `+=` in loops to avoid repeated memory allocations.
3. Pre-compute `_ROOT_DIR` at module load time to convert `root_dir()` into an $O(1)$ constant return.
