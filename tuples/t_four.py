numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
even_numbers = ()
for num in numbers:
    if num % 2 == 0:
        even_numbers = even_numbers + (num,)
print("Original tuple:", numbers)
print("Even numbers tuple:", even_numbers)