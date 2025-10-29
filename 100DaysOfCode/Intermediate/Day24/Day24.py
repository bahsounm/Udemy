# opening, and reading the file

file = open("../../../../../Desktop/Praise be to God.txt")
contents = file.read()
print(contents)
file.close() # need to closer at some point to enhance performance

# can do it this way that way you dont have to close it later
with open("myfile.txt") as f:
    contents = f.read()
    print(contents)


# writng to the file 
# mode is default as read
# w will overwrite everything and write what you have
# a will append to whats already there
# if we try to open a file that does not exist, a new file will be created

with open("myfile.txt", mode="a") as f:
    pass

# understanding relative and absolute file paths
"""
Absolute: start from the root, and make their way to the desired file = ""/Users/Bahsoun/Desktop/Praise be to God.txt""

Relative: starts from the working directory = "../../../../../Desktop/Praise be to God.txt"
"""