from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.goto(0,250)
        self.color("white")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", True, align="center",font=('Arial', 20, 'normal'))

    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_score()
