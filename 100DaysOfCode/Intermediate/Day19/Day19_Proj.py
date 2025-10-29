# Turtle Race Betting (astag)
from turtle import Turtle, Screen
import random as rand


screen = Screen()
screen.setup(width=500,height=400)

user_bet = screen.textinput("Make your Bet!!!","Which color turtle will win the race?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False
winner = None

def create_turtles(colors):
    turtles = {}
    y = 100
    for color in colors:
        turtles[color] = Turtle(shape="turtle")
        turtles[color].color(color)
        turtles[color].penup()
        turtles[color].goto(-230, y)
        y -= 40
    return turtles

turtles = create_turtles(colors)

if user_bet:
    is_race_on = True

while is_race_on:
    for color in turtles:
        turtle = turtles[color]
        
        if turtle.xcor() > 230:
            is_race_on = False
            winner = (turtle, color)
            break

        rand_dist = rand.randint(0,10)
        turtle.forward(rand_dist)

if winner[1] == user_bet:
    print("Yay Your Turtle Won")
else:
    print("Ooops, Your Turtle Lost")



















screen.exitonclick()