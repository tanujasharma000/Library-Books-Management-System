from db_connect2 import get_connection

def display_books():
    conn=get_connection()
    print("Connected to database successfully!")
    if conn:
        cursor=conn.cursor()
        try:
            
            cursor.execute("select*from books")
            rows=cursor.fetchall()
            if rows:
                for row in rows:
                    print(row)
            else:
                print("No books found!!")
            
        except Exception as e:
            print("Exception caught while displaying books: ",e)
        
        finally:
            cursor.close()
            conn.close()

    else:
        print("database connection failed...")


def add_books():
    conn=get_connection()
    if conn:
        try:
            cursor=conn.cursor()
            title=input("Enter the title of book: ")
            author=input("Enter the author name: ")
            available_copies=int(input("Enter the number of available books: "))
            total_copies=int(input("Enter the number of total books: "))
            insert_query="insert into books (title,author,total_copies,available_copies) values(%s ,%s ,%s, %s)"
            data=(title, author, total_copies, available_copies)

            cursor.execute(insert_query,data)
            conn.commit()

            print("books added successfully..hehe")

        except Exception as e:
            print("Error inserting book:",e)

        finally:
            cursor.close()
            conn.close()
    else:
        print("database connection failed! :(")


def delete_book():
    conn=get_connection()
    if conn:
        
        try:
            cursor=conn.cursor()
            book_id=int(input("Enter book id to delete: "))
            cursor.execute("select *from books where book_id= %s",(book_id,))
            book=cursor.fetchall()

            if book:

                cursor.execute("select *from issued_books where book_id= %s",(book_id,))
                issued=cursor.fetchall()
            
                if issued:
                    print("book issued by someone...can't delete the data..")

                else:
                   
                   cursor.execute("delete from books where book_id=%s",(book_id,))
                   conn.commit()
                   print("book deleted successfully")
            else:
                print("book not found")

        except Exception as e:
            print("Error deleting book",e)

        finally:
            cursor.close()
            conn.close()

    else:
        print("error connecting database :( ")

def search_books_by_title():
    conn=get_connection()
    if conn:
        try:
            cursor=conn.cursor()
            title=input("Enter the book title to search: ")
            query="select* from books where title like %s"
            cursor.execute(query,('%'+title+'%',))
            rows=cursor.fetchall()

            if rows:
                for row in rows:
                    print(row)
            else:
                print("no books found for this title")

        except Exception as e:
            print("Error searching file: ",e)
        finally:
            cursor.close()
            conn.close()
    else:
        print("failed to connect database :( ")


def search_books_by_author():
    conn=get_connection()
    if conn:
        try:
            cursor=conn.cursor()
            author=input("Enter the book author to search: ")
            query="select* from books where author like %s"
            cursor.execute(query,('%'+author+'%',))
            rows=cursor.fetchall()

            if rows:
                for row in rows:
                    print(row)
            else:
                print("no books found for this title")

        except Exception as e:
            print("Error searching file: ",e)
        finally:
            cursor.close()
            conn.close()
    else:
        print("failed to connect database :( ")

def sort_books():
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()

            print("Sort by:")
            print("1. Title")
            print("2. Author")
            choice = input("Enter your choice (1 or 2): ")

            if choice == '1':
                cursor.execute("SELECT * FROM books ORDER BY title ASC")
            elif choice == '2':
                cursor.execute("SELECT * FROM books ORDER BY author ASC")
            else:
                print("Invalid choice!")
                return

            rows = cursor.fetchall()
            if rows:
                print("Sorted Books:")
                for row in rows:
                    print(row)
            else:
                print("No books found to sort.")

        except Exception as e:
            print("Error while sorting books:", e)
        finally:
            cursor.close()
            conn.close()
    else:
        print("Database connection failed!")
  


def update_book():
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()

            book_id = int(input("Enter Book ID to update: "))
            cursor.execute("SELECT * FROM books WHERE book_id = %s", (book_id,))
            book = cursor.fetchone()

            if book:
                print("Current Book Details:")
                print(book)

                title = input("Enter new title (leave blank to keep current): ")
                author = input("Enter new author (leave blank to keep current): ")
                total = input("Enter new total copies (leave blank to keep current): ")
                available = input("Enter new available copies (leave blank to keep current): ")

                
                title = title if title else book[1]
                author = author if author else book[2]
                total = int(total) if total else book[3]
                available = int(available) if available else book[4]

                update_query = "UPDATE books SET title = %s, author = %s, total_copies = %s, available_copies = %s WHERE book_id = %s"
                
                cursor.execute(update_query, (title, author, total, available, book_id))
                conn.commit()
                print("Book updated successfully!")
            else:
                print("Book not found!")

        except Exception as e:
            print("Error updating book:", e)
        finally:
            cursor.close()
            conn.close()
    else:
        print("Database connection failed!")
