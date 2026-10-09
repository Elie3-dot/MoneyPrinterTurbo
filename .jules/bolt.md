## 2025-10-10 - Punctuation Utilities & Root Directory Optimization

**Learning:**
- `str_contains_punctuation` and `split_string_by_punctuations` in `app/utils/utils.py` are executed repeatedly during TTS, subtitle splitting, and audio transcription. Pre-computing `PUNCTUATION_SET = set("".join(const.PUNCTUATIONS))` enables O(1) set membership and `isdisjoint` checks.
- Building strings character-by-character via `txt += char` in loops causes quadratic string allocations. Collecting characters in a `list` buffer and joining on sentence boundaries reduces string splitting runtime by ~4.5x.
- `root_dir()` previously called `os.path.realpath(__file__)` on every invocation, triggering redundant disk stat lookups. Pre-computing `_ROOT_DIR` at module initialization provides a ~200x speedup.
- `@lru_cache` should NOT be added to `get_ffmpeg_binary()` as unit tests (`TestVideoService`) patch `os.environ` and `shutil.which` dynamically between test cases, causing cached return values to fail test assertions.

**Action:**
- Use pre-computed sets for character/punctuation filtering across string loops.
- Use list accumulation (`txt_chars.append(c)`) instead of string concatenation in loops.
- Avoid applying `@lru_cache` to functions that depend on dynamic environment variables patched in tests.
