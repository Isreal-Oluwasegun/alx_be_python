from library_management import Book, Library
import unittest

class Book(unittest.TestCase):
    def setUp(self):
        self.book = Book()
        self.library = Library()
    def test_book(self):
        self.assertIsInstance(self.book, Book)