from Book import Book


def main():
    book1 = Book("Atomic habits", "James Clear", 320)
    book2 = Book("Harry Potter 1", "J.K.Rowling", 240)
    book3 = Book("Sherlock Holmes", "Sir Arthur Conan Doyle", 210)
    book2.borrow()
    print(book1)
    print(book2)
    print(book3)
    print(Book.total_books)
    book2.give_back()
    print(book2)


if __name__ == "__main__":
    main()
