# working wit hturtle graphics
# turtle graphics documentation:     https://docs.python.org/3/library/turtle.html


from turtle import Turtle, Screen
import random as rand 

timmy = Turtle()
screen = Screen()
timmy.shape("turtle")

# Draw a square
# for i in range(4):
#     timmy.forward(100)
#     timmy.left(90)

# Draw a dashed line, use up to bring the pen up off the page, and down to put the pen down on the page
# timmy.shape("arrow")
# for i in range(10):
#     timmy.down()
#     timmy.forward(10)
#     timmy.up()
#     timmy.forward(10)


# Drawing each shape from triangle to decagon (10)
# timmy.width(10)
# colors = ["blue", "red","green", "pink", "teal", "orange", "purple", "yellow", "medium purple", "lime", "midnight blue"]
# for i in range(3,11):
#     # need to minues from 180 to account for rotation is the opposite direction
#     angle = 180 - ((i-2)*180)/i
#     print(angle)
#     for j in range(i):
#         timmy.color(rand.choice(colors))
#         timmy.forward(100)
#         timmy.left(angle)

# Generating a random walk
# direction = [0, 90, 180, 270]
# for i in range(50):
#     timmy.forward(30)
#     timmy.left(rand.choice(direction))
#     timmy.color(rand.choice(colors))

# Generating a random walk with random colors
# direction = [0, 90, 180, 270]
# screen.colormode(255)
# for i in range(50):
#     timmy.forward(30)
#     timmy.left(rand.choice(direction))
#     timmy.pencolor((rand.randint(0,255), rand.randint(0,255), rand.randint(0,255)))

# Drawing a spirograph
# screen.colormode(255)
# timmy.speed(0)
# for i in range(72):
#     timmy.circle(200)
#     timmy.left(5)
#     timmy.pencolor((rand.randint(0,255), rand.randint(0,255), rand.randint(0,255)))

screen.exitonclick()
