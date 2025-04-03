import pymysql

# 本地或者云数据库
def get_db_connection():
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='0m9n8b7v6c',
            database='comp7640db233',
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection
    except pymysql.Error as e:
        print(f"Database connection error: {e}")
        return None
    
