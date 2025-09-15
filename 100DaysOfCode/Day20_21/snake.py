from turtle import Turtle
class Snake:

    def __init__(self):
        # create our snakes
        self.snake = self.create_snake()

    def create_snake(self):
        snake = []
        for i in range(3):
            # default turtle size is 20x20
            turtle = Turtle(shape="square")
            turtle.color("white")
            turtle.penup()
            turtle.setx(-20*i)
            snake.append(turtle)
        return snake
    
    def move(self):
        # in order to make the snake move nicely and TURN nicely, we set each part of the snake to assume the position of its following piece
        for idx in range(len(self.snake)-1,0,-1):
            new_x, new_y = self.snake[idx-1].xcor(), self.snake[idx-1].ycor()
            self.snake[idx].goto(new_x,new_y)
        # move the head of the snake and the rest with follow
        self.snake[0].forward(20)