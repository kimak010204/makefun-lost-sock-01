"""Funniest Lost Sock Status Update — writes one status update to /output/entry.txt.

Stdlib only. ENTRY is a single line, 1-120 chars, no trailing newline.
"""

import os

ENTRY = "I followed the lint to a secret sock society under the bed. We meet Tuesdays. My owner is not invited."

assert 1 <= len(ENTRY) <= 120, f"entry length {len(ENTRY)} out of range"
assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
assert ENTRY.strip(), "entry must not be only whitespace"
assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing whitespace"

out_dir = os.environ.get("OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
