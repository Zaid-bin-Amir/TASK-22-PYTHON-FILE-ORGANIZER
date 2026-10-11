from pathlib import Path

TEST_DIR = Path("test_directory")

SAMPLE_FILES = [
    "photo1.jpg",
    "photo2.PNG",
    "logo.svg",
    "resume.pdf",
    "notes.txt",
    "report.docx",
    "data.csv",
    "movie.mp4",
    "song.mp3",
    "backup.zip",
    "script.py",
    "index.html",
    "unknown.xyz",
    "README",
]


def create_test_directory():
    TEST_DIR.mkdir(exist_ok=True)
    for name in SAMPLE_FILES:
        (TEST_DIR / name).write_text(f"Sample content of {name}")

    images_dir = TEST_DIR / "Images"
    images_dir.mkdir(exist_ok=True)
    (images_dir / "photo1.jpg").write_text("Old photo1 already in Images")

    print(f"Test directory created: {TEST_DIR.resolve()}")


if __name__ == "__main__":
    create_test_directory()
