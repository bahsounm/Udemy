import time

from turtle import Screen
from player import Player
from scoreboard import Scoreboard
#---------------------------------------------------------------------
screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)
#---------------------------------------------------------------------
player = Player()
score = Scoreboard()
#---------------------------------------------------------------------
game_is_on = True

screen.onkeypress(key="Up", fun=player.move)

while game_is_on:
    time.sleep(0.1)
    screen.update()

    if player.ycor() > 280:
        score.increase_score()
        player.reset_position()
#---------------------------------------------------------------------
screen.exitonclick()