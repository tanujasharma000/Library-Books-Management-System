from books_operations import *
from issued_books import *

def main_menu():
    while True:
        print("\n===== Library Books Management System =====")
        print("1. Add Book")
        print("2. Display All Books")
        print("3. Search Book by Title")
        print("4. Search Book by Author")
        print("5. Sort Books")
        print("6. Delete Book")
        print("7. Update Book Info")
        print("8. Issue Book")
        print("9. Return Book")
        print("10. Show Issued Books")
        print("11. Show Issue Summary (by Person)")
        print("12. Add Copies to Book")
        print("13. Generate Report")
        print("14. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            add_books()
        elif choice == '2':
            display_books()
        elif choice == '3':
            search_books_by_title()
        elif choice == '4':
            search_books_by_author()
        elif choice == '5':
            sort_books()
        elif choice == '6':
            delete_book()
        elif choice == '7':
            update_book()
        elif choice == '8':
            issue_book()
        elif choice == '9':
            return_book()
        elif choice == '10':
            show_issued_books()
        elif choice == '11':
            show_issued_summary()
        elif choice == '12':
            add_copies_to_book()
        elif choice == '13':
            generate_report()
        elif choice == '14':
            print("Exiting Program... Bye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

