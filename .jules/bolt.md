## 2025-05-18 - Fast SRT Parsing with Fast-String Pre-Screening
**Learning:** In SRT parsing, running regex matches against every single line (including indices, subtitle text, and blank lines) causes significant overhead. Pre-screening lines with `"-->" in line` before evaluating a module-level pre-compiled regex avoids regex execution on ~75%+ of lines and yields a ~3.8x speedup.
**Action:** Always look for fast string pre-screening checks (e.g. substring or prefix checks) before running regex searches in hot loops.
