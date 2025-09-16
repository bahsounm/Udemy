from turtle import Turtle
import random as rand

SPEED = 15
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.reset = False
        self.y_movement = SPEED
        self.x_movement = SPEED

    def start(self):
        self.goto(self.xcor()+self.x_movement, self.ycor() +self.y_movement)

    def refresh(self):
        self.goto(0, 0)
    
    def bounce_y(self):
        self.y_movement *=-1
    
    def bounce_x(self):
        self.x_movement *=-1