class Book:
    def __init__(self, title="unknown", author="unknown"):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self._books = []
    def add_book(self, books):
        self._books.append(books)
    def list_available_books(self):
        return f"Available books after setup: {self._books}"
    def check_out_book(self, title):
        if title in self._books:
            self._books.remove(title)
            return f"\nAvailable books after checking out '{title}': {self._books}"
        else:
            return f"{title} is unavailable"
    def return_book(self, title):
        self._books.append(title)
        return f"\nAvailable books after returning '{title}': {self._books}"