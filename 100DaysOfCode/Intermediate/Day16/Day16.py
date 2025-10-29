# OOP, using a class Turtle to test things out

import turtle

timmy = turtle.Turtle()
timmy.shape('turtle')
timmy.color('coral')

turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)

my_screen = turtle.Screen()
my_screen.exitonclick()

#--------------------------
# Python packages 

# # pip install prettytable to install the package

import prettytable

table = prettytable.PrettyTable()
table.add_column("Pokemon", ["Pikachu","Charmander", "Squirtle"])
table.add_column("Type", ["Electric", "Fire", "Water"])

table.align = "l"


print(table)

