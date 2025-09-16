from turtle import Turtle

SPEED = 20

class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.setheading(90)
        self.shapesize(stretch_len=5,stretch_wid=1)
        self.goto(position)
        self.speed(0)

    def move_up(self):
        self.forward(SPEED)

    def move_down(self):
        self.forward(-SPEED)

    def prevent_move(self):
        if self.ycor() > 0:
            self.sety(230)
        else:
            self.sety(-219)

