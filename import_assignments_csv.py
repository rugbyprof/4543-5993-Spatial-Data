#!/usr/bin/env python3

from pathlib import Path
import yaml
import csv

CSV_FILE = "assignments.csv"


def main():
    updates = 0

    with open(CSV_FILE, newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:

            path = Path(row["path"].strip())
            meta_path = path / "meta.yaml"

            if not meta_path.exists():
                print(f"⚠️  Missing meta.yaml: {meta_path}")
                continue

            with meta_path.open() as f:
                data = yaml.safe_load(f) or {}

            changed = False

            for field in ["course", "title", "due", "points"]:
                value = row.get(field, "").strip()
                if value != "":
                    if data.get(field) != value:
                        data[field] = value
                        changed = True

            if changed:
                with meta_path.open("w") as f:
                    yaml.safe_dump(data, f, sort_keys=False)
                updates += 1
                print(f"✏️  Updated: {meta_path}")

    print(f"\n✅ Updated {updates} meta.yaml files")


if __name__ == "__main__":
    main()
