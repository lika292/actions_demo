
import unittest
from src.library import Book, PrintedBook, EBook, User, Librarian, Library


class TestLibrary(unittest.TestCase):

    def test_book_availability(self):
        book = Book("Test", "Author", 2000)
        self.assertTrue(book.is_available())

        book.mark_as_taken()
        self.assertFalse(book.is_available())

        book.mark_as_returned()
        self.assertTrue(book.is_available())

    def test_user_borrow_return(self):
        user = User("Alice")
        book = Book("Book", "Author", 2020)

        msg1 = user.borrow(book)
        self.assertIn("взял(а) книгу", msg1)
        self.assertFalse(book.is_available())

        msg2 = user.return_book(book)
        self.assertIn("вернул(а)", msg2)
        self.assertTrue(book.is_available())

    def test_library_lend_book(self):
        lib = Library()
        user = User("Bob")
        book = Book("Python", "Guido", 1991)

        lib.add_user(user)
        lib.add_book(book)

        res = lib.lend_book("Python", "Bob")
        self.assertIn("взял(а) книгу", res)
        self.assertFalse(book.is_available())

    def test_ebook_download(self):
        ebook = EBook("Digital", "Anon", 2021, 5, "pdf")
        msg = ebook.download()
        self.assertIn("загружается", msg)


if __name__ == "__main__":
    unittest.main()
