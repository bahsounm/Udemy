# Event listeners using turtle

from turtle import Turtle, Screen

tim = Turtle()

screen = Screen()



# def move_forward():
#     tim.forward(10)

# telling the screen to listen to key presses
# screen.listen()
# specifying what happens when you click a specific key
# screen.onkey(key="space", fun=move_forward)

# mini Proj

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_left():
    tim.left(10)

def move_right():
    tim.right(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="space", fun=clear)
















screen.exitonclick()