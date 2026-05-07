from pathlib import Path

SELF = Path(__file__).resolve()

KEEP_EXTENSIONS = {".ipynb", ".md", ".yaml"}
KEEP_FILENAMES = {"README.md", "meta.yaml"}

IGNORE_DIRS = {
    ".git",
    "__pycache__",
    ".ipynb_checkpoints"
}

def should_keep(path):
    if path.is_dir():
        return path.name not in IGNORE_DIRS

    return (
        path.suffix in KEEP_EXTENSIONS or
        path.name in KEEP_FILENAMES
    )

def print_tree(path: Path, prefix=""):
    items = [p for p in sorted(path.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))
             if should_keep(p)]

    for i, item in enumerate(items):
        
        # Skip this script

        if item.resolve() == SELF:

            continue
        
        connector = "└── " if i == len(items) - 1 else "├── "

        print(prefix + connector + item.name)

        if item.is_dir():
            extension = "    " if i == len(items) - 1 else "│   "
            print_tree(item, prefix + extension)

print_tree(Path("."))