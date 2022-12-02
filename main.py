import turtle
import pandas


screen = turtle.Screen()
screen.setup(722, 488)
screen.title("US States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

t = turtle.Turtle()
t.hideturtle()
t.penup()

states_data = pandas.read_csv("50_states.csv")
states = states_data.state.to_list()

guessed_states = []
while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missed_states = [state for state in states if state not in guessed_states]
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in states:
        guessed_states.append(answer_state)
        state = states_data[states_data.state == answer_state]
        x_coord = int(state.x)
        y_coord = int(state.y)
        t.goto(x_coord, y_coord)
        t.write(state.state.item())
