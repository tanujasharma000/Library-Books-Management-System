# Library Books Management System

A command-line project built using Python and MySQL to manage books in a library.  
Developed by **Tanuja Sharma** | BCA 2nd Semester

---

## Features

- Add new books
- Display all books
- Search books by title or author
- Sort books by title or author
- Update book information
- Delete books (only if not currently issued)
- Issue books to a person
- Return issued books
- Show all issued books
- Show issued summary (person-wise)
- Generate report (total, issued, available)
- Add more copies to an existing book

---

## Tech Stack

- **Programming Language:** Python 3.x  
- **Database:** MySQL  
- **Connector:** mysql-connector-python

---

Project Structure

main_.py – Main menu and user options

books_operations.py – Handles all book-related operations (add, delete, search, sort)

issued_books.py – Issue, return, summary, and report generation for issued books

db_connect2.py – MySQL database connection setup

README.md – Project documentation


---

## How to Run

### Prerequisites

- Python 3.x
- MySQL Server installed and running
- Install connector library using:

```bash
pip install mysql-connector-python
Steps to Run
Create a MySQL database (e.g., library_db) and required tables (books, issued_books)

Update database credentials in db_connect2.py

Run the main script:
python main.py


# MySQL Table Schema
-books
Column	and Type
book_id (PK)	INT AUTO_INCREMENT
title	VARCHAR(255)
author	VARCHAR(255)
total_copies	INT
available_copies	INT

-issued_books
Column	and Type
id (PK)	INT AUTO_INCREMENT
book_id (FK)	INT
issued_to	VARCHAR(255)
issue_date	DATE

Author
Tanuja Sharma 
BCA Student exploring backend development using Python and MySQL

