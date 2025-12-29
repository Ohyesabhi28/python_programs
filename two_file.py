file = open("sample.txt", "r")

count = 0
for line in file:
    count += 1

file.close()

print("Number of lines:", count)
