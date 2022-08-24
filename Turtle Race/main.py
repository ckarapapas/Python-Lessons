import random
import turtle
from turtle import Turtle, Screen
screen = Screen()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


def set_up(t, y):
    ind = random.randint(0, len(colors)-1)
    t.shape("turtle")
    t.up()
    t.color(colors.pop(ind))
    t.goto(x=-220, y=y)


winner = turtle.textinput("Bet!", "Choose the color of the winner:").lower()
all_turtles = []
for i in range(0,6):
    tim = Turtle()
    set_up(tim, -180+i*50)
    all_turtles.append(tim)

race_is_on = True
while race_is_on:
    for t in all_turtles:
        t.forward(random.randint(0,10))
        if t.position()[0] >= 330:
            race_is_on = False
            win_turtle = t.color()[0]

if win_turtle == winner:
    print("You win the bet!")
else:
    print(f"You lose, {win_turtle} wins!")
screen.exitonclick()