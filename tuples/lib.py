class Book:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        self.is_available = True

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []        

class Student_Member(Member):
    def __init__(self, member_id, name, book_limit):
        super().__init__(member_id, name)
        self.book_limit = book_limit

class Library:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.books = []
            cls._instance.members = []
        return cls._instance
    

class BorrowService:
    @staticmethod
    def borrow_book(member, book):
        if not book.is_available:
            print("Book not available")
            return

        if isinstance(member, Student_Member):
            if len(member.borrowed_books) >= member.book_limit:
                print("Book limit reached")
                return

        book.is_available = False
        member.borrowed_books.append(book)
        print("Book borrowed")

    @staticmethod
    def return_book(member, book):
        if book in member.borrowed_books:
            book.is_available = True
            member.borrowed_books.remove(book)
            print("Book returned")


class SearchService:
    @staticmethod
    def search_book(library, title):
        found = False

        for book in library.books:
            if title.lower() in book.title.lower():
                print("Found:", book.title)
                found = True

        if not found:
            print("Book not found")

            

library = Library()

book1 = Book(1, "Python")
book2 = Book(2, "DSA")
library.books.extend([book1, book2])

student = Student_Member(1, "Abhinav", book_limit=1)
library.members.append(student)

BorrowService.borrow_book(student, book1)
BorrowService.return_book(student, book1)
SearchService.search_book(library, "Python")
SearchService.search_book(library,"DSA")
SearchService.search_book(library,"C++")
