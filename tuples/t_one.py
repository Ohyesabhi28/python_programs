def remove_empty_strings(strings):
    result = []
    for item in strings:
        if item != "":
            result.append(item)
    return result


strings = ["apple", "", "banana", "", "cherry", "", ""]
print("Original list:", strings)

clean_list = remove_empty_strings(strings)
print("List after removing empty strings:", clean_list)