import csv

def read_csv(file):
    with open(file, "r", newline="") as f:
        return list(csv.reader(f))

def clean_data(rows, column=None):
    if not rows:
        return [], 0

    header = rows[0]

    if column:
        if column not in header:
            raise ValueError(f"Column {column} not found in CSV")
        index = header.index(column)

    data = rows[1:]

    seen = set()
    unique_rows = [header]
    duplicates = 0


    for row in data:
        if column:
            key = row[index].strip().lower()
        else:
            key = tuple(cell.strip().lower() for cell in row)

        if key not in seen:
            seen.add(key)
            unique_rows.append(row)
        else:
            duplicates += 1

    return unique_rows, duplicates

def write_csv(file, rows):
    with open(file, "w", newline="") as f:
        csv.writer(f).writerows(rows)


