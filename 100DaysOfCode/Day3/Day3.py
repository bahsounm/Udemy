# Control with if / else
print("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm?"))

if height > 120:
    print("You can ride the rollercoaster")
    # adding nesting frm below here
    age = int(input("What is your age?"))
    if age >=18:
        print("Your ticket price is 12")
    elif age >= 12 and age < 18:
        print("Your ticket price is 7")
    else:
        print("Your ticket price is 5")

else:
    print("Sorry youll have to come back when youre a bit taller")
    
# comparison operaters include >, <, >=, <=, !=, ==,
# conditionals need to be based on True or False
#-------------------------------------------------------------------------------
# The Modulo operator
# this operator returns the remainder 

num = int(input("Pick a number and Ill tell you if its odd or even"))
if num%2 == 0:
    print(f"your number {num} is even")
else:
    print(f"your number {num} is odd")
#-------------------------------------------------------------------------------
# nested conditionals using if, elif and else
# see roller coster up top
#-------------------------------------------------------------------------------
# mini proj
print("Welcome to Python Pizza Deliveries")
size = input("What size of pizza do you want? S, M L: ")
pepperoni = input("Do you want pepperoni on the pizza? Y or N: ")
extra_cheese = input("Do you want extra Cheese on your pizza? Y or N: ")

total = 0

if size == "S":
    total += 15
elif size == "M":
    total+= 20
elif size == "L":
    total += 25

if pepperoni == "Y":
    if size == "S":
        total+=2
    else:
        total +=3
if extra_cheese == "Y":
    total += 1

print(f"Your total bill is: {total}")
#-------------------------------------------------------------------------------
# Logical Operators = and, or, not









