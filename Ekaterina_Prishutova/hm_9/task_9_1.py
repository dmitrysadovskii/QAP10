class Book:

    def __init__(self, name, author, pages, isbn):
        self.name = name
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.flag_reserve = 0


class User:

    def __init__(self, name):
        self.name = name
        self.books = []
        self.reserved_books = []

    def reserve_book(self, book):
        if book.flag_reserve == 0:
            self.reserved_books.append(book)
            book.flag_reserve = 1
        else:
            print("Книга уже зарезервирована")

    def take_a_book(self, book):
        if book.flag_reserve == 0 or self.reserved_books.count(book) > 0:
            self.books.append(book)
            book.flag_reserve = 1
        else:
            print("Книга уже зарезервирована")

    def return_book(self, book):
        if self.books.count(book) > 0:
            self.books.remove(book)
            book.flag_reserve = 0
        elif self.reserved_books.count(book) > 0:
            self.reserved_books.remove(book)
            book.flag_reserve = 0
        else:
            print("Книга не принадлежит пользователю")
