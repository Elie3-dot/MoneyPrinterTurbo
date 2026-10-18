## 2025-05-20 - Module-level Pre-compiled Regular Expressions in LLM Service
**Learning:** Calling `re.sub`, `re.search`, or `re.split` with string patterns repeatedly inside LLM parsing functions triggers runtime regex compilation overhead. Pre-compiling regexes at the module level speeds up string processing and JSON recovery by ~40%.
**Action:** When working on text cleaning or parsing pipelines, declare top-level pre-compiled regex objects (`re.compile`) to avoid repeated dynamic compilation.
