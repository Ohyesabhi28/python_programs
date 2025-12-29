class NegativeAgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise NegativeAgeError("Age cannot be negative")

    birth_year = 2025 - age  
    print("Year of Birth:", birth_year)

except NegativeAgeError as e:
    print("Error:", e)

except ValueError:
    print("Error: Please enter a valid number")
