"""Write one comedy patch note to /output/entry.txt.

Stdlib only, no network, deterministic: the same line every run.
"""

import os

ENTRY = "v4.0.2: fixed a bug where entering a room wiped the task queue without saving; step back out and re-enter to recover it."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
