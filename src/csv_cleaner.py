import csv
import re

EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

def read_csv(file):
    with open(file, "r", newline="", encoding="utf-8") as f:
        return list(csv.reader(f))

def write_csv(file, rows):
    with open(file, "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(rows)

def normalize_row(row):
    return [cell.strip() for cell in row]

def remove_empty_rows(rows):
    return [row for row in rows if any(cell.strip() for cell in row)]

def is_valid_email(value):
    return bool(EMAIL_REGEX.match(value))

def is_int(value):
    try:
        int(value)
        return True
    except:
        return False

VALIDATORS = {
    "email": is_valid_email,
    "int": is_int,
}

def apply_rules(row, header, rules):
    """
    rules example:
    {
        "email": "email",
        "age": "int"
    } 
    """

    failures = []

    for col_name, rule in rules.items():
        if col_name not in header:
            failures.append(f"invalid_column:{col_name}")
            continue

        idx = header.index(col_name)
        value = row[idx].strip()

        validator = VALIDATORS.get(rule)

        if not validator:
            failures.append(f"unknown_rule:{rule}")
            continue

        if not validator(value):
            failures.append(f"{col_name}:{rule}:{value}")

    if failures:
        return False, failures

    return True, None

def deduplicate(rows, key_columns=None):
    seen = set()
    result = []
    duplicates = []

    for row in rows:
        if key_columns:
            key = []
            for col in key_columns:
                if col in row:
                    key.append(row[col].strip().lower())
            key = tuple(key)
        else:
            key = tuple(cell.strip().lower() for cell in row)

        if key in seen:
            duplicates.append(row)
            continue

        seen.add(key)
        result.append(row)

    return result, duplicates

def clean_data(rows, rules=None, dedupe_keys=None):
    """
    returns:
        cleaned_rows, stats
    """

    stats = {
        "invalid_rows": [],
        "duplicate_rows": [],
        "rule_failures": [],
    }

    if not rows or len(rows) < 2:
        return [], stats

    header = normalize_row(rows[0])
    data = rows[1:]

    data = remove_empty_rows(data)
    data = [normalize_row(row) for row in data]

    data, dup_rows = deduplicate(data, dedupe_keys)
    stats["duplicate_rows"] = dup_rows

    cleaned = [header]

    for row in data:
        if len(row) != len(header):
            stats["invalid_rows"].append({"row": row, "reason": "column_mismatch"})
            continue

        if rules:
            ok, failures = apply_rules(row, header, rules)
            if not ok:
                stats["rule_failures"].append({
                    "row": row,
                    "failures": failures
                })
                continue

        cleaned.append(row)

    return cleaned, stats