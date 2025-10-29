import time

from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager
import random as rand
#---------------------------------------------------------------------
screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)
car_man = CarManager()
#---------------------------------------------------------------------
player = Player()
score = Scoreboard()
#---------------------------------------------------------------------
game_is_on = True

screen.onkeypress(key="Up", fun=player.move)
offset = 40
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_man.start_cars()

    # check if the player has crossed the finish line
    if player.ycor() > 280:
        # update the score, and take the turtle back to the starting position for the next level
        score.increase_score()
        player.reset_position()
        car_man.next_level()
    
    for car in car_man.cars:
        if player.distance(car) < 20:
            score.game_over()
            game_is_on = False
        if car.xcor() < -330:
            car.setx(350 + offset)
            offset += 40
#---------------------------------------------------------------------
screen.exitonclick()