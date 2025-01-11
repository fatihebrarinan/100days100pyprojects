from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.highscore = file.read()
        self.penup()
        self.goto(0, 265)
        self.color("white")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score = {self.score} Highscore = {self.highscore}", align="center", font=("Courier", 20, "bold"))

    def reset_scoreboard(self):
        if self.score > int(self.highscore):
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.highscore))
            self.score = 0
            self.update_score()
    #def game_over(self):
     #   self.goto(0, 0)
      #  self.write(arg="GAME OVER", align="center", font=("Courier", 30, "bold"))

    def increase_score(self):
        self.score += 1
        self.update_score()
