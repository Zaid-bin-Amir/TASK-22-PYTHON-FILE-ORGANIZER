# TASK-22-PYTHON-FILE-ORGANIZER# Python File Organizer

A simple Python command-line tool that scans a folder and automatically sorts its files into category folders based on their extensions.

Built as part of a Python Programming Track assignment to learn filesystem automation using `pathlib` and `shutil`.

## Features

- Sorts files into `Images`, `Documents`, `Videos`, `Audio`, `Archives`, `Code` and `Others`
- Uses `pathlib` for clean and readable filesystem operations
- Handles duplicate filenames safely (`photo.jpg` becomes `photo_1.jpg`, nothing is overwritten)
- Case-insensitive extension matching (`.PNG` and `.png` are treated the same)
- Skips hidden files and existing subfolders
- `--dry-run` mode to preview changes before moving anything

## Project Structure

```
python-file-organizer/
├── file_organizer.py          # main organizer script
├── create_test_directory.py   # builds a sample folder for testing
├── test_directory/            # sample files (before organizing)
├── before_after.txt           # folder structure before and after
├── run_output.txt             # output of a sample run
└── README.md
```

## Requirements

- Python 3.6 or higher
- No external libraries needed (uses only the standard library)

## Usage

1. Create the test directory:

```
python create_test_directory.py
```

2. Preview what will happen (nothing is moved):

```
python file_organizer.py test_directory --dry-run
```

3. Organize the files:

```
python file_organizer.py test_directory
```

> Warning: do not run this on important personal folders while testing. Use `test_directory` only.

## Category Mapping

| Category  | Extensions                                                      |
|-----------|-----------------------------------------------------------------|
| Images    | .jpg .jpeg .png .gif .bmp .svg .webp                            |
| Documents | .pdf .doc .docx .txt .odt .rtf .pptx .xlsx .csv                 |
| Videos    | .mp4 .mkv .avi .mov .wmv                                        |
| Audio     | .mp3 .wav .aac .flac .ogg                                       |
| Archives  | .zip .rar .7z .tar .gz                                          |
| Code      | .py .js .html .css .java .cpp .c .json                          |
| Others    | everything else                                                 |

To add or change categories, edit the `CATEGORIES` dictionary in `file_organizer.py`.

## Example

Before:

```
test_directory/
├── Images/
│   └── photo1.jpg
├── README
├── backup.zip
├── data.csv
├── index.html
├── logo.svg
├── movie.mp4
├── notes.txt
├── photo1.jpg
├── photo2.PNG
├── report.docx
├── resume.pdf
├── script.py
├── song.mp3
└── unknown.xyz
```

After:

```
test_directory/
├── Archives/
│   └── backup.zip
├── Audio/
│   └── song.mp3
├── Code/
│   ├── index.html
│   └── script.py
├── Documents/
│   ├── data.csv
│   ├── notes.txt
│   ├── report.docx
│   └── resume.pdf
├── Images/
│   ├── logo.svg
│   ├── photo1.jpg
│   ├── photo1_1.jpg
│   └── photo2.PNG
├── Others/
│   ├── README
│   └── unknown.xyz
└── Videos/
    └── movie.mp4
```

Notice that `photo1.jpg` already existed in `Images/`, so the incoming file was saved as `photo1_1.jpg` instead of overwriting it.

## How It Works

1. `get_category()` reads a file's extension and finds its category.
2. `get_unique_destination()` adds a numeric suffix if the target name is already taken.
3. `organize_folder()` loops over the folder, creates category folders when needed and moves each file with `shutil.move()`.

## Learning Notes

- **pathlib**: an object-oriented way to work with filesystem paths.
- **os vs shutil**: `os` gives low-level operating system functions (paths, listing, removing), while `shutil` provides high-level file operations such as moving and copying.
- **Automation**: Python can replace repetitive file-management work with a script that runs in seconds.

## License

Free to use for learning purposes.
