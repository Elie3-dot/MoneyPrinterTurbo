## 2025-03-09 - Pre-computing set membership for string punctuation splitting

**Learning:** String splitting and punctuation detection functions in utility modules can be called frequently during video/subtitle generation. Using string concatenation (`txt += char`) inside loops creates $O(N^2)$ memory copying overhead, while checking list membership (`char in PUNCTUATIONS`) causes repeated $O(M)$ scans. Using a pre-computed `PUNCTUATION_SET` and list buffer (`txt.append(char)` with `"".join(txt)`) speeds up string splitting by ~3x while keeping code clean and readable.

**Action:** Always pre-compute constant collection lookups into `set`s at module level and use list accumulator buffers (`list.append` + `"".join()`) when constructing strings character-by-character in loops.
