import pymysql
from database.db_connection import get_db_connection


class VendorService:
    def get_all_vendors(self):
        connection = get_db_connection()
        if connection:
            try:
                with connection.cursor() as cursor:
                    sql = "SELECT * FROM vendors"
                    cursor.execute(sql)
                    return cursor.fetchall()
            except pymysql.Error as e:
                print(f"Error getting vendors: {e}")
            finally:
                connection.close()
        return []

    def create_vendor(self, business_name, customer_feedback_score=None, geographical_presence=None):
        connection = get_db_connection()
        if connection:
            try:
                with connection.cursor() as cursor:
                    sql = "INSERT INTO vendors (business_name, customer_feedback_score, geographical_presence) VALUES (%s, %s, %s)"
                    cursor.execute(sql, (business_name, customer_feedback_score, geographical_presence))
                connection.commit()
                print("Vendor created successfully.")
            except pymysql.Error as e:
                print(f"Error creating vendor: {e}")
            finally:
                connection.close()