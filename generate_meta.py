#!/usr/bin/env python3

from pathlib import Path
import yaml

DEFAULT_META = {
    "title": "Assignment Title Here",
    "course": "4543-5993-Spatial-Data",
    "type": "assignment",
    "due": None,
    "points": None,
    "notebooks": [],
    "created_from": "auto",
}


def find_assignment_folders(root="."):
    """
    Find folders that contain at least one .ipynb file
    """
    for path in Path(root).rglob("*.ipynb"):
        yield path.parent


def create_meta_yaml(folder: Path):
    meta_path = folder / "meta.yaml"

    if meta_path.exists():
        print(f"⏭️  Skipping (exists): {meta_path}")
        return

    notebooks = sorted(p.name for p in folder.glob("*.ipynb"))

    meta = DEFAULT_META.copy()
    meta["notebooks"] = notebooks

    with meta_path.open("w") as f:
        yaml.safe_dump(meta, f, sort_keys=False)

    print(f"✅ Created: {meta_path}")


def main(root="."):
    seen = set()

    for folder in find_assignment_folders(root):
        if folder in seen:
            continue
        seen.add(folder)
        create_meta_yaml(folder)


if __name__ == "__main__":
    main()
