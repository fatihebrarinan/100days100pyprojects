import time
import random
from turtle import Screen
from cars import CarManager
from player import Player
from scoreboard import Scoreboard

game_is_on = True

screen = Screen()
screen.screensize(canvwidth=600, canvheight=600)
screen.tracer(0)

player = Player()
carManager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(key="Up", fun=player.up)


i = 0
while game_is_on:
    i += 1
    if i % 4 == 0:
        carManager.create_car()
    carManager.move_all_cars()
    scoreboard.write_level()

    for cars in carManager.all_cars:
        if cars.distance(player) < 20:
            scoreboard.write_gameover()
            game_is_on = False


    if player.ycor() >= 320:
        player.level_up(scoreboard, carManager)

    time.sleep(0.1)
    screen.update()

screen.exitonclick()








