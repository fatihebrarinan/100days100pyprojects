from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
gamble = screen.textinput("Welcome to the turtle race!", "Who will win?: ")
end_of_game = False
winner = ""
screen.title("Turtle Racing Game")
colors = ["blue", "red", "yellow", "purple", "green", "orange"]
y_pos = [100, 60, 20, -20, -60, -100]
all_turtles = []


def random_speed():
    random_num = random.randint(1, 5)
    return random_num * 5


for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_pos[i])
    all_turtles.append(new_turtle)

while not end_of_game:
    for turtles in all_turtles:
        turtles.forward(random_speed())
        if turtles.xcor() >= 230:
            winner = turtles.pencolor()
            end_of_game = True
            break

print(f"Winner is {winner}!")
if gamble == winner:
    print("You guessed it right!")
else:
    print("You guessed it wrong!")

screen.exitonclick()
