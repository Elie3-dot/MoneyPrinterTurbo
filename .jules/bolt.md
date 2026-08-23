## 2026-08-23 - Memoizing `get_all_azure_voices` for WebUI and API calls

**Learning:** `get_all_azure_voices` in `app/services/voice.py` was being called on every Streamlit WebUI script rerun to populate the Azure voice selector, parsing the JSON voice list, lowercasing locale filters, formatting strings, and sorting 300+ items repeatedly.
**Action:** Use `@lru_cache(maxsize=128)` on a helper that accepts a tuple representation of `filter_locals`, and return a shallow copy to prevent caller mutation. This achieves a ~100x speedup for cached lookups.
