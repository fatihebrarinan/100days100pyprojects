from turtle import Turtle
import pandas
import pandas as pd


class StatesManager:
    def __init__(self):
        self.states_data = pandas.read_csv("50_states.csv")
        self.state_names_list = self.states_data.state.to_list()

    def create_state_name(self, state_name):
        state = Turtle()
        state.hideturtle()
        state.penup()
        # get x and y
        state_row = self.states_data[self.states_data.state == f"{state_name}"]
        state_x = state_row.x.item()
        state_y = state_row.y.item()
        state.goto(state_x,state_y)
        state.write(f"{state_name}", align="center", font=("Courier", 11, "normal"))

    def generate_states_to_learn(self, states):
        self.states_to_learn = [state for state in self.state_names_list if state not in states]
        pd.Series(self.states_to_learn).to_csv("states_to_learn.csv")


