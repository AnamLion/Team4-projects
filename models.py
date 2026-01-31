# models.py

class Book:
    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity

    def __str__(self):
        return f"ID: {self.book_id} | Title: {self.title} | Author: {self.author} | Qty: {self.quantity}"

class Member:
    def __init__(self, member_id, name, phone, books_issued=0):
        self.member_id = member_id
        self.name = name
        self.phone = phone
        self.books_issued = books_issued

    def __str__(self):
        return f"ID: {self.member_id} | Name: {self.name} | Phone: {self.phone} | Books Issued: {self.books_issued}"

class Transaction:
    def __init__(self, transaction_id, member_id, book_id, issue_date, return_date=None, fine=0):
        self.transaction_id = transaction_id
        self.member_id = member_id
        self.book_id = book_id
        self.issue_date = issue_date
        self.return_date = return_date
        self.fine = fine

    def __str__(self):
        return (f"Trans ID: {self.transaction_id} | Member: {self.member_id} | "
                f"Book: {self.book_id} | Issued: {self.issue_date} | "
                f"Returned: {self.return_date or 'N/A'} | Fine: {self.fine}")
