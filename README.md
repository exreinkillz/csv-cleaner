# CSV Cleaner – Lightweight Python CLI Tool

A lightweight CLI tool for cleaning CSV files by removing duplicates, invalid rows, and normalizing data.

---

## 🔧 What it does

- Duplicate row removal (full row or column-based key)
- Data validation (email, integer)
- Empty row filtering
- Normalization (whitespace trimming)
- Dry-run mode for safe preview
  
---

## Output

The tool generates:
- Cleaned CSV file
- Processing statistics (duplicates, invalid rows, rule failures)

---

## ⚡ Example

### Before (messy data)

```csv
Name,Email,Email
Alex,,alex@mail.com
Alex,,alex@mail.com
```

### After (clean data)

```csv
name,email
alex,alex@mail.com
```

## 🚀 Features

- Remove duplicate rows (full or by column)
- Clean messy data (trim, normalize text)
- Safe processing (no data loss)
- Dry-run mode (preview before cleaning)

## 🧩 Quick Start

```bash
python src/main.py --input messy.csv --output clean.csv
```
Column included usage:

```bash
python src/main.py --input <input_file> --output <output_file> --column <column_name>
```
Dry-run usage:

```bash
python src/main.py --input <input_file> --output <output_file> --dry-run
```

## 💡 Common Use Cases

- Cleaning Excel/CSV exports
- Preparing data for analysis
- Fixing messy datasets from clients or reports
- Automating repetitive data cleaning tasks

## 🎯 Why use this tool?

Instead of manually cleaning messy data in Excel, this tool automates the process and saves you time.
