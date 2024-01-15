import turtle
import  pandas

screen = turtle.Screen()
screen.title("INDIA states Game")
image = "india-state.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("states_data.csv")
all_states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 29:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/29 states Correct",  prompt="What's another state's name?").title()
    # print(answer_state)
    if answer_state == "Exit":
        a = turtle.Turtle()
        a.hideturtle()
        a.penup()
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        # print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        print(new_data)
        # new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)



screen.exitonclick()


# To get a coordinate
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()