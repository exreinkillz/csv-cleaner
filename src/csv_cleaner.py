import csv
import re

EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

def read_csv(file):
    try:
        with open(file, "r", newline="", encoding="utf-8") as f:
            return list(csv.reader(f))
    except FileNotFoundError:
        raise Exception(f"Input file not found: {file}")
    except Exception as e:
        raise Exception(f"Failed to read CSV: {e}")

def write_csv(file, rows):
    try:
        with open(file, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerows(rows)
    except Exception as e:
        raise Exception(f"Failed to write to CSV: {e}")

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
    except ValueError:
        return False

VALIDATORS = {
    "email": is_valid_email,
    "int": is_int,
}

def apply_rules(row, header_map, rules):
    failures = []

    for col_name, rule in rules.items():
        if col_name not in header_map:
            failures.append({
                "column": col_name,
                "error": "invalid_column"
            })
            continue

        idx = header_map(col_name)
        value = row[idx].strip()

        validator = VALIDATORS.get(rule)

        if not validator:
            failures.append({
                "column": col_name,
                "error": "unknown_rule",
                "rule": rule
            })
            continue

        if not validator(value):
            failures.append({
                "column": col_name,
                "rule": rule,
                "value": value
            })

    if failures:
        return False, failures

    return True, None

def deduplicate(rows, header_map, key_columns=None):
    seen = set()
    result = []
    duplicates = []

    if key_columns:
        for col in key_columns:
            if col not in header_map:
                raise Exception(f"Column not found in header: {col}")

    for row in rows:
        if key_columns:
            key = []
            for col in key_columns:
                idx = header_map(col)
                value = row[idx].strip().lower()

                if not value:
                    value = "__EMPTY__"

                key.append(value)

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
    stats = {
        "total_rows": 0,
        "clean_rows": 0,
        "duplicates_removed": 0,
        "invalid_count": 0,
        "rule_fail_count": 0,
        "invalid_rows": [],
        "duplicate_rows": [],
        "rule_failures": [],
    }

    if not rows or len(rows) < 2:
        return [], stats

    header = normalize_row(rows[0])
    data = rows[1:]

    header_map = {col: idx for idx, col in enumerate(header)}

    data = remove_empty_rows(data)
    data = [normalize_row(row) for row in data]

    data, dup_rows = deduplicate(data, header_map, dedupe_keys)
    stats["duplicate_rows"] = dup_rows

    cleaned = [header]

    for row in data:
        if len(row) != len(header):
            stats["invalid_rows"].append({"row": row, "reason": "column_mismatch"})
            continue

        if rules:
            ok, failures = apply_rules(row, header_map, rules)
            if not ok:
                stats["rule_failures"].append({
                    "row": row,
                    "failures": failures
                })
                continue

        cleaned.append(row)

    stats["total_rows"] = len(rows) - 1
    stats["clean_rows"] = len(cleaned) - 1
    stats["duplicates_removed"] = len(stats["duplicate_rows"])
    stats["invalid_count"] = len(stats["invalid_rows"])
    stats["rule_fail_count"] = len(stats["rule_failures"])

    return cleaned, stats