import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
segments = []
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="w", fun=snake.up)
screen.onkey(key="s", fun=snake.down)
screen.onkey(key="a", fun=snake.left)
screen.onkey(key="d", fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() < -280 or snake.segments[0].ycor() > 280:
        scoreboard.reset_scoreboard()
        snake.reset_snake()

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            scoreboard.reset_scoreboard()
            snake.reset_snake()

screen.exitonclick()
