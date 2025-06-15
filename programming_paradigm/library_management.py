class Book:
    def __init__(self, title="unknown", author="unknown"):
        self.title = title
        self.author = author
        self._is_checked_out = False

class Library(Book):
    def __init__(self):
        self._books = []

    def add_book(self, books):
        self._books.append(books)

    def list_available_books(self):
       return self._books
    
    def check_out_book(self, title):
        if title in self._books:
            self._books.remove(title)
            self._is_checked_out = True
        return self._is_checked_out

    def return_book(self, title):
        if self._is_checked_out == True:
            self._books.append(title)
            self._is_checked_out = False
