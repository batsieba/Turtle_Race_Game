import turtle
from turtle import Turtle, Screen
import random


def draw_turtle(x, y, t_color):
    tim = Turtle("turtle")
    tim.color(t_color)
    tim.penup()
    tim.goto(x,y)
    tim.pendown()
    return tim


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="which turtle is going to win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y = [-70, -40, -10, 20, 50, 80]
all_turtles = []
for i in range(0, 6):
    new_turtle = draw_turtle(-230, y[i], colors[i])
    new_turtle.penup()
    all_turtles.append(new_turtle)
    # ----------another way to do it-----------
    # new_turtle = Turtle("turtle")
    # new_turtle.penup()
    # new_turtle.color(colors[i])
    # new_turtle.goto(-230, y[i])
    # all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner")
            else:
                print(f"You have lost! The {winning_color} was the winner")
        pace = random.randint(0,10)
        turtle.forward(pace)


screen.exitonclick()
