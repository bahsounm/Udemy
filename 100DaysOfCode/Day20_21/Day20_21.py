from turtle import Turtle, Screen
import random as rand
import time

# creating and designing our screen
screen = Screen()
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0) # this is how we turn of the animations, cause when the snake moves it fidgets

# Create our 3 starting turtles

turtles = []

for i in range(3):
    # default turtle size is 20x20
    turtle = Turtle(shape="square")
    turtle.color("white")
    turtle.penup()
    turtle.setx(-20*i)
    turtles.append(turtle)

game_is_on = True

while game_is_on:
    screen.update() # this is to update the screen to account for the tracer above, 
    time.sleep(0.1) # maybe also change this cause i like the other fluid motion better 
    for turtle in turtles:
        turtle.forward(20)























screen.exitonclick()