import turtle
import time
from states_manager import StatesManager

screen = turtle.Screen()
screen.title("U.S. State Guessing Game")

#Implies background image
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

statesManager = StatesManager()

guessed_states = []

while len(guessed_states) < 50:
    guess = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Guess a state: ").title()

    if guess == "Exit":
        break
    if guess in set(statesManager.state_names_list):
        guessed_states.append(guess)
        statesManager.create_state_name(guess)

statesManager.generate_states_to_learn(guessed_states)

