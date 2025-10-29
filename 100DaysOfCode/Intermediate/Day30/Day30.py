# FileNotFound
# with open("data.txt") as file:
#     file.read()

# KeyError
# using a key for a dictionary and that key in no in there

# Index Error
# indexing somthuing that doesnt exist, ex. the list is lenght 5 and we try to list[10]

# we can catch these exceptions 

# try:
#     try what we want to do
# except:
#      if something else went wrong do this insterad
# else:
#      if all looks good in our try then run this code
# finally:
#      do this no matter what happens whether things passed or not 

# Catching Exceptions
try:
    file = open("data,txt")
    x = {"a": 1}
    print(x["a"])
except FileNotFoundError: # try to be specific with the error you are trying to find, dont just generalize the except catch
    file = open("data,txt", "w")
    file.write("Hello World")
except KeyError as errorMessage:
    print("we can also do this. we can catch multiple exceptions and handle each one differently")
    # errorMessage will hold the key that contains the issue
else:
    content = file.read()
    print(content)
finally:
    file.close()


# Raising Exceptions

height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")
bmi = weight / height**2