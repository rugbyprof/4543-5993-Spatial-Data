#!/usr/bin/env python3

from pathlib import Path
import yaml
import csv

OUTPUT = "assignments.csv"

FIELDS = ["course", "title", "due", "points", "path"]


def main(root="."):
    rows = []

    for meta in Path(root).rglob("meta.yaml"):
        with meta.open() as f:
            data = yaml.safe_load(f) or {}

        if meta.parent.as_posix()[0:1] == ".":
            # skip hidden folders
            continue
        rows.append(
            {
                "course": data.get("course", ""),
                "title": data.get("title", meta.parent.name),
                "due": data.get("due", ""),
                "points": data.get("points", ""),
                "path": meta.parent.as_posix(),
            }
        )

    rows.sort(key=lambda r: (r["due"] or "9999"))

    with open(OUTPUT, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    print(f"✅ Exported {len(rows)} assignments to {OUTPUT}")


if __name__ == "__main__":
    main()
