import colorgram
import turtle as t
import random
t.colormode(255)
tostos = t.Turtle()
my_screen = t.Screen()
tostos.speed("fastest")
tostos.hideturtle()
colors = colorgram.extract('image.jpg', 11)


def new_color():
    random_number = random.randint(0,10)
    random_color = colors[random_number]
    return tostos.color(random_color.rgb)


for place in range(0, 601, 60):
    tostos.penup()
    tostos.goto(-300, -300+place)
    tostos.dot(25)
    for i in range(10):
        new_color()
        tostos.forward(60)
        tostos.dot(25)

my_screen.exitonclick()
