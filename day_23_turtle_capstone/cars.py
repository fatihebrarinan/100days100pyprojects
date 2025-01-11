import random
from turtle import Turtle

COLORS = ["red", "yellow", "blue", "green", "orange", "black"]




class CarManager:

    def __init__(self):
        self.all_cars = []
        self.moveDistance = 10
        self.moveIncrement = 2


    def create_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.setheading(180)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        random_y = random.randint(-250, 250)
        new_car.goto(400, random_y)
        self.all_cars.append(new_car)
    def move_all_cars(self):
        for car in self.all_cars:
            car.forward(self.moveDistance)















