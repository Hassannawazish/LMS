class Book:
    def __init__(self, isbn, title, author, year):
        """Initialisation of book attributes"""
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """Method to display a book as a string"""
        return f"{self.title} - {self.author} ({self.year}) - ISBN: {self.isbn}"
