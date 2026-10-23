import csv


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
