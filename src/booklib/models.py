# library/models.py

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass
class Book:
    title: str
    author: str
    isbn: str
    borrower: Optional[str] = None
    due_date: Optional[datetime] = None

@dataclass
class User:
    username: str
    borrowed_books: list = field(default_factory=list)
