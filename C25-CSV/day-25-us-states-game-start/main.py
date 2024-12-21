import turtle, os, pandas

script_dir = os.path.dirname(__file__)
image = os.path.join(script_dir, "blank_states_img.gif")

from sympy import im

screen = turtle.Screen()
screen.title("U.S. States Game")

turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv(os.path.join(script_dir,"50_states.csv"))
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv(os.path.join(script_dir,"states_to_learn.csv"))
        #print(missing_states)
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.item()), int(state_data.y.item()))
        t.write(state_data.state.item())

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
#turtle.mainloop()




#screen.exitonclick()