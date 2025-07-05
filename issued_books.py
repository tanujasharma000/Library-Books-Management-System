from db_connect2 import get_connection
import datetime

def issue_book():
    conn= get_connection()
    if conn:
        try:
            cursor= conn.cursor()
            book_id= int(input("Enter Book ID to issue: "))
            issued_to= input("Enter name of person: ")

            cursor.execute("SELECT available_copies FROM books WHERE book_id = %s", (book_id,))
            result= cursor.fetchone()

            if result and result[0] > 0:
               
                cursor.execute("UPDATE books SET available_copies = available_copies - 1 WHERE book_id = %s", (book_id,))

                issue_date= datetime.date.today().strftime('%Y-%m-%d')
                cursor.execute(  "INSERT INTO issued_books (book_id, issued_to, issue_date) VALUES (%s, %s, %s)",
                    (book_id, issued_to, issue_date)  )

                conn.commit()
                print("Book issued successfully!")

            elif result:
                print("No available copies of this book.")
            else:
                print("Book not found.")

        except Exception as e:
            print("Error while issuing book:", e)
        finally:
            cursor.close()
            conn.close()
    else:
        print("Database connection failed.")


def return_book():
    conn=get_connection()
    if conn:
        try:
            cursor=conn.cursor()
            book_id = int(input("Enter Book ID to return: "))
            issued_to = input("Enter name of person returning: ")
            cursor.execute("SELECT * FROM issued_books WHERE book_id = %s AND issued_to = %s", (book_id, issued_to))
            result= cursor.fetchone()
            if result:
                cursor.execute("update books set available_books=available_books+1 where book_id=%s",(book_id,))
                cursor.execute("delete from books where book_id=%s and issed_to =%s",(book_id,issued_to))
                conn.commit()
                print("Book returned successfully!")
            else:
                print("This book was not issued to this person.")

        except Exception as e:
            print("Error while returning book:", e)
        finally:
            cursor.close()
            conn.close()
    else:
        print("Database connection failed.")

def show_issued_books():
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query="select ib.book_id , b.title, ib.issued_to, ib.issue_date From issued_books ib Join books b on ib.book_id=b.book_id Order by issue_date desc"
            cursor.execute(query)
            rows=cursor.fetchall()
            if rows:
                print("Issued Books:")
                for row in rows:
                    print(f"Book ID: {row[0]} | Title: {row[1]} | Issued To: {row[2]} | Date: {row[3]}")
            else:
                print("No books currently issued.")

        except Exception as e:
            print("Error while fetching issued books:", e)
        finally:
            cursor.close()
            conn.close()
    else:
        print("Database connection failed.")


def show_issued_summary():
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()

            query = "select issued_to ,count(*) as Total_issued from issued_books group by issued_to order by total_issued desc"
            cursor.execute(query)
            rows = cursor.fetchall()

            if rows:
                print("Books issued summary:")
                for row in rows:
                    print(f"{row[0]} - {row[1]} book(s) issued")
            else:
                print("No books are currently issued to anyone.")

        except Exception as e:
            print("Error while generating summary:", e)
        finally:
            cursor.close()
            conn.close()
    else:
        print("Database connection failed.")

from db_connect2 import get_connection

def add_copies_to_book():
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()

            book_id = int(input("Enter Book ID to add copies: "))
            cursor.execute("SELECT * FROM books WHERE book_id = %s", (book_id,))
            book = cursor.fetchone()

            if book:
                print("Current Book Info:")
                print(f"Title: {book[1]}, Author: {book[2]}")
                print(f"Total Copies: {book[3]}, Available Copies: {book[4]}")

                add_count = int(input("How many copies do you want to add?= "))

                cursor.execute(" UPDATE books  SET total_copies = total_copies + %s, available_copies = available_copies + %s WHERE book_id = %s", (add_count, add_count, book_id))

                conn.commit()
                print(f"{add_count} copies added successfully!")

            else:
                print("Book not found!")

        except Exception as e:
            print("Error while adding copies:", e)
        finally:
            cursor.close()
            conn.close()
    else:
        print("Database connection failed.")


from db_connect2 import get_connection

def generate_report():
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT SUM(total_copies) FROM books")
            total_books = cursor.fetchone()[0] or 0
            cursor.execute("SELECT SUM(available_copies) FROM books")
            available_books = cursor.fetchone()[0] or 0
            cursor.execute("SELECT COUNT(*) FROM issued_books")
            issued_books = cursor.fetchone()[0]

            print("\n LIBRARY REPORT ")
            print(f"Total Books (All Copies): {total_books}")
            print(f"Total Available Copies: {available_books}")
            print(f"Total Issued Books: {issued_books}")

        except Exception as e:
            print("Error while generating report:", e)
        finally:
            cursor.close()
            conn.close()
    else:
        print("Database connection failed.")
