from turtle import Screen
import random as rand
import time
import snake as s

# creating and designing our screen
screen = Screen()
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0) # this is how we turn of the animations, cause when the snake moves it fidgets
#----------------------------------------------------------------------------------------------------------
# Running our Game
game_is_on = True
# create out starting snake
snake = s.Snake()

while game_is_on:
    screen.update() # this is to update the screen to account for the tracer above, 
    time.sleep(0.1) # maybe also change this cause i like the other fluid motion better 

    snake.move()



screen.exitonclick()