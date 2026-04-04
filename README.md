# CSV Data Cleaner & Validator (Python CLI)

Clean, validate, and deduplicate messy CSV files in seconds — without manual work.

---

## 🚨 Problem

Messy CSV files often contain:
- Duplicate entries
- Invalid data (emails, numbers)
- Inconsistent formatting
- Empty or broken rows

Cleaning them manually in Excel is slow, error-prone, and not scalable.

---

## ✅ Solution

This tool automates CSV cleaning by:

- Removing duplicate rows (full or column-based)
- Validating data using custom rules
- Normalizing and cleaning raw data
- Generating detailed processing reports

---

## ⚙️ Features

- Deduplication (full row or specific columns)
- Data validation (email, integer)
- Data normalization (whitespace trimming)
- Empty row removal
- Dry-run mode (preview changes safely)
- JSON report generation
- Robust error handling

---

## 🚀 Example Usage

```bash
python src/main.py \
  --input messy.csv \
  --output clean.csv \
  --column email \
  --rules email=email age=int \
  --report report.json
```

---

## 📊 Example Output

```bash
Total rows: 1000
Clean rows: 820
Duplicates removed: 120
Invalid rows: 60
Rule failures: 40
```

## 📁 Report Example (JSON)

```json
{
  "total_rows": 1000,
  "clean_rows": 820,
  "duplicates_removed": 120,
  "invalid_count": 60,
  "rule_fail_count": 40
}
```

## 🧪 Example Workflow

- Input (messy.csv)
```csv
name,age,email
Alex,23,alex@mail.com
Alex,23,alex@mail.com
Emma,,emma@mail.com
```

- Output(clean.csv)
```csv
name,age,email
Alex,23,alex@mail.com
Emma,,emma@mail.com
```

## 🧩 Quick Start
- Normal run(Without any rules)
```bash
python src/main.py --input messy.csv --output clean.csv
```
- With validation rules:
```bash
python src/main.py --input messy.csv --output clean.csv --rules email=email age=int
```
- Dry-Run preview:
```bash
python src/main.py --input messy.csv --dry-run
```

## 🎯 Use Cases
- Cleaning CSV exports from Excel or Google Sheets
- Preparing datasets for analysis
- Freelance data cleaning tasks
- Automating repetitive data cleanup

## 💡 Why This Tool?
Unlike simple CSV cleaners, this tool:
- Validates data (not just cleans it)
- Provides detailed processing insights
- Supports safe preview before execution
- Handles real-world messy datasets
