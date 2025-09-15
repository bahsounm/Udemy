from turtle import Turtle, Screen
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        # create our snakes
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        self.keys = ["Up", "Down", "Left", "Right"]

    def create_snake(self):
        for i in range(3):
            # default turtle size is 20x20
            turtle = Turtle(shape="square")
            if i == 0:
                turtle.color("orange")
            else:
                turtle.color("green")
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
        headings = [90, 270, 180, 0]
        # this allows us to control movement, the snake is not allowed to move back on itself
        if (self.head.heading() == 90 and key != "Down") or (self.head.heading() == 270 and key != "Up") or (self.head.heading() == 0 and key != "Left") or (self.head.heading() == 180 and key != "Right"):
            self.head.setheading(headings[self.keys.index(key)])

    def extend(self):
        turtle = Turtle(shape="square")
        turtle.color("green")
        turtle.penup()
        turtle.goto(self.snake[-1].position())
        self.snake.append(turtle)