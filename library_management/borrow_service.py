from member import Student_Member
from excep1 import BorrowLimitExceededError


class BorrowService:
    @staticmethod
    def borrow_book(member, book):
        if not book.is_available:
            print("Book not available")
            return

        if isinstance(member, Student_Member):
            if len(member.borrowed_books) >= member.book_limit:
                raise BorrowLimitExceededError("Student borrowing limit exceeded")

        book.is_available = False
        member.borrowed_books.append(book)
        print("Book borrowed")

    @staticmethod
    def return_book(member, book):
        if book in member.borrowed_books:
            book.is_available = True
            member.borrowed_books.remove(book)
            print("Book returned")
