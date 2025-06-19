# library/services.py

from datetime import datetime, timedelta
from .models import Book, User

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book: Book):
        self.books.append(book)

    def register_user(self, user: User):
        self.users.append(user)

    def checkout_book(self, isbn: str, username: str):
        book = next((b for b in self.books if b.isbn == isbn and b.borrower is None), None)
        user = next((u for u in self.users if u.username == username), None)

        if not book:
            raise ValueError("Book not available")
        if not user:
            raise ValueError("User not found")

        book.borrower = username
        book.due_date = datetime.now() + timedelta(days=14)
        user.borrowed_books.append(isbn)

    def return_book(self, isbn: str):
        book = next((b for b in self.books if b.isbn == isbn), None)
        if book and book.borrower:
            user = next((u for u in self.users if u.username == book.borrower), None)
            if user:
                user.borrowed_books.remove(isbn)
            book.borrower = None
            book.due_date = None
