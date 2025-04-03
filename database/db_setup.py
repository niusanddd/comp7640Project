import pymysql
from db_connection import get_db_connection


def create_tables():
    connection = get_db_connection()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS vendors (
                        vendor_id INT AUTO_INCREMENT PRIMARY KEY,
                        business_name VARCHAR(255) NOT NULL,
                        customer_feedback_score DECIMAL(3, 2),
                        geographical_presence VARCHAR(255)
                    )
                """)


                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS products (
                        product_id INT AUTO_INCREMENT PRIMARY KEY,
                        name VARCHAR(255) NOT NULL,
                        price DECIMAL(10, 2) NOT NULL,
                        vendor_id INT,
                        FOREIGN KEY (vendor_id) REFERENCES vendors(vendor_id)
                    )
                """)


                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS product_tags (
                        tag_id INT AUTO_INCREMENT PRIMARY KEY,
                        tag_name VARCHAR(255) UNIQUE NOT NULL
                    )
                """)


                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS product_tag_relations (
                        relation_id INT AUTO_INCREMENT PRIMARY KEY,
                        product_id INT,
                        tag_id INT,
                        FOREIGN KEY (product_id) REFERENCES products(product_id),
                        FOREIGN KEY (tag_id) REFERENCES product_tags(tag_id)
                    )
                """)


                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS customers (
                        customer_id INT AUTO_INCREMENT PRIMARY KEY,
                        contact_number VARCHAR(20),
                        shipping_details TEXT
                    )
                """)

                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS orders (
                        order_id INT AUTO_INCREMENT PRIMARY KEY,
                        customer_id INT,
                        order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        status ENUM('pending', 'paid', 'shipped', 'completed', 'cancelled') DEFAULT 'pending',
                        payment_method VARCHAR(50),
                        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
                    )
                """)

                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS order_items (
                        order_item_id INT AUTO_INCREMENT PRIMARY KEY,
                        order_id INT,
                        product_id INT,
                        quantity INT NOT NULL,
                        unit_price DECIMAL(10, 2) NOT NULL,
                        FOREIGN KEY (order_id) REFERENCES orders(order_id),
                        FOREIGN KEY (product_id) REFERENCES products(product_id)
                    )
                """)

                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS customer_order_history (
                        history_id INT AUTO_INCREMENT PRIMARY KEY,
                        customer_id INT,
                        order_id INT,
                        FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
                        FOREIGN KEY (order_id) REFERENCES orders(order_id)
                    )
                """)

            connection.commit()
            print("Tables created successfully.")
        except pymysql.Error as e:
            print(f"Error creating tables: {e}")
        finally:
            connection.close()


if __name__ == "__main__":
    create_tables()
    