file = open("sample.txt", "r")
word = input("Enter word to search: ")

found = False

for line in file:
    if word in line:
        found = True
        break

file.close()

if found:
    print("Word found")
else:
    print("Word not found")
