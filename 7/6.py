class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, author, title):
        new_book = Book(author, title)
        self.books.append(new_book)
    
    def view_books(self):
        for book in self.books:
            print(book.author + ": " + book.title)
    
    def sort_by_author(self):
        self.books.sort(key=lambda x: x.author)
        self.view_books()
    
    def sort_by_title(self):
        self.books.sort(key=lambda x: x.title)
        self.view_books()

library = Library()
library.add_book("Author 1", "Title 1")
library.add_book("Author 2", "Title 2")
library.add_book("Author 3", "Title 3")
library.view_books()
print("Sorted by author:")
library.sort_by_author()
print("Sorted by title:")
library.sort_by_title()
