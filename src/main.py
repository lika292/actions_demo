class Book:
    def __init__(self, title, author, year):
        self.__title = title
        self.__author = author
        self.__year = year
        self.__available = True

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_year(self):
        return self.__year

    def is_available(self):
        return self.__available

    def mark_as_taken(self):
        self.__available = False

    def mark_as_returned(self):
        self.__available = True

    def __str__(self):
        return f"{self.__title} — {self.__author}, {self.__year} " \
               f"({'доступна' if self.__available else 'занята'})"

class PrintedBook(Book):
    def __init__(self, title, author, year, pages, condition):
        super().__init__(title, author, year)
        self.pages = pages
        self.condition = condition

    def repair(self):
        if self.condition == "плохая":
            self.condition = "хорошая"
        elif self.condition == "хорошая":
            self.condition = "новая"

    def __str__(self):
        base = super().__str__()
        return f"{base} | стр: {self.pages}, состояние: {self.condition}"

class EBook(Book):
    def __init__(self, title, author, year, file_size, format):
        super().__init__(title, author, year)
        self.file_size = file_size
        self.format = format

    def download(self):
        print(f"Книга «{self.get_title()}» загружается...")

    def __str__(self):
        base = super().__str__()
        return f"{base} | файл: {self.file_size} МБ, формат: {self.format}"

class User:
    def __init__(self, name):
        self.name = name
        self.__borrowed_books = []

    def borrow(self, book):
        if book.is_available():
            book.mark_as_taken()
            self.__borrowed_books.append(book)
            print(f"{self.name} взял(а) книгу «{book.get_title()}»")
        else:
            print(f"Книга «{book.get_title()}» недоступна!")

    def return_book(self, book):
        if book in self.__borrowed_books:
            book.mark_as_returned()
            self.__borrowed_books.remove(book)
            print(f"{self.name} вернул(а) книгу «{book.get_title()}»")

    def show_books(self):
        if not self.__borrowed_books:
            print(f"{self.name} не имеет взятых книг.")
        else:
            print(f"Книги пользователя {self.name}:")
            for b in self.__borrowed_books:
                print(b.get_title())

    def get_borrowed_books(self):
        return tuple(self.__borrowed_books)

class Librarian(User):
    def add_book(self, library, book):
        library.add_book(book)

    def remove_book(self, library, title):
        library.remove_book(title)

    def register_user(self, library, user):
        library.add_user(user)

class Library:
    def __init__(self):
        self.__books = []
        self.__users = []

    def add_book(self, book):
        self.__books.append(book)
        print(f"Добавлена книга: {book.get_title()}")

    def remove_book(self, title):
        for b in self.__books:
            if b.get_title() == title:
                self.__books.remove(b)
                print(f"Книга «{title}» удалена.")
                return
        print(f"Книга «{title}» не найдена.")

    def add_user(self, user):
        self.__users.append(user)
        print(f"Добавлен пользователь: {user.name}")

    def find_user(self, name):
        for u in self.__users:
            if u.name == name:
                return u
        return None

    def find_book(self, title):
        for b in self.__books:
            if b.get_title() == title:
                return b
        return None

    def show_all_books(self):
        print("Все книги:")
        for b in self.__books:
            print(b)

    def show_available_books(self):
        print("Доступные книги:")
        for b in self.__books:
            if b.is_available():
                print(b)

    def lend_book(self, title, user_name):
        book = self.find_book(title)
        user = self.find_user(user_name)

        if not book:
            print("Книга не найдена!")
            return
        if not user:
            print("Пользователь не найден!")
            return

        user.borrow(book)

    def return_book(self, title, user_name):
        book = self.find_book(title)
        user = self.find_user(user_name)

        if not book or not user:
            print("Ошибка возврата!")
            return

        user.return_book(book)
