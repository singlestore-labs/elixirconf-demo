from elixirconf.db import db


def main():
    try:
        with db.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS product_categories (
                    id BIGINT AUTO_INCREMENT,
                    name VARCHAR(128) NOT NULL,
                    KEY (id),
                    SHARD KEY (name),
                    CONSTRAINT name_uk UNIQUE (name)
                );
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    id BIGINT AUTO_INCREMENT,
                    category_id BIGINT NOT NULL,
                    name VARCHAR(512) NOT NULL,
                    description TEXT,
                    price DECIMAL(10, 2),
                    KEY (id),
                    SHARD KEY (name),
                    CONSTRAINT name_uk UNIQUE (name)
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS product_embeddings (
                    id BIGINT PRIMARY KEY AUTO_INCREMENT,
                    product_id BIGINT NOT NULL,
                    content TEXT NOT NULL,
                    embedding VECTOR(1536) NOT NULL
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS product_inventory (
                    id BIGINT PRIMARY KEY AUTO_INCREMENT,
                    product_id BIGINT NOT NULL,
                    stock BIGINT NOT NULL DEFAULT 0,
                    supply_delivery_days INTEGER NOT NULL DEFAULT 0,
                    reorder_threshold BIGINT NOT NULL DEFAULT 0
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS orders (
                    id BIGINT PRIMARY KEY AUTO_INCREMENT,
                    created_at TIMESTAMP NOT NULL
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS order_products (
                    id BIGINT PRIMARY KEY AUTO_INCREMENT,
                    order_id BIGINT NOT NULL,
                    product_id BIGINT NOT NULL
                )
            """)
    finally:
        db.close()


if __name__ == "__main__":
    main()
