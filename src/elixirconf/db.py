from dotenv import load_dotenv
from os import getenv
from singlestoredb import connect

load_dotenv()

db = connect(
    user=getenv("DB_USERNAME"),
    password=getenv("DB_PASSWORD"),
    host=getenv("DB_HOST"),
    port=getenv("DB_PORT"),
    database=getenv("DB_NAME")
)
