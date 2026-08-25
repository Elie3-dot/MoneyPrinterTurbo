## 2025-08-25 - [Optimize estimate_no_voice_duration in voice.py]
**Learning:** `estimate_no_voice_duration` in `app/services/voice.py` previously executed regex compilation and duplicate matching on every call for word counting (`re.findall(r"[A-Za-z0-9]+", text)`), alongside string tuple checks on unicodedata categories.
**Action:** Pre-compile `_CJK_RE` and `_WORD_RE` regexes at module level, reuse word match lists for character length calculations, and check `category[0] in ("L", "N")` directly instead of `category.startswith(("L", "N"))`.
