# Pong Game
from turtle import Screen, Turtle
import random as rand
import time
from board import Board
from score import Score
from player import Player
from ball import Ball
#----------------------------------------------------------------------------------------------------------
# creating and designing our screen
screen = Screen()
screen.title("Snake Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0) # this is how we turn of the animations, cause when the snake moves it fidgets
screen.listen() # this is for listening to key press events 
#----------------------------------------------------------------------------------------------------------

# Creating our Board (includes the line in the middle and the score for each player)
board = Board()
score1 = Score((-70,220))
score2 = Score((70, 220))
ball = Ball()
#----------------------------------------------------------------------------------------------------------
# creating our 2 players
player1 = Player((-370,0))
player2 = Player((360,0))
#----------------------------------------------------------------------------------------------------------
# Creating our game logic
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    ball.start()

    # Player 1 movement keys (REMEMBER THE FUNCTION CANNOT HAVE "()")
    screen.onkeypress(key = "w", fun = player1.move_up)
    screen.onkeypress(key = "s", fun = player1.move_down)

    # Player 2 movement keys (REMEMBER THE FUNCTION CANNOT HAVE "()")
    screen.onkeypress(key = "Up", fun = player2.move_up)
    screen.onkeypress(key = "Down", fun = player2.move_down)


    # Detect collision of the paddle with the roof and floor
    if player1.ycor() > 230 or player1.ycor() < -219:
        player1.prevent_move()
    if player2.ycor() > 230 or player2.ycor() < -219:
        player2.prevent_move()

    # Detect Ball collision with the y axis, change the direction
    if ball.ycor() > 280 or ball.ycor() < -265:
        ball.bounce_y()

    # Detect the ball collision with x axis, if hits paddle change direction, if hits wall update score and start ball again
    if ball.distance(player2) < 50 and ball.xcor() > 340 or ball.distance(player1) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    if ball.xcor() >380:
        score1.increase_score()
        ball.bounce_x()
        ball.refresh()
    elif ball.xcor() < -380:
        score2.increase_score()
        ball.bounce_x()
        ball.refresh()
#----------------------------------------------------------------------------------------------------------
screen.exitonclick()