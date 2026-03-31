# CSV Cleaner CLI Tool

A Python CLI tool for cleaning CSV files by removing duplicate rows. Supports both full-row and column-based deduplication with basic data normalization.

---

## Features

- Full-row duplicate removal
- Column-based duplicate removal (`--column`)
- Data normalization (trim + case-insensitive comparison)
- Keeps original CSV header intact
- Safe handling of empty datasets
- Dry-run mode (no side effects)
- Duplicate statistics reporting
    
---

## Usage

```bash
python src/main.py --input <input_file> --output <output_file> --column <column_name>
```

---

## Dry-Run

```bash
python src/main.py --input data.csv --output cleaned.csv --dry-run
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

## Use Cases

- Data preprocessing tasks
- Cleaning exports from Excel / Google Sheets
- Lightweight ETL pipelines
- Automation scripts
  
---

## Note

- No sample dataset is included.
- Input file must be a valid CSV.
- Column name must match header exactly.

---

## Tech Stack

- Python 3  
- argparse (CLI)  
- csv module  
- logging  

