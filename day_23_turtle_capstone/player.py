from turtle import Turtle
from scoreboard import Scoreboard
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(0, -280)

    def up(self):
        self.forward(10)

    def level_up(self, scoreboard, carManager):
        self.goto(0,-280)
        scoreboard.level_up()
        carManager.moveDistance += carManager.moveIncrement

