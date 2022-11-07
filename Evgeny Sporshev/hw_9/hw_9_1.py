# Библиотека
class Book:
    def __init__(self, title, author, pages, isbn, reserved):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = reserved


class Reader:
    def __init__(self, name):
        self.books = list()
        self.name = name

    def add_book(self, book):
        if book.reserved:
            print(f'Книга "{book.title}" уже взята другим читателем.')
        else:
            self.books.append(book)
            book.reserved = True
            print(f'Книга "{book.title}" успешно выдана читателю {self.name}.')

    def remove_book(self, book):
        if book.reserved:
            book.reserved = False
            print(f'Книга "{book.title}" вернулась в библиотеку')
        else:
            print(f'Книга "{book.title}" вернуть нельзя, она и так свободна')


Book_one = Book('Зов Ктулху', 'Говард Лавкрафт', 416, '978-5-17-099202-7', False)
Book_two = Book('Некрономикон. Книга запретных тайн', 'Говард Лавкрафт', 416, '978-5-17-119689-9', False)
Book_three = Book('Тайная страсть', 'Джоанна Линдсей', 320, '978-5-17-150218-8', False)

jenya = Reader('Женя')
jenya.add_book(Book_one)
jenya.add_book(Book_two)
olesya = Reader('Олеся')
olesya.add_book(Book_one)
olesya.add_book(Book_two)
olesya.remove_book(Book_three)
olesya.add_book(Book_three)
jenya.remove_book(Book_two)
