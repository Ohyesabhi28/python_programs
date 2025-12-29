def format_name(name):
    if not isinstance(name, str):
        raise TypeError("Input must be a string")

    return name.capitalize()


try:
    print(format_name("abhishek"))   
    print(format_name(123))          
except TypeError as e:
    print(e)
