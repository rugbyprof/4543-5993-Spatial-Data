#!/usr/bin/env python3

from pathlib import Path
import yaml
from datetime import datetime

NOW = datetime.now()


OUTPUT_FILE = "GLOBAL_CALENDAR.md"


def truncate_string(s, max_length=31):
    # Check if the string length exceeds the maximum length
    if len(s) > max_length:
        # Truncate the string and add the ellipsis (...)
        # The total length with "..." will be max_length
        return s[: max_length - 3] + "..."
    else:
        # Return the original string if it is not too long
        return s


def load_meta(meta_path: Path):
    with meta_path.open() as f:
        data = yaml.safe_load(f)

    if not data or not data.get("due"):
        return None

    try:
        due = datetime.fromisoformat(str(data["due"]))
    except ValueError:
        raise ValueError(f"Invalid due date in {meta_path}")

    return {
        "course": data.get("course", "UNKNOWN"),
        "title": data.get("title", meta_path.parent.name),
        "due": due,
        "points": data.get("points", ""),
        "path": meta_path.parent.as_posix(),
    }


def collect_assignments(root="."):
    assignments = []

    for meta in Path(root).rglob("meta.yaml"):
        record = load_meta(meta)
        if record:
            assignments.append(record)

    return sorted(assignments, key=lambda a: (a["due"], a["title"].lower()))


def render_markdown(assignments):
    lines = []
    lines.append("# 📅 Global Assignment Calendar\n")
    lines.append("| Status | Course | Assignment | Due Date | Points | Folder |")
    lines.append("|--------|--------|-----------|----------|--------|--------|")

    for a in assignments:
        is_late = a["due"] < NOW
        status = "🔴 LATE" if is_late else "🟢"

        due_str = a["due"].strftime("%Y-%m-%d %H:%M")
        folder_link = f"[{truncate_string(a['path'])}]({a['path']})"

        title = f"**{a['title']}**" if is_late else a["title"]

        lines.append(
            f"| {status} | {a['course']} | {title} | {due_str} | {a['points']} | {folder_link} |"
        )

    return "\n".join(lines) + "\n"


def main():
    assignments = collect_assignments()

    if not assignments:
        print("⚠️  No dated assignments found.")
        return

    content = render_markdown(assignments)
    Path(OUTPUT_FILE).write_text(content)

    print(f"✅ Wrote {OUTPUT_FILE} ({len(assignments)} items)")


if __name__ == "__main__":
    main()
