import random
import json

from elixirconf.constants import ORDERS_COUNT, PRODUCT_CATEGORIES, PRODUCTS
from elixirconf.csv import csv_writer
from elixirconf.openai import create_embeddings
from elixirconf.utils import create_get_random_date


def generate_product_categories():
    with csv_writer("data/product_categories.csv", ("id", "name")) as write:
        for id, name in PRODUCT_CATEGORIES.items():
            write((id, name))


def generate_products():
    with csv_writer("data/products.csv", ("id", "category_id", "name", "description", "price")) as write:
        for product in PRODUCTS:
            write((
                product["id"],
                product["category_id"],
                product["name"],
                product["description"],
                f"{product["price"]:.2f}"
            ))


def generate_product_embeddings():
    descriptions = [product["description"] for product in PRODUCTS]
    description_embeddings = create_embeddings(descriptions)

    with csv_writer("data/product_embeddings.csv", ("id", "product_id", "content", "embedding")) as write:
        for embedding in description_embeddings:
            write((
                embedding.index + 1,
                PRODUCTS[embedding.index]["id"],
                descriptions[embedding.index],
                json.dumps(embedding.embedding)
            ))


def generate_product_inventory():
    with csv_writer("data/product_inventory.csv", ("id", "product_id", "stock", "supply_delivery_days", "reorder_threshold")) as write:
        for i, product in enumerate(PRODUCTS):
            write((
                i + 1,
                product["id"],
                random.randint(1, 1000),
                random.randint(1, 30),
                random.randint(1, 100)
            ))


def generate_orders():
    product_ids = [product["id"] for product in PRODUCTS]
    get_random_date = create_get_random_date()

    with csv_writer("data/orders.csv", headers=("id", "created_at")) as write_orders:
        with csv_writer("data/order_products.csv", headers=("id", "order_id", "product_id")) as write_order_products:
            order_id = 0

            for _ in range(ORDERS_COUNT):
                order_id += 1
                created_at = get_random_date().strftime("%Y-%m-%d %H:%M:%S")
                write_orders((order_id, created_at))

                for product_id in random.sample(product_ids, random.randint(1, 5)):
                    quantity = random.randint(1, 10)
                    write_order_products((
                        order_id,
                        product_id,
                        quantity
                    ))


def main():
    generate_product_categories()
    generate_products()
    generate_product_embeddings()
    generate_product_inventory()
    generate_orders()


if __name__ == "__main__":
    main()
