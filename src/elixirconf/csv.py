import csv
from pathlib import Path


def write_csv(rows, path, headers=None):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)

        if headers:
            writer.writerow(list(headers))

        for row in rows:
            writer.writerow(list(row))

    return path


def read_csv(path, headers=True):
    path = Path(path)
    rows = []

    with path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)

        if headers:
            next(reader, None)

        for row in reader:
            rows.append(tuple(row))

    return rows
