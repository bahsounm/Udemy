from turtle import Turtle

class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.write(f"{self.score}", align="center", font=('Courier', 50, 'bold'))


    def update_score(self):
        self.write(f"{self.score}", align="center", font=('Courier', 50, 'bold'))

    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_score()