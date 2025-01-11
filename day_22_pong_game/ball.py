from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.home()
        self.bounce_x()
        self.move_speed = 0.1

    # def move(self):
    #     if self.heading() == 45 and (self.ycor() > 280):
    #         self.setheading(315)
    #     if self.heading() == 315 and (self.ycor() < -280):
    #         self.setheading(45)
    #     if self.heading() == 135 and (self.ycor() > 280):
    #         self.setheading(225)
    #     if self.heading() == 225 and (self.ycor() < -280):
    #         self.setheading(135)
    #     self.forward(10)
    # my solution.

