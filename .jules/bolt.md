# Bolt's Performance Journal

## 2026-08-16 - Punctuation set lookup and list accumulation in string splitting
**Learning:** Checking character membership against a Python list `const.PUNCTUATIONS` during string iteration causes $O(N \times P)$ linear scan overhead, and repeatedly concatenating strings (`txt += char`) generates intermediate string objects. Converting punctuation to a pre-computed set `PUNCTUATION_SET` allows $O(1)$ set membership testing and $O(N)$ disjoint checks via `PUNCTUATION_SET.isdisjoint()`. Accumulating characters in a list (`txt.append(char)`) and joining on delimiter boundaries yields a ~1.7x–2.7x speedup for string splitting and punctuation checking in subtitle processing.
**Action:** Always pre-compute static character lists as sets for $O(1)$ lookup and set operation algorithms when scanning or splitting large text streams.
