from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

scoreboard = Scoreboard()

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)

screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #Detect collision with paddle.
    if (ball.xcor() > 320 and ball.distance(r_paddle) < 50) or(ball.xcor() < -320 and ball.distance(l_paddle) < 50):
        ball.bounce_x()


    #Detect if r_paddle misses.
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #Detect if l_paddle misses.
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()
