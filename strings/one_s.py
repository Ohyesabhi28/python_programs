s = input("Enter a string: ")

length = len(s)
middle_index = length // 2

new_string = s[0] + s[middle_index] + s[-1]

print("New string:", new_string)