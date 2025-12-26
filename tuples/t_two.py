def count_odd_even(numbers):
    odd = []
    even = []

    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    return odd, even

numbers = [10, 15, 20, 25, 30, 33, 42]

odd_numbers, even_numbers = count_odd_even(numbers)

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)