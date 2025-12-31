class StudentIterator:
    def __init__(self, students):
        self.students = students
        self.index = 0
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.students):
            name = self.students[self.index]
            self.index += 1

            if name.startswith("S"):
                self.count += 1

            return name
        else:
            raise StopIteration
students = ["Alice", "Bob", "Sam", "Sophie", "John", "Sara"]
student_iterator = StudentIterator(students)