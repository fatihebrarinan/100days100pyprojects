from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-340, 300)
        self.level = 1
    def level_up(self):
        self.level += 1

    def write_level(self):
        self.clear()
        self.write(arg="Level: " + str(self.level), move=False, align="center", font=('Arial', 15, 'normal'))
    def write_gameover(self):
        self.home()
        self.write(arg="GAME OVER", move=False, align="center", font=('Arial', 30, 'bold'))
