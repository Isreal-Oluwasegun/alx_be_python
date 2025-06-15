# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book._is_checked_out = True
                return
        print(f"'{title}' is not available for checkout.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book._is_checked_out = False
                return
        print(f"'{title}' cannot be returned (not found or already available).")

    def list_available_books(self):
        available = [f"{book.title} by {book.author}" for book in self._books if not book._is_checked_out]
        if not available:
            print("No books are currently available.")
        else:
            for book in available:
                print(book)
