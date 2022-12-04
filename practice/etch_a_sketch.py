# W = Forwards
# S = Backwards
# A = Counter-Clockwise: Left
# D = Clockwise: Right
# C = Clear Drawing

from turtle import Turtle, Screen

sketch = Turtle()

sketch.speed("fastest")

def move_forward():
    sketch.forward(10)

def move_backward():
    sketch.back(10)

def move_left():
    sketch.left(10)

def move_right():
    sketch.right(10)

def clear():
    sketch.reset()

screen = Screen()
screen.listen()

screen.onkey(key="w", fun=move_forward)

screen.onkey(key="s", fun=move_backward)

screen.onkey(key="a", fun=move_left)

screen.onkey(key="d", fun=move_right)

screen.onkey(key="c", fun=clear)

screen.exitonclick()