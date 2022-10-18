class Book:

    def __init__(self, name: str, author: str, pages: int, isbn: int, reserved=False):
        self.name = name
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = reserved


class Visitor:

    def __init__(self, visitor_name: str):
        self.visitor_name = visitor_name
        self.taken_lst = list()

    def get_book(self, book):
        if book not in self.taken_lst and book.reserved is False:
            self.taken_lst.append(book)
        else:
            print(f'{self.visitor_name} не может взять {book.name}')

    def reserve_book(self, book):
        book.reserved = True if book.reserved is False else\
            print(f'{self.visitor_name} не может зарезервировать {book.name}')

    def return_book(self, book):
        if book in self.taken_lst:
            self.taken_lst.remove(book)
        else:
            print(f'{self.visitor_name} не может вернуть {book.name}')
