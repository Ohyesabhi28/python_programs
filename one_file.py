source = open("source.txt", "r")
destination = open("destination.txt", "w")

content = source.read()
destination.write(content)

source.close()
destination.close()

print("File copied successfully")
