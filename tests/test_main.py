import unittest
from unittest.mock import patch
import io
from src.library import Book, EBook, Library, User

class TestLibrary(unittest.TestCase):

    def setUp(self):
        # Создаём библиотеку и пользователя
        self.library = Library()
        self.user = User("Alice")
        self.library.add_user(self.user)

        # Создаём обычную книгу и электронную
        self.book = Book("Book Title", "Author Name", 2023)
        self.library.add_book(self.book)

        self.ebook = EBook("Digital", "Digital Author", 2024, 5.0, "PDF")
        self.library.add_book(self.ebook)

    def test_book_availability(self):
        # Проверяем, что книга добавлена в библиотеку
        with patch('sys.stdout', new_callable=io.StringIO) as fake_out:
            self.library.show_available_books()
            output = fake_out.getvalue()
            self.assertIn(self.book.get_title(), output)
            self.assertIn(self.ebook.get_title(), output)

    def test_ebook_download(self):
        # Проверяем, что при скачивании выводится сообщение
        with patch('sys.stdout', new_callable=io.StringIO) as fake_out:
            self.ebook.download()
            output = fake_out.getvalue()
            self.assertIn("загружается", output)

    def test_library_lend_book(self):
        # Проверяем, что библиотека выдаёт книгу пользователю
        with patch('sys.stdout', new_callable=io.StringIO) as fake_out:
            self.library.lend_book(self.book.get_title(), self.user.name)
            output = fake_out.getvalue()
            self.assertIn("взял(а) книгу", output)

    def test_user_borrow_return(self):
        # Пользователь берёт книгу
        with patch('sys.stdout', new_callable=io.StringIO) as fake_out:
            self.user.borrow(self.book)
            output_borrow = fake_out.getvalue()
            self.assertIn("взял(а) книгу", output_borrow)

        # Пользователь возвращает книгу
        with patch('sys.stdout', new_callable=io.StringIO) as fake_out:
            self.user.return_book(self.book)
            output_return = fake_out.getvalue()
            self.assertIn("вернул(а) книгу", output_return)


if __name__ == "__main__":
    unittest.main()
