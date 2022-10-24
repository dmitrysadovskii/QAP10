class Book:
    def __init__(self, name, author, pages, isbn):
        self.name = name
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = False
        self.name_res = []


class User:
    def __init__(self, name):
        self.name = name
        self.book_list = []

    def take_book(self, book):
        if book.reserved is False:
            book.reserved = True
            self.book_list.append(book)
        elif book.reserved is True and book.name_res == self.name:
            book.reserved = True
            self.book_list.append(book)
        else:
            print('Книгу читает другой пользователь')

    def back_book(self, book):
        if book in self.book_list:
            book.reserved = False
            self.book_list.remove(book)

    def booking_book(self, book):
        if book.reserved is True:
            print('Книга уже зарезервирована')
        else:
            book.reserved = True
            book.name_res = self.name


book_a = Book('war and peace', 'L.Tolstoy', 1300, 556589222)
user_a = User('Lera')
user_b = User('Sasha')
user_a.take_book(book_a)
user_b.take_book(book_a)
