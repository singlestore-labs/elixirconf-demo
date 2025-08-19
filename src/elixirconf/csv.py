import csv
from pathlib import Path
from contextlib import contextmanager
from typing import Sequence, Optional, Any, Callable, Generator
from elixirconf.db import db


@contextmanager
def csv_writer(
    path: Path | str,
    headers: Optional[Sequence[str]] = None,
    batch_size: int = 10_000,
) -> Generator[Callable[[Sequence[Any]], None], None, None]:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    file = path.open("w", encoding="utf-8", newline="")
    writer = csv.writer(file)

    if headers is not None:
        writer.writerow(headers)

    buffer: list[Sequence[Any]] = []

    def flush() -> None:
        if buffer:
            writer.writerows(buffer)
            buffer.clear()

    def write(row: Sequence[Any]) -> None:
        buffer.append(row)
        if len(buffer) >= batch_size:
            flush()

    try:
        yield write
    finally:
        flush()
        file.close()


def load_csv(path: Path | str, table_name: str):
    with db.cursor() as cursor:
        cursor.execute(f"""
            LOAD DATA LOCAL INFILE %s
            INTO TABLE {table_name}
            LINES TERMINATED BY '\r\n'
            FIELDS TERMINATED BY ','
            ENCLOSED BY '"'
            IGNORE 1 LINES
        """, (path))
