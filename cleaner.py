import csv
import sys


def read_rows(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def write_rows(rows, path):
    if not rows:
        return
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


def drop_empty_rows(rows):
    return [row for row in rows if any(value.strip() for value in row.values())]


def strip_whitespace(rows):
    return [{key: value.strip() for key, value in row.items()} for row in rows]


def remove_duplicates(rows):
    seen = set()
    unique = []
    for row in rows:
        key = tuple(row.values())
        if key not in seen:
            seen.add(key)
            unique.append(row)
    return unique


def clean(rows):
    rows = drop_empty_rows(rows)
    rows = strip_whitespace(rows)
    return remove_duplicates(rows)


if __name__ == "__main__":
    input_path, output_path = sys.argv[1], sys.argv[2]
    write_rows(clean(read_rows(input_path)), output_path)


def normalize_city(rows):
    return [{**row, "city": row["city"].title()} for row in rows]
