import mysql.connector
import os 

def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv("DB_PASSWORD"), 
            database="library_db"
        )
        return conn
    except mysql.connector.Error as er: 
        print(f"Database connection failed: {er}")
        return None

