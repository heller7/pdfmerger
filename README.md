# PDF Merger Command-Line Tool

This Python script merges PDF files found in subdirectories of a specified input directory and saves the merged files to a specified output directory.

## Features
- Merges PDF files from subdirectories.
- Configurable number of files per merge.
- Periodic merging to check for new files.

## Requirements
- Python 3.x
- PyPDF2

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/pdf-merger-tool.git
    cd pdf-merger-tool
    ```

2. Install dependencies:

    ```bash
    pip install PyPDF2
    ```

## Usage

```bash
python main.py <input_directory> <output_parent_directory> [--max_files_per_merge MAX_FILES] [--interval INTERVAL]

## Arguments
input_directory: Directory containing subdirectories with PDF files to merge.
output_parent_directory: Directory to save the merged PDF files.
--max_files_per_merge: Maximum number of PDF files to merge at a time (default: 2).
--interval: Interval (in seconds) between merge operations (default: 60).

## Directories
input_directory/
├── subdir1/
│   ├── file1.pdf
│   ├── file2.pdf
│   └── file3.pdf
├── subdir2/
│   ├── file4.pdf
│   ├── file5.pdf
│   └── file6.pdf


output_parent_directory/
├── subdir1/
│   ├── merged_1.pdf
├── subdir2/
│   ├── merged_1.pdf





