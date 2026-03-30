import csv

def read_csv(file):
    with open(file, "r", newline="") as f:
        return list(csv.reader(f))

def clean_data(rows):
    if not rows:
        return [], 0

    header = rows[0]
    data = rows[1:]

    seen = set()
    unique_rows = [header]
    duplicates = 0

    for row in data:
        t = tuple(row)
        if t not in seen:
            seen.add(t)
            unique_rows.append(row)
        else:
            duplicates += 1

    return unique_rows, duplicates

def write_csv(file, rows):
    with open(file, "w", newline="") as f:
        csv.writer(f).writerows(rows)


