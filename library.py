from node import Node
from book import Book

class Library:
    def __init__(self):
        """Initialisation of the tree root"""
        self.root = None

    def add_book(self, book):
        """Method to add a book to the BST"""
        if self.root is None:
            self.root = Node(book)
        else:
            self._add(self.root, book)
    
    def _add(self, node, book):
        if book.title < node.book.title:
            if node.left is None:
                node.left = Node(book)
            else:
                self._add(node.left, book)
        elif book.title > node.book.title:
            if node.right is None:
                node.right = Node(book)
            else:
                self._add(node.right, book)
        else:
            print(f"Book with ISBN {book.isbn} already exists.")
    
    def remove_book(self, isbn):
        """Method to remove a book by ISBN from the BST"""
        self.root = self._remove(self.root, isbn)
    
    def _remove(self, node, isbn):
        if node is None:
            return node
        if isbn < node.book.isbn:
            node.left = self._remove(node.left, isbn)
        elif isbn > node.book.isbn:
            node.right = self._remove(node.right, isbn)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.book = temp.book
            node.right = self._remove(node.right, temp.book.isbn)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def search_book(self, criteria, value):
        """Method to search for a book by title, author, or ISBN"""
        if criteria == 'isbn':
            return self._search_isbn(self.root, value)
        elif criteria == 'title':
            return self._search_title(self.root, value)
        elif criteria == 'author':
            return self._search_author(self.root, value)
        else:
            return None

    def _search_isbn(self, node, isbn):
        if node is None or node.book.isbn == isbn:
            return node
        elif isbn < node.book.isbn:
            return self._search_isbn(node.left, isbn)
        else:
            return self._search_isbn(node.right, isbn)
    
    def _search_title(self, node, title):
        if node is None or node.book.title == title:
            return node
        elif title < node.book.title:
            return self._search_title(node.left, title)
        else:
            return self._search_title(node.right, title)
    
    def _search_author(self, node, author):
        if node is None:
            return None
        if author == node.book.author:
            return node
        left_search = self._search_author(node.left, author)
        return left_search if left_search else self._search_author(node.right, author)

    def display_books(self, sort_by='title'):
        """Method to display all books, sorted by title or year"""
        if sort_by == 'title':
            self._in_order_traversal(self.root)
        else:
            self._in_order_traversal_by_year(self.root)
    
    def _in_order_traversal(self, node):
        if node:
            self._in_order_traversal(node.left)
            print(node.book)
            self._in_order_traversal(node.right)
    
    def _in_order_traversal_by_year(self, node):
        if node:
            self._in_order_traversal_by_year(node.left)
            print(node.book)
            self._in_order_traversal_by_year(node.right)
    
    def save(self, file_name):
        """Method to save the books to a text file"""
        books = []
        self._collect_books(self.root, books)
        with open(file_name, 'w') as file:
            for book in books:
                file.write(f"{book.isbn},{book.title},{book.author},{book.year}\n")
    
    def _collect_books(self, node, books):
        if node:
            self._collect_books(node.left, books)
            books.append(node.book)
            self._collect_books(node.right, books)

    def load(self, file_name):
        """Method to load the books from a text file"""
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    isbn, title, author, year = line.strip().split(',')
                    book = Book(isbn, title, author, int(year))
                    self.add_book(book)
        except FileNotFoundError:
            print(f"File {file_name} not found.")
