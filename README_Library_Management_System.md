# 📚 Library Management System (Python -- Excel Based)

A console-based **Library Management System** developed in Python using
a modular structure and Excel for persistent storage.

This project demonstrates structured programming practices, file
handling, and real-world system design for managing books, members, and
transactions in a library environment.

------------------------------------------------------------------------

## 🚀 Project Overview

This system allows a librarian to:

-   Authenticate users (Login system)
-   Manage Books (Add, View, Delete, Update)
-   Manage Members
-   Issue and Return Books
-   Track Transactions
-   Generate Reports
-   Create Data Backups
-   Store all data in Excel files

The system is menu-driven and designed for clear terminal interaction.

------------------------------------------------------------------------

## 🗂️ Project Structure

    library management system/
    │
    ├── main.py              # Entry point of the application
    ├── login.py             # User authentication logic
    ├── books.py             # Book management module
    ├── members.py           # Member management module
    ├── transactions.py      # Issue and return logic
    ├── reports.py           # Reporting features
    ├── storage.py           # Excel data handling
    ├── backup.py            # Backup functionality
    ├── users.xlsx           # Excel data storage

------------------------------------------------------------------------

## 🧩 Module Description

### main.py

Controls overall program flow and connects all modules together.

### login.py

Handles user authentication and validates login credentials.

### books.py

Manages book records including adding, viewing, updating, and deleting.

### members.py

Handles member registration, viewing, and removal.

### transactions.py

Manages issuing and returning of books, and updates availability.

### reports.py

Generates reports and displays transaction summaries.

### storage.py

Handles reading and writing data to Excel files.

### backup.py

Creates backup copies of Excel data for safety.

------------------------------------------------------------------------

## 🛠️ Technologies Used

-   Python 3.x
-   Excel (.xlsx) for persistent storage
-   Modular programming structure
-   File handling and structured logic

------------------------------------------------------------------------

## ⚙️ How to Run

1.  Install Python 3.x\

2.  Install required library:

        pip install openpyxl

3.  Navigate to the project directory\

4.  Run:

        python main.py

------------------------------------------------------------------------

## 🎯 Key Features

✔ Console-based interactive menu\
✔ Persistent data storage using Excel\
✔ Modular design\
✔ Backup support\
✔ CRUD operations\
✔ Practical transaction handling

------------------------------------------------------------------------

## 🔮 Future Improvements

-   Convert to full OOP architecture\
-   Implement MVC pattern\
-   Replace Excel with SQLite\
-   Add role-based authentication\
-   Add unit testing\
-   Build GUI or Web version

------------------------------------------------------------------------

## 👨‍💻 Author

Developed as a practical implementation of a Library Management System
to demonstrate structured programming and real-world workflow
simulation.
