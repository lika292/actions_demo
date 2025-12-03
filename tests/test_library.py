import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main import Book, PrintedBook, EBook, User, Library, Librarian


class TestBook(unittest.TestCase):
    def test_book_creation(self):
        book = Book("1984", "Джордж Оруэлл", 1949)
        self.assertEqual(book.get_title(), "1984")
        self.assertEqual(book.get_author(), "Джордж Оруэлл")
        self.assertEqual(book.get_year(), 1949)
        self.assertTrue(book.is_available())

    def test_book_availability(self):
        book = Book("Test Book", "Author", 2024)
        self.assertTrue(book.is_available())
        book.mark_as_taken()
        self.assertFalse(book.is_available())
        book.mark_as_returned()
        self.assertTrue(book.is_available())


class TestPrintedBook(unittest.TestCase):
    def test_printed_book_creation(self):
        pbook = PrintedBook("Война и мир", "Л. Толстой", 1869, 1225, "хорошая")
        self.assertEqual(pbook.pages, 1225)
        self.assertEqual(pbook.condition, "хорошая")
        self.assertEqual(pbook.get_title(), "Война и мир")

    def test_repair_method(self):
        pbook = PrintedBook("Книга", "Автор", 2000, 300, "плохая")
        pbook.repair()
        self.assertEqual(pbook.condition, "хорошая")
        pbook.repair()
        self.assertEqual(pbook.condition, "новая")


class TestEBook(unittest.TestCase):
    def test_ebook_creation(self):
        ebook = EBook("Питон для начинающих", "И. Иванов", 2023, 5.2, "PDF")
        self.assertEqual(ebook.file_size, 5.2)
        self.assertEqual(ebook.format, "PDF")

    def test_download_method(self):
        ebook = EBook("Книга", "Автор", 2024, 10.5, "EPUB")
        try:
            ebook.download()
            success = True
        except Exception:
            success = False
        self.assertTrue(success)


class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = User("Анна")
        self.assertEqual(user.name, "Анна")
        self.assertEqual(user.get_borrowed_books(), ())

    def test_borrow_and_return_book(self):
        user = User("Иван")
        book = Book("Книга", "Автор", 2024)
        user.borrow(book)
        self.assertFalse(book.is_available())
        self.assertEqual(len(user.get_borrowed_books()), 1)
        user.return_book(book)
        self.assertTrue(book.is_available())
        self.assertEqual(len(user.get_borrowed_books()), 0)


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book1 = Book("Книга 1", "Автор 1", 2000)
        self.book2 = Book("Книга 2", "Автор 2", 2010)
        self.user = User("Анна")

    def test_add_and_remove_book(self):
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.remove_book("Книга 1")
        self.library.remove_book("Несуществующая книга")

    def test_add_and_find_user(self):
        self.library.add_user(self.user)
        found_user = self.library.find_user("Анна")
        self.assertIsNotNone(found_user)
        self.assertEqual(found_user.name, "Анна")

    def test_find_book(self):
        self.library.add_book(self.book1)
        found_book = self.library.find_book("Книга 1")
        self.assertIsNotNone(found_book)
        self.assertEqual(found_book.get_title(), "Книга 1")

    def test_lend_and_return_book(self):
        self.library.add_book(self.book1)
        self.library.add_user(self.user)
        self.library.lend_book("Книга 1", "Анна")
        self.assertFalse(self.book1.is_available())
        self.library.return_book("Книга 1", "Анна")
        self.assertTrue(self.book1.is_available())


class TestLibrarian(unittest.TestCase):
    def test_librarian_inheritance(self):
        librarian = Librarian("Библиотекарь")
        self.assertIsInstance(librarian, User)

    def test_librarian_methods(self):
        librarian = Librarian("Иван")
        library = Library()
        book = Book("Книга", "Автор", 2024)
        user = User("Анна")
        try:
            librarian.add_book(library, book)
            librarian.register_user(library, user)
            librarian.remove_book(library, "Книга")
            success = True
        except Exception:
            success = False
        self.assertTrue(success)


if __name__ == "__main__":
    unittest.main()
