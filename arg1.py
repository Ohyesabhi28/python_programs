def largest_number(*args):
    if not args:
        return "No numbers provided"

    largest = args[0]

    for num in args:
        if num > largest:
            largest = num

    return largest


# Example usage
print(largest_number(10, 45, 23, 89, 12))