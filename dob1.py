from datetime import datetime

dob_input = input("Enter date of birth (YYYY-MM-DD): ")

dob = datetime.strptime(dob_input, "%Y-%m-%d").date()
today = datetime.today().date()

age = today.year - dob.year

if (today.month, today.day) < (dob.month, dob.day):
    age -= 1

print("Age:", age)
