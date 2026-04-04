import argparse
import logging
import sys
import json

from csv_cleaner import read_csv, clean_data, write_csv

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def parse_rules(rule_args):
    rules = {}
    for r in rule_args:
        if "=" not in r:
            raise Exception(f"Invalid rule format: {r} (expected col=rule)")
        col, rule = r.split("=", 1)
        rules[col.strip()] = rule.strip()
    return rules


def print_summary(stats):
    logging.info("----- SUMMARY -----")
    logging.info(f"Total rows: {stats['total_rows']}")
    logging.info(f"Clean rows: {stats['clean_rows']}")
    logging.info(f"Duplicates removed: {stats['duplicates_removed']}")
    logging.info(f"Invalid rows: {stats['invalid_count']}")
    logging.info(f"Rule failures: {stats['rule_fail_count']}")


def main():
    parser = argparse.ArgumentParser(description="Clean, validate, and deduplicate CSV files")

    parser.add_argument("--input", required=True, help="Input CSV file")
    parser.add_argument("--output", help="Output CSV file")

    parser.add_argument("--column", nargs="+", help="Column(s) to deduplicate on")
    parser.add_argument("--rules", nargs="*", help="Validation rules (e.g. email=email age=int)")

    parser.add_argument("--report", help="Save report as JSON file")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing output")

    args = parser.parse_args()

    try:
        rows = read_csv(args.input)

        if not rows:
            logging.error("Empty input file")
            sys.exit(1)

        rules = parse_rules(args.rules) if args.rules else None

        cleaned, stats = clean_data(
            rows,
            rules=rules,
            dedupe_keys=args.column
        )

        if not cleaned:
            logging.error("No valid data after processing")
            sys.exit(1)

        print_summary(stats)

        if args.dry_run:
            logging.info("DRY RUN MODE - no file written")

            preview_count = min(5, len(cleaned) - 1)
            if preview_count > 0:
                logging.info("Sample cleaned rows:")
                for row in cleaned[1:1 + preview_count]:
                    logging.info(row)

        else:
            if not args.output:
                logging.error("Output file required (unless using --dry-run)")
                sys.exit(1)

            write_csv(args.output, cleaned)
            logging.info("CSV written successfully")

        if args.report:
            try:
                with open(args.report, "w", encoding="utf-8") as f:
                    json.dump(stats, f, indent=4)
                logging.info(f"Report saved to {args.report}")
            except Exception as e:
                logging.error(f"Failed to write report: {e}")
                sys.exit(2)

        sys.exit(0)

    except Exception as e:
        logging.error(f"Error: {e}")
        sys.exit(2)


if __name__ == "__main__":
    main()