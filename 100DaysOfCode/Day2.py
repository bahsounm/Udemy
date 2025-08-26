# Python Primitive Data Types
# String = anything between " "
s = "Hello World"
# Integer = Whole number
i = 5
# Float = real numbers
f = 3.14159
# Boolean = True or False
b = True
#-------------------------------------------------------------------------------
# Subscrtpting: printing the element/char of a list/string
# note indexing starts from 0
print(s[0])
print(s[-1])
#-------------------------------------------------------------------------------
# Type Checking + Type Conversion AKA Type Casting
# Note: Not everything can be converted (like string with letter to int)
print(str(type(s)) + "\n" + str(type(i)) + "\n" + str(type(f)) + "\n" + str(type(b)))
#-------------------------------------------------------------------------------
# MAthematical Operations
print(1+2)
print(1-2)
print(1*2)
print(1/2)
print(1//2) # can be dangerous since youre missing the rest of the cdeciamls this took out the .5
print(2**4)
print(8%2)
#-------------------------------------------------------------------------------
# Number Manipulation and F Strings
print(round(3.1))
print(round(3.5))
print(round(ndigits=2, number = 5.3456)) # can spcify how many to reound too

print(f"your score is {f}")
