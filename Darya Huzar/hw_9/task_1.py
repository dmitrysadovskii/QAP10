class Book:
    def __init__(self, name, author, page_count, ISBN):
        self.name = name
        self.author = author
        self.page_count = page_count
        self.ISBN = ISBN
        self.reserved = False
        self.borrowed_by = None

    def reserve(self):
        self.reserved = True

    def borrow(self, user):
        if self.reserved:
            print(f"Book {self.name} is already reserved.")
            return
        if self.borrowed_by is not None:
            print(f"Book {self.name} is already borrowed by {self.borrowed_by.name}.")
            return
        self.borrowed_by = user
        print(f"{user.name} has borrowed {self.name}.")

    def return_book(self, user):
        if self.borrowed_by is None:
            print(f"Book {self.name} is not borrowed.")
            return
        if self.borrowed_by != user:
            print(f"{user.name} cannot return {self.name} as it was borrowed by {self.borrowed_by.name}.")
            return
        self.borrowed_by = None
        print(f"{user.name} has returned {self.name}.")


class User:
    def __init__(self, name):
        self.name = name

    def borrow_book(self, book):
        book.borrow(self)

    def return_book(self, book):
        book.return_book(self)


book = Book("War and Peace", "Leo Tolstoy", 1225, "1234567890")

user1 = User("John")
user2 = User("Jane")

user1.borrow_book(book)
user2.borrow_book(book)
user1.return_book(book)
user2.borrow_book(book)
book.reserve()
user1.borrow_book(book)
