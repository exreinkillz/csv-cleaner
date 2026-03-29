import argparse
import csv

parser = argparse.ArgumentParser(description="Clean CSV files from duplicates")
parser.add_argument("--input", required=True, help="Input CSV file")
parser.add_argument("--output", required=True, help="Output CSV file")

args = parser.parse_args()

input_file = args.input
output_file = args.output

with open(input_file, "r", newline="") as f:
    reader = csv.reader(f)
    rows = list(reader)

unique_rows = []
for row in rows:
    if row not in unique_rows:
        unique_rows.append(row)

with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(unique_rows)