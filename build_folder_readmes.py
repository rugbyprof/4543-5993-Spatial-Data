#!/usr/bin/env python3

from pathlib import Path
import yaml
from datetime import datetime

NOW = datetime.now()

HEADER_FILE = "._header.md"
AUTOGEN_FILE = "._autogen.md"
README_FILE = "README.md"


def load_meta(meta_path):
    with meta_path.open() as f:
        data = yaml.safe_load(f) or {}

    if not data.get("due"):
        return None

    due = datetime.fromisoformat(str(data["due"]))

    return {
        "title": data.get("title", meta_path.parent.name),
        "due": due,
        "points": data.get("points", ""),
        "path": meta_path.parent.name,
    }


def generate_table(assignments):
    lines = []
    lines.append("| Status | Assignment | Due | Points |")
    lines.append("|--------|-----------|-----|--------|")

    for a in assignments:
        late = a["due"] < NOW
        status = "🔴 LATE" if late else "🟢"
        title = f"**{a['title']}**" if late else a["title"]
        due = a["due"].strftime("%Y-%m-%d %H:%M")

        lines.append(f"| {status} | [{title}]({a['path']}) | {due} | {a['points']} |")

    return "\n".join(lines)


def build_folder(folder: Path):
    assignments = []

    for meta in folder.rglob("meta.yaml"):
        record = load_meta(meta)
        if record:
            assignments.append(record)

    if not assignments:
        return

    assignments.sort(key=lambda a: (a["due"], a["title"].lower()))

    table = generate_table(assignments)

    (folder / AUTOGEN_FILE).write_text("## 📅 Assignment Calendar\n\n" + table + "\n")

    # Assemble README
    parts = []

    header = folder / HEADER_FILE
    if header.exists():
        parts.append(header.read_text())

    parts.append((folder / AUTOGEN_FILE).read_text())

    (folder / README_FILE).write_text("\n\n".join(parts))
    print(f"✅ Updated README in {folder}")


def main():
    for folder in Path(".").iterdir():
        if folder.is_dir() and folder.name[0].isdigit():
            build_folder(folder)


if __name__ == "__main__":
    main()
