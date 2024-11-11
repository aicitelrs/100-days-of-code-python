# import colorgram
import turtle as t
from turtle import Screen
import random

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

color_list = [(1, 9, 30), (229, 235, 242), (239, 232, 238), (121, 95, 41), (72, 32, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 170), (151, 92, 115), (35, 90, 26), (6, 154, 73), (205, 63, 91), (168, 129, 78), (3, 78, 28), (1, 64, 147), (221, 179, 218), (4, 220, 218), (80, 135, 179), (130, 157, 177), (81, 110, 135), (120, 187, 164), (11, 213, 220), (118, 18, 36), (243, 205, 7), (132, 223, 209), (229, 173, 165)]

turtle = t.Turtle()
t.colormode(255)

def dot_color():
    color = random.choice(color_list)
    return color

def dots():
    for dot in range(10):
        turtle.dot(20, dot_color())
        turtle.forward(50)
    turtle.setx(-200)
    turtle.setheading(270)
    turtle.forward(50)
    turtle.setheading(0)

turtle.penup()

cont = 0
x = -200
turtle.setx(x)
turtle.sety(200)
while cont < 10:
    dots()
    cont += 1




screen = Screen()
screen.exitonclick()