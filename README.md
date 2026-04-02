# CSV Cleaner (Python Automation Tool)

Do you have messy CSV files (including Excel exports) with duplicate rows, missing values, or inconsistent formatting?

This tool automatically cleans and standardizes your data in seconds.

---

## 🔧 What it does

- Removes duplicate rows (full or based on a specific column)
- Cleans and normalizes messy data (trimming, case handling)
- Keeps your original structure intact
- Outputs a clean, ready-to-use CSV file

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
