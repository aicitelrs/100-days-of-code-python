# building an etch a sketch project

from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

def move_forwards():
    turtle.forward(10)

def move_backwards():
    turtle.backward(10)

def move_counter_clockwise():
    new_heading = turtle.heading() + 10
    turtle.setheading(new_heading)

def move_clockwise():
    new_heading = turtle.heading() - 10
    turtle.setheading(new_heading)

def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

screen.listen()
screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=move_counter_clockwise, key="a")
screen.onkey(fun=move_clockwise, key="d")
clear()


screen.exitonclick()