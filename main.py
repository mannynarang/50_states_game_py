import turtle
from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
turtle = Turtle()

screen.title("U.S. States Game")
screen.bgpic("blank_states_img.gif")
turtle.penup()
turtle.hideturtle()

df = pd.read_csv("50_states.csv")
correct_guesses=[]
guess = 1
game_on = True
while guess < 50 and game_on:
    answer = screen.textinput(title=f" Correct guesses : {len(correct_guesses)}/50", prompt="Guess a state name? ").lower()
    result = df[df.state.str.lower() == answer]
    if answer == "exit":
        game_on = False
        break

    if not result.empty and not result.state.item() in correct_guesses :
        turtle.setpos(int(result.x), int(result.y))
        turtle.write(result.state.item())
        correct_guesses.append(result.state.item())
        guess += 1

missed_states = df[~df.state.isin(correct_guesses)]


with open("missed_states.csv","w") as FILE:
    for missed_state in missed_states.state.values.tolist():
        FILE.write(f"{str(missed_state)}\n")



def get_mouse_click_cord(x, y):
    print(x, y)


screen.onscreenclick(get_mouse_click_cord)

screen.mainloop()
