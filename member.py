class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []


class Student_Member(Member):
    def __init__(self, member_id, name, book_limit):
        super().__init__(member_id, name)
        self.book_limit = book_limit
