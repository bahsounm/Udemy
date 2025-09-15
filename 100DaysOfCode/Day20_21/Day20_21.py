# Snake Game
from turtle import Screen
import random as rand
import time
import snake as s
import food as f
import score as sc
import line as l
#----------------------------------------------------------------------------------------------------------
# creating and designing our screen
screen = Screen()
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0) # this is how we turn of the animations, cause when the snake moves it fidgets
screen.listen() # this is for listening to key press events 
#----------------------------------------------------------------------------------------------------------
# Running our Game
game_is_on = True
#----------------------------------------------------------------------------------------------------------
# create out starting snake, food, score, and line
snake = s.Snake()
food = f.Food()
score = sc.Score()
line = l.Line()
speed = 0.1
#----------------------------------------------------------------------------------------------------------
while game_is_on:
    screen.update() # this is to update the screen to account for the tracer above, 
    time.sleep(speed) # maybe also change this cause i like the other fluid motion better 

    snake.move()

    for key in snake.keys:
        screen.onkey(lambda k=key:snake.turn(k), key)

    # detect snake food collision, lower number means more accurate the snake must be
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()
        speed *= 0.9
    
    # detecting collion with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 258 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # detect collision with tail, slice the first one out to not worry about it
    for part in snake.snake[1:]:
        if snake.head.distance(part) < 10:
            game_is_on = False
            score.game_over()
#----------------------------------------------------------------------------------------------------------
screen.exitonclick()