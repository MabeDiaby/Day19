# Event Listeners

from turtle import Turtle, Screen

tim = Turtle()

def move_forward():
    tim.forward(10)

screen = Screen()
screen.listen()

screen.onkey(key="space", fun=move_forward)
screen.exitonclick()