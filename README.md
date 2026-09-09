# File Sorter by Modified Year

A simple Python script to walk through all files in a target directory and copy them into an output directory, organized into subfolders by the files' modified year.

---

## Features

- Recursively scans all files in the target directory.
- Copies files into year-based subfolders inside the specified output directory.
- Automatically creates year subfolders if they don’t exist.
- Skips processing the output directory itself to avoid infinite loops.
- Displays the total number of files copied.

---

## Requirements

- Python 3.12
- No external dependencies (uses standard library only)

---

## Usage

```bash
python main.py <target_dir> <output_dir>
```

---

### Motive

Originally created this script to help sort old photos on my pc.
