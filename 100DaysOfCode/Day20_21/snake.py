from turtle import Turtle, Screen
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        # create our snakes
        self.snake = []
        self.create_snake()
        self.keys = ["Up", "Down", "Left", "Right"]

    def create_snake(self):
        for i in range(3):
            # default turtle size is 20x20
            turtle = Turtle(shape="square")
            turtle.color("white")
            turtle.penup()
            turtle.setx(-20*i)
            self.snake.append(turtle)
    
    def move(self):
        # in order to make the snake move nicely and TURN nicely, we set each part of the snake to assume the position of its following piece
        for idx in range(len(self.snake)-1,0,-1):
            new_x, new_y = self.snake[idx-1].xcor(), self.snake[idx-1].ycor()
            self.snake[idx].goto(new_x,new_y)
        # move the head of the snake and the rest with follow
        self.snake[0].forward(MOVE_DISTANCE)

    def turn(self, key):
        # heading allows us to change which way the snake is going to move
        heading = [90, 270, 180, 0]
        self.snake[0].setheading(heading[self.keys.index(key)])