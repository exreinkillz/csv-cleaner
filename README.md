# CSV Cleaner CLI Tool

A lightweight Python CLI tool that removes duplicate rows from CSV files while preserving the header.

---

## Features

- Removes duplicate rows from CSV files  
- Keeps original header intact  
- Reports statistics (input, output, duplicates removed)  
- Handles empty or missing files safely  

---

## Usage

```bash
python src/main.py --input <input_file> --output <output_file>
```

---

## Project Structure

```
src/
  main.py
  csv_cleaner.py

.gitignore
README.md
```

---

## Note

No sample data is included.  
Provide your own CSV file via CLI arguments.

---

## Tech Stack

- Python 3  
- argparse (CLI)  
- csv module  
- logging  

