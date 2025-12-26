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
