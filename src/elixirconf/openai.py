from dotenv import load_dotenv
from os import getenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=getenv("OPENAI_API_KEY"))


def create_embeddings(input: list[str]):
    response = client.embeddings.create(
        input=input,
        model="text-embedding-3-small"
    )

    return response.data
