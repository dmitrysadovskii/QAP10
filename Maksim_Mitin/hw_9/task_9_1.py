class Book:
    def __init__(self, name, author, pages, isbn, reserved):
        self.name = name
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = reserved


class User:
    def __init__(self, first_name, last_name):
        self.firstname = first_name
        self.lastname = last_name

    @staticmethod
    def take_book(book):
        if book.reserved:
            print(f'You cant take {book.name} book , another user reserved or take this book already')
        else:
            book.reserved = True
            print(f'You take {book.name} book , please do not forget to return book')

    @staticmethod
    def return_book(book):
        if book.reserved:
            print(f'{book.name} book already returned, maybe its not our book, please check ')
        else:
            book.reserved = False
            print(f'You return {book.name} book , thank you for choosing our library !')

    @staticmethod
    def reserver_book(book):
        if book.reserved:
            print(f'You cant take {book.name} book , another user reserved or take this book already')
        else:
            book.reserved = True
            print(f'You reserve {book.name} book,please take reserved book in 7 days or reserve will be canceled')


book_1 = Book('Pupa i Lupa', 'Uncle Bogdan', 123, 9786123453211, False)
book_2 = Book('Deep Dark Male Fantasies', 'Van Darkholm', 69, 9786123453322, True)
book_3 = Book('God Hates Us All', 'Jesus', 666, 9786123453666, False)
book_4 = Book('Existence Is Futile', 'Jesus', 999, 9786123453999, False)


print(book_1.reserved)

user_1 = User('Pig', 'Benis')
user_2 = User('nataS', 'tearG')

user_1.take_book(book_1)
user_1.take_book(book_2)
user_2.take_book(book_1)

print(book_1.reserved)
