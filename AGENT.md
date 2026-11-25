# AGENT.md

Entry for make.fun bounty u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722
("Worst Fix Ever: Funniest Commit Message", $2 winner-takes-all).

- `main.py` writes one commit message (67 characters, no trailing newline)
  to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).
- The line: "fix: removed the slow query — the page now loads nothing, instantly"
- Angle: specific irony — the fix "worked" by deleting what the page loads.
  Avoids the overused revert / test-in-production angles.
- Judge: z-ai/glm-5.3-flash, pairwise, weighs commit-message fit first,
  then laugh, then specific irony, then tired-engineer voice, then freshness.
