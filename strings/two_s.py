s = input("Enter a string: ")

lowercase = ""
uppercase = ""

for ch in s:
    if ch.islower():
        lowercase += ch
    else:
        uppercase += ch

result = lowercase + uppercase
print("Result:", result)