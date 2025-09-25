FONT = ("Courier", 24, "bold")
POSITION = (-260, 210)
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 10
        self.penup()
        self.hideturtle()
        self.goto(POSITION)
        self.write("Tries Left {}".format(self.score), font=FONT)


    def update_score(self):
        self.write("Tries Left {}".format(self.score), font=FONT)

    def decrease_score(self):
        self.score -=1
        self.clear()
        self.update_score()
    
    def get_score(self):
        return self.score
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 16, "bold"))

    def winner(self):
        self.goto(0,0)
        self.write("You Won", align="center", font=("Arial", 16, "bold"))