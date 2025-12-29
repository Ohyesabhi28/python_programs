def count_odd_even(*args):
    odd_count = 0
    even_count = 0

    for num in args:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return odd_count, even_count

odd, even = count_odd_even(1, 2, 3, 4, 5, 6, 7)
print("Odd count:", odd)
print("Even count:", even)