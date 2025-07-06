import mysql.connector
def get_connection():
    try:
        conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="xyz",
        database="library_db"
        )
        return conn
    except mysql.connector.error as er:
        print("Error while connecting to database:", er)
        return None

