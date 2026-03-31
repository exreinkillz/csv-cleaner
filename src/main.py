import argparse
import logging
import sys

from csv_cleaner import read_csv, clean_data, write_csv

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

def main():
    parser = argparse.ArgumentParser(description="Clean CSV files from duplicates")
    parser.add_argument("--input", required=True, help="Input CSV file")
    parser.add_argument("--output", required=True, help="Output CSV file")
    parser.add_argument("--column", help="Column name to deduplicate on")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing output file")
    args = parser.parse_args()

    rows = read_csv(args.input)

    if len(rows) == 0:
        logging.error("Empty input file")
        sys.exit(1)

    cleaned, duplicates = clean_data(rows, args.column)

    if not cleaned:
        logging.error("No valid data found")
        sys.exit(1)

    if args.dry_run:
        logging.info("DRY RUN MODE - no file written")
        logging.info(f"Rows after cleaning: {len(cleaned)}")
        logging.info(f"Duplicates removed: {duplicates}")
    else:
        write_csv(args.output, cleaned)
        logging.info(f"Duplicates removed: {duplicates}")
        logging.info("CSV cleaning completed successfully")

if __name__ == "__main__":
    main()