from turtle import Turtle

class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,300)
        self.setheading(270)

        for i in range(30):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)



