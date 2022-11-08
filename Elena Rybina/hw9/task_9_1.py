class Book:

    def __init__(self, book_name, author, pages, isbn, reserved):
        self.book_name = book_name
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = reserved

class User:

    def __init__(self, name):
        self.name = name

    def  take_a_book(self,book):



