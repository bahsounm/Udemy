# Million Dollar Painting

import colorgram
from turtle import Screen, Turtle
import random as rand

# Extracting our color palette
colors = colorgram.extract('hunter.jpg', 30)
rgb = []
for color in colors:
    rgb.append((color.rgb.r,color.rgb.g,color.rgb.b))


# Creating timmy
timmy = Turtle()
timmy.width(10)
timmy.speed(0)
timmy.up()
timmy.hideturtle()
screen = Screen()
screen.colormode(255)

# logic for painting

for i in range(1,11):
    timmy.setpos(-300,-300 + 50*i)
    for j in range(10):
        timmy.pencolor(rand.choice(rgb))
        timmy.down()
        timmy.dot(20)
        timmy.up()
        timmy.forward(50)



















screen.exitonclick()