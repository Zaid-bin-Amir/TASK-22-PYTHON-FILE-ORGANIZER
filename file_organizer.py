import argparse
import shutil
import sys
from pathlib import Path

CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".odt", ".rtf", ".pptx", ".xlsx", ".csv"},
    "Videos": {".mp4", ".mkv", ".avi", ".mov", ".wmv"},
    "Audio": {".mp3", ".wav", ".aac", ".flac", ".ogg"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Code": {".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".json"},
}

DEFAULT_CATEGORY = "Others"


def get_category(file_path):
    extension = file_path.suffix.lower()
    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category
    return DEFAULT_CATEGORY


def get_unique_destination(destination):
    if not destination.exists():
        return destination
    counter = 1
    while True:
        candidate = destination.with_name(f"{destination.stem}_{counter}{destination.suffix}")
        if not candidate.exists():
            return candidate
        counter += 1


def organize_folder(folder, dry_run=False):
    folder = Path(folder).resolve()
    if not folder.is_dir():
        print(f"Error: '{folder}' is not a valid folder.")
        return 0

    moved = 0
    for item in sorted(folder.iterdir()):
        if not item.is_file():
            continue
        if item.name.startswith("."):
            continue

        category = get_category(item)
        target_dir = folder / category
        destination = get_unique_destination(target_dir / item.name)

        if dry_run:
            print(f"[DRY RUN] {item.name} -> {category}/{destination.name}")
        else:
            target_dir.mkdir(exist_ok=True)
            shutil.move(str(item), str(destination))
            print(f"Moved: {item.name} -> {category}/{destination.name}")
        moved += 1

    print(f"\nTotal files {'found' if dry_run else 'moved'}: {moved}")
    return moved


def main():
    parser = argparse.ArgumentParser(description="Organize files into folders by extension.")
    parser.add_argument("folder", help="Path of the folder to organize")
    parser.add_argument("--dry-run", action="store_true", help="Show what would happen without moving files")
    args = parser.parse_args()

    organize_folder(args.folder, args.dry_run)


if __name__ == "__main__":
    sys.exit(main())
