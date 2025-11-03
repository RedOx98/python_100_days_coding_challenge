import turtle
from turtle import Turtle, Screen

import pandas
import pandas as pd

tim = Turtle()
screen = Screen()
screen.title("The US STATES")
# screen.setup(width=900, height=900)
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

# Read state data
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

# Main game loop
while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name? (or type 'Exit' to quit)"
    ).title()

    if answer_state == 'Exit':
        missing_states = [state for state in all_states if state not in guessed_states] #conditional dictionary list
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv", index=False)
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        print(state_data)
        tim.hideturtle()
        tim.penup()
        tim.goto(int(state_data.x.item()), int(state_data.y.item()))
        tim.write(answer_state, align="center", font=("Courier", 8, "normal"))

# Exit on click
screen.exitonclick()