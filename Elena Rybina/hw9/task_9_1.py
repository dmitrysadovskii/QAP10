class Book:

    def __init__(self, book_name, author, pages, isbn, reserved):
        self.book_name = book_name
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = reserved

class User:
    def __init__(self, name):
        self.books = []
        self.name = name

    def take_book(self, book):
        if book.reserved:
            print(f'The book "{book.book_name}" is reserved.')
        else:
            self.books.append(book)
            book.reserved = 1
            print(f'The book "{book.book_name}" was successfully picked up by {self.name}.')

    def remove_book(self, book):
        if book.reserved:
            book.reserved = 0
            print(f'The book "{book.book_name}" is avaliable.')
        else:
            print(f'The book "{book.book_name}" is already available')


Book_1 = Book('Norwegian Wood', 'Haruki Murakami', 125, '5976579', 0)
Book_2 = Book('The Sherlock Holmes stories', 'Arthur Conan Doyle', 352, '6876579', 0)


user_1 = User('Elena')
user_2 = User('Pete')
user_1.take_book(Book_1)
user_2.remove_book(Book_1)
user_2.take_book(Book_2)
user_1.take_book(Book_1)
user_2.remove_book(Book_2)
user_2.take_book(Book_1)
