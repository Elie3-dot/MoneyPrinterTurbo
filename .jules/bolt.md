## 2025-05-18 - [O(1) Punctuation Set Lookups]
**Learning:** Performing `char in list` or iterating over punctuation lists (`const.PUNCTUATIONS`) during string splitting and word checking leads to unnecessary `O(N)` linear searches for every character in scripts/subtitles. Using a pre-computed `PUNCTUATION_SET` set allows `O(1)` membership lookups and fast `isdisjoint` string scans.
**Action:** Use pre-computed sets for multi-character/symbol matching in frequent text processing loops.
