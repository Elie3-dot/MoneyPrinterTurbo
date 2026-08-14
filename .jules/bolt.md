# Bolt's Journal - Critical Learnings

## 2025-05-18 - Fast Punctuation Lookup with Pre-built Set
**Learning:** Checking string characters against `const.PUNCTUATIONS` (a list of punctuation marks) in loop-heavy text processing functions (`str_contains_punctuation` and `split_string_by_punctuations`) incurs repeated linear scans ($O(N)$). Using a pre-computed set `PUNCTUATION_SET = set("".join(const.PUNCTUATIONS))` enables $O(1)$ lookup via `not PUNCTUATION_SET.isdisjoint(word)` and `char not in PUNCTUATION_SET`, giving a ~1.7x to 3x speedup without changing behavior.
**Action:** Always prefer set operations (`isdisjoint`, set lookup) when matching single characters or sets of target characters in strings across frequent loops.
