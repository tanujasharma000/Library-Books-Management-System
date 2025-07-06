# 📚 Library Books Management System  

A Python command-line application for managing library books and tracking issuances using MySQL.  

**Developer**: Tanuja Sharma | BCA 2nd Semester  
**Latest Update**: Implemented secure database credential handling  

---

## ✨ Features  
### Book Operations  
- Add new books & update existing  
- Search/sort by title/author  
- Delete books (only if not issued)  
- Add copies to existing books  
### Issuance Management  
- Issue/return books with date tracking  
- View issued books (person-wise summary)  
### Reporting  
- Generate reports: total/issued/available books  

---

## ⚙️ Tech Stack  
- **Backend**: Python 3  
- **Database**: MySQL  
- **Dependencies**:  
  ```bash
  mysql-connector-python 
  python-dotenv  # For secure credentials
  
🗂️ Project Structure

File	and Purpose

main.py ->	Main application menu

books_operations.py ->	Book CRUD operations

issued_books.py ->	Handle issuances/returns/reports

db_connect2.py ->	Secure database connection setup

.env ->Stores credentials (gitignored)


🚀 Setup Guide

1. Database Preparation
   
sql

CREATE DATABASE library_db;

USE library_db;

CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    total_copies INT NOT NULL,
    available_copies INT NOT NULL
);

CREATE TABLE issued_books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT NOT NULL,
    issued_to VARCHAR(255) NOT NULL,
    issue_date DATE NOT NULL,
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);

2. Configure Environment
   
Create .env file:

ini

DB_HOST="localhost"

DB_USER="root"

DB_PASSWORD="your_actual_password"  

DB_NAME="library_db"

Add to .gitignore:

.gitignore

.env

__pycache__/

3. Install & Run
bash
# Install dependencies
pip install mysql-connector-python python-dotenv

# Run application
python main.py
