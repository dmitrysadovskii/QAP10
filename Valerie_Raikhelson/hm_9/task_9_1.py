class Book:
    books = list()

    def __init__(self,
                 name: str,
                 author: str,
                 amount_of_pages: int,
                 __isbn: str,
                 is_reserved: bool):
        self.name = name
        self.author = author
        self.amount_of_pages = amount_of_pages
        self.isbn = __isbn
        self.is_reserved = is_reserved

    def add_book(self, book):
        self.books.append(book)


book_1 = Book("A Novel", "Hoover", 100, "978-1-56619-909-1", is_reserved=False)
book_2 = Book("The Night Ship", "Kidd", 100, "978-1-56619-909-2", is_reserved=False)
book_3 = Book("O Caledonia", "Barker", 100, "978-1-56619-909-3", is_reserved=False)

book_1.add_book(book_1)
book_2.add_book(book_2)
book_3.add_book(book_3)


class User:
    books_in_library = Book.books

    def __init__(self, l_name: str):
        self.l_name = l_name
        self.checked_out_books = list()

    def get_book(self, name):
        for check_book in self.checked_out_books:
            if check_book.name == name:
                raise Exception(f"The book {name} has already been taken from the library")

        for book in self.books_in_library:
            if name == book.name and book.is_reserved is True:
                raise Exception(f"This book: {name} is reserved or borrowed")

            if name == book.name and book.is_reserved is False:
                book.is_reserved = True
                self.checked_out_books.append(book)
                break
        print(len(self.checked_out_books))
        print(book.name, book.is_reserved)

    def return_book(self, isbn, name):
        for book in self.books_in_library:
            if isbn == book.isbn and name == book.name:
                book.is_reserved = False
                self.checked_out_books.remove(book)
                break
            else:
                raise Exception(f"Check request data: {isbn}, {name}")
        print(len(self.checked_out_books))
        print(book.name, book.is_reserved)

    def reserve_book(self, name, author, amount_of_pages, isbn, is_reserved=True):
        for book in self.books_in_library:
            if isbn == book.isbn:
                raise Exception("The book already exist in library")

        order = Book(name, author, amount_of_pages, isbn, is_reserved)
        self.books_in_library.append(order)
        self.checked_out_books.append(order)

        print(len(self.checked_out_books))
        print(len(self.books_in_library))


user = User("Oleg")
user.get_book("A Novel")
user.get_book("O Caledonia")

user_1 = User("Oleg")
# user_1.get_book("A Novel")
# user_1.get_book("O Caledonia")

user.return_book("978-1-56619-909-1", "A Novel")
user.reserve_book("Anna K", "James", 100, "978-1-56619-909-5", True)
user_1.reserve_book("Anna K", "James", 100, "978-1-56619-909-5", True)
