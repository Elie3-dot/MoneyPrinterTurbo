## 2025-05-20 - Optimize punctuation matching and sentence splitting in utils

**Learning:** `str_contains_punctuation` and `split_string_by_punctuations` in `app/utils/utils.py` were performing linear scans over `const.PUNCTUATIONS` list and repeated string allocations (`txt += char`). Using a pre-computed module-level set `PUNCTUATION_SET` along with `isdisjoint()` for punctuation detection and character list accumulation for sentence splitting yields a ~1.7x to 3.7x performance speedup.

**Action:** Prefer module-level pre-computed sets and list character building when scanning or parsing texts char-by-char in Python.
