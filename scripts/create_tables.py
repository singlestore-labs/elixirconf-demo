from elixirconf.db import db


def main():
    try:
        with db.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS product_categories (
                    id BIGINT AUTO_INCREMENT,
                    name VARCHAR(128) NOT NULL,
                    PRIMARY KEY (id)
                );
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    id BIGINT AUTO_INCREMENT,
                    category_id BIGINT NOT NULL,
                    name VARCHAR(512) NOT NULL,
                    description TEXT,
                    price DECIMAL(10, 2),
                    PRIMARY KEY (id)
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS product_embeddings (
                    id BIGINT AUTO_INCREMENT,
                    product_id BIGINT NOT NULL,
                    content TEXT NOT NULL,
                    embedding VECTOR(1536) NOT NULL,
                    PRIMARY KEY (id)
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS product_inventory (
                    id BIGINT AUTO_INCREMENT,
                    product_id BIGINT NOT NULL,
                    stock BIGINT NOT NULL DEFAULT 0,
                    supply_delivery_days BIGINT NOT NULL DEFAULT 0,
                    reorder_threshold BIGINT NOT NULL DEFAULT 0,
                    PRIMARY KEY (id)
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS orders (
                    id BIGINT AUTO_INCREMENT,
                    created_at TIMESTAMP NOT NULL,
                    PRIMARY KEY (id)
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS order_products (
                    order_id BIGINT NOT NULL,
                    product_id BIGINT NOT NULL,
                    quantity INT NOT NULL,
                    SHARD KEY (order_id),
                    SORT KEY (order_id)
                )
            """)
    finally:
        db.close()


if __name__ == "__main__":
    main()
