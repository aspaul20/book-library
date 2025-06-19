from booklib import Library, Book
from booklib import User
from datetime import datetime
import pytest

def test_services_func():

     book1 = Book(title="Book 1", author="Stephen King", isbn="123")

     library = Library()
     library.add_book(book1)

     user1 = User(username="user1")

     library.register_user(user1)

     library.checkout_book(isbn="123", username="user1")
     assert "123" in user1.borrowed_books
     assert isinstance(book1.due_date, datetime)
     assert book1.borrower == user1.username

     library.return_book(isbn="123")
     assert "123" not in user1.borrowed_books
     assert book1.due_date is None
     assert book1.borrower is None

def test_services_exception():
     book1 = Book(title="Book 1", author="Stephen King", isbn="123")
     user1 = User(username="user1")
     user2 = User(username="user2")

     library = Library()
     library.add_book(book1)
     library.register_user(user1)
     library.register_user(user2)

     with pytest.raises(ValueError, match="User not found"):
          library.checkout_book(isbn="123", username="user5")

     library.checkout_book(isbn="123", username="user1")
     with pytest.raises(ValueError, match="Book not available"):
          library.checkout_book(isbn="123", username="user2")