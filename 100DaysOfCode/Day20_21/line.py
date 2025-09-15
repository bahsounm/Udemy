from turtle import Turtle

class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.goto(-300,250)
        self.color("white")
        self.hideturtle()
        self.write("-------------------------------------------------------------------------------------------------------------------------------------------------------")

