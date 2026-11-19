class Book:
    total_books = 0

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_borrowed = False
        Book.total_books += 1

    def borrow(self):
        self.is_borrowed = True

    def give_back(self):
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} | {self.author} | {self.pages} pages | {'Borrowed' if self.is_borrowed else 'Available'}"
