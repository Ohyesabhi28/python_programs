from book import Book
from member import Student_Member
from library import Library
from borrow_service import BorrowService
from search_service import SearchService

library = Library()

book1 = Book(1, "Python")
book2 = Book(2, "DSA")
library.books.extend([book1, book2])

student = Student_Member(1, "Abhinav", book_limit=1)
library.members.append(student)

BorrowService.borrow_book(student, book1)
BorrowService.return_book(student, book1)

SearchService.search_book(library, "Python")
SearchService.search_book(library, "DSA")
SearchService.search_book(library, "C++")
