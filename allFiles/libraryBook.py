# Create a library book class that stores inormation about a book, tracks whether it's borrowed or available and allows user to borrow, return or check it's status
class LibraryBook:
    def __init__(self, title, author):
        self.title=title
        self.author=author
        self.available=True
    def borrow(self):
        if self.available:
            self.available= False
            return"Book borrowed successfully"
        else:
            return "Book is already borrowed"
    def return_book(self):
        if not self.available:
            self.available=True
            return "Book returned"
        else:
            return "Book was not borrowed"
    def get_information(self):
        if self.available:
            return f"The book {self.title} by {self.author} is available"
        else:
            return f"The book {self.title} by {self.author} is not available"