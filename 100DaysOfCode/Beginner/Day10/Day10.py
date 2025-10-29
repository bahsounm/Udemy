# Functions with outputs

def format_name(first, last):
    """This takes the first and last name and formats it to
    return the title case version of the name"""
    f = first.title()
    l = last.title()

    return f"{f} {l}"

name = format_name("ANGELA", "SMiTh")

print(name)

# Fucntions with input from other function outputs

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

print(sub(add(5,3), 5))

# Functions with multiple outputs
def format_name2(first, last):
    f = first.title()
    l = last.title()

    return f,l

first, last = format_name2("ANGELA", "SMiTh")

print(f"{first} {last}")


# Docstrings: the way we can give a function a descritpon, without actually having to go to the fucntion and read any comments etc
def format_name(first, last):
    """This takes the first and last name and formats it to
    return the title case version of the name"""
    f = first.title()
    l = last.title()

    return f"{f} {l}"