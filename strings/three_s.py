s = input("Enter a string: ")

char_count = {}

for ch in s:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1

print("Character occurrences:")
for key, value in char_count.items():
    print(key, ":", value)