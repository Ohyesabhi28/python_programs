from excep1 import BookNotFoundError


class SearchService:
    @staticmethod
    def search_book(library, title):
        for book in library.books:
            if title.lower() in book.title.lower():
                return book

        raise BookNotFoundError("Book does not exist")
