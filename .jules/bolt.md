# Bolt's Performance Journal

## 2026-08-31 - MP3 Duration Probe Optimization
**Learning:** Loading MoviePy's `AudioFileClip` just to read an MP3 duration incurs heavy object initialization, subprocess reader setups, and stdout redirection wrappers (~30ms per invocation). Querying metadata using `ffmpeg -hide_banner -i` directly via subprocess and regex matching `Duration: ...` takes ~5ms (~6x faster) while avoiding Python object allocation/cleanup overhead.

**Action:** Prefer lightweight CLI probes (`ffmpeg -hide_banner -i`) for media metadata queries instead of instantiating full MoviePy clip objects, with defensive fallbacks to MoviePy if probing fails.
