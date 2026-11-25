import os

# One commit message for a fix that made everything worse:
# the slow query is gone because the page no longer loads anything.
ENTRY = "fix: removed the slow query — the page now loads nothing, instantly"

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
# The grader counts characters: 67 chars, well inside the 1-100 gate.
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
