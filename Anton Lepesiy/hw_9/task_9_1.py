class Book:
    def __init__(self, name, author, pages, isbn):
        self.name = name
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = False        # статус резервации пользователем
        self.availability = True        # статус доступности в библиотеке


class User:
    def __init__(self, name):
        self.name = name
        self.list_of_books_read = []
        self.list_of_reserved_books = []

    def reservation_of_the_book(self, book):
        assert book.reserved is False, 'Книга уже зарезервирована'
        assert book.availability is True, 'Книгу читает другой пользователь'
        self.list_of_reserved_books.append(book)
        book.reserved = True

    def take_the_book(self, book):
        assert book.reserved is False, 'Книга уже зарезервирована'
        assert book.availability is True, 'Книгу читает другой пользователь'
        self.list_of_books_read.append(book)
        book.availability = False
        book.reserved = False

    def return_the_book(self, book):
        if book in self.list_of_books_read:
            book.availability = True
            self.list_of_books_read.remove(book)
        else:
            print('У пользователя нет такой книги')

    def dereservation(self, book):
        if book in self.list_of_reserved_books:
            book.reserved = False
            self.list_of_reserved_books.remove(book)
        else:
            print('Пользователь не резервировал такой книги')


book_1 = Book("Сабакі Эўропы", "Альгерд Бахарэвіч", 676, 978-80-908687-2-4)
book_2 = Book('Diuna', 'Frank Herbert', 777, 978-83-8188-138-8)
user_1 = User('Anton')
user_2 = User('Krystsina')
user_3 = User('Vlada')

user_1.reservation_of_the_book(book_1)
user_2.take_the_book(book_2)
user_3.take_the_book(book_2)
