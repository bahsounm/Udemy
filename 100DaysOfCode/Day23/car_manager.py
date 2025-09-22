COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10

from turtle import Turtle
import random as rand

class CarManager:
    def __init__(self):
        self.cars = []
        self.multiplier = 1
        self.car_speed = 1
        self.generate_cars()


    def generate_cars(self):
        x = 40
        for i in range(100):
            car = Turtle()
            car.penup()
            car.color(rand.choice(COLORS))
            car.shape("square")
            car.setheading(180)
            car.shapesize(stretch_len=2,stretch_wid=1)
            car.goto(350 + x, rand.randint(-250,270))
            car.speed(10)
            self.cars.append(car)
            x+= 40


    def start_cars(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE*self.multiplier)

    def next_level(self):
        self.car_speed += 1
        self.multiplier *= 1.09
        for car in self.cars:
            car.speed(self.car_speed)
