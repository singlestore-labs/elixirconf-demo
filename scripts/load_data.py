
from elixirconf.csv import load_csv


def load_product_categories():
    load_csv("data/product_categories.csv", "product_categories")


def load_products():
    load_csv("data/products.csv", "products")


def load_product_embeddings():
    load_csv("data/product_embeddings.csv", "product_embeddings")


def load_product_inventory():
    load_csv("data/product_inventory.csv", "product_inventory")


def load_orders():
    load_csv("data/orders.csv", "orders")


def load_order_products():
    load_csv("data/order_products.csv", "order_products")


def main():
    load_product_categories()
    load_products()
    load_product_embeddings()
    load_product_inventory()
    load_orders()
    load_order_products()


if __name__ == "__main__":
    main()
