def find_grade(**kwargs):
    if not kwargs:
        return "No subjects provided"

    total = 0
    count = 0

    for subject, marks in kwargs.items():
        total += marks
        count += 1

    average = total / count

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"

    return grade

grade = find_grade(
    maths=85,
    physics=78,
    chemistry=82,
    english=90
)

print("Grade:", grade)
