FONT = ("Courier", 24, "normal")
POSITION = (-270, 250)
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.goto(POSITION)
        self.write("Level {}".format(self.score), font=FONT)


    def update_score(self):
        self.write("Level {}".format(self.score), font=FONT)

    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_score()
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 16, "bold"))