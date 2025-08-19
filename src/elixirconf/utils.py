from random import randrange
from datetime import datetime, timezone, timedelta


def create_get_random_date():
    now = datetime.now(timezone.utc)
    start = now - timedelta(days=30)
    delta_seconds = int((now - start).total_seconds())

    def get():
        return start + timedelta(seconds=randrange(delta_seconds))

    return get
