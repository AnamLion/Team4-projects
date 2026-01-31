# books.py
from models import Book

class BookManager:
    def __init__(self, storage):
        self.storage = storage
        self.sheet_name = "Books"

    def generate_book_id(self, ws):
        """Generates a simple incremental Book ID."""
        last_row = ws.max_row
        if last_row <= 1:
            return 101  # Start from 101
        last_id = ws.cell(row=last_row, column=1).value
        # Handle cases where cell might be None or not an int (if corrupted)
        try:
            return int(last_id) + 1
        except (TypeError, ValueError):
            return 101

    def add_book(self):
        """Adds a new book to Excel."""
        wb = self.storage.get_workbook()
        ws = self.storage.get_sheet(wb, self.sheet_name)

        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        
        while True:
            try:
                quantity = int(input("Enter Quantity: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number for Quantity.")

        book_id = self.generate_book_id(ws)
        book = Book(book_id, title, author, quantity)

        ws.append([
            book.book_id,
            book.title,
            book.author,
            book.quantity
        ])

        self.storage.save_workbook(wb)
        print(f"\n Book added successfully.")
        print(f"Book ID: {book.book_id}\n")

    def view_books(self):
        """Displays all books with Available, Issued, and Total counts."""
        wb = self.storage.get_workbook()
        ws = self.storage.get_sheet(wb, self.sheet_name)
        
        # Calculate Issued Counts from Transactions
        issued_counts = {}
        if "Transactions" in wb.sheetnames:
            ws_trans = wb["Transactions"]
            for row in ws_trans.iter_rows(min_row=2, values_only=True):
                # Row: TransactionID, MemberID, BookID, IssueDate, ReturnDate, Fine
                if len(row) >= 5:
                    book_id = str(row[2])
                    return_date = row[4]
                    if return_date is None or return_date == "":
                        issued_counts[book_id] = issued_counts.get(book_id, 0) + 1

        print("\n LIBRARY BOOKS \n")
        if ws.max_row <= 1:
            print("No books found.\n")
            return

        for row in ws.iter_rows(min_row=2, values_only=True):
            if not any(row): continue # Skip empty rows
            book_id, title, author, quantity = row
            
            available_qty = quantity
            issued_qty = issued_counts.get(str(book_id), 0)
            total_qty = available_qty + issued_qty
            
            print(
                f"ID: {book_id} | "
                f"Title: {title} | "
                f"Author: {author} | "
                f"Available: {available_qty} | Issued: {issued_qty} | Total: {total_qty}"
            )
        print()

    def search_book(self):
        """Searches for a book by BookID or Title."""
        wb = self.storage.get_workbook()
        ws = self.storage.get_sheet(wb, self.sheet_name)

        search_query = input("Enter Book ID or Title to search: ").lower()
        found = False

        print("\nSearch Results:")
        for row in ws.iter_rows(min_row=2, values_only=True):
            if not any(row): continue
            book_id, title, author, quantity = row
            if str(book_id) == search_query or search_query in str(title).lower():
                print(f"ID: {book_id} | Title: {title} | Author: {author} | Qty: {quantity}")
                found = True

        if not found:
            print("No matching book found.")
        print()

    def delete_book(self):
        """Deletes a book from Excel by BookID."""
        wb = self.storage.get_workbook()
        ws = self.storage.get_sheet(wb, self.sheet_name)

        delete_id = input("Enter Book ID to delete: ")
        found = False
        rows_to_keep = []

        for row in ws.iter_rows(min_row=2, values_only=True):
            if not any(row): continue
            book_id = str(row[0])
            if book_id != delete_id:
                rows_to_keep.append(row)
            else:
                found = True

        if not found:
            print("\n Book not found.\n")
            return

        # Clear existing data (except header)
        ws.delete_rows(2, ws.max_row)
        for row in rows_to_keep:
            ws.append(list(row))

        self.storage.save_workbook(wb)
        print("\nBook deleted successfully.\n")

    def books_menu(self):
        """Displays the Books menu and routes user choices."""
        while True:
            print("BOOKS MENU")
            print("1. Add Book")
            print("2. View Books")
            print("3. Search Book")
            print("4. Delete Book")
            print("5. Back to Main Menu")

            choice = input("Enter choice: ")
            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.view_books()
            elif choice == "3":
                self.search_book()
            elif choice == "4":
                self.delete_book()
            elif choice == "5":
                break
            else:
                print("\n Invalid choice. Try again.\n")