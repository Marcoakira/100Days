from turtle import Turtle, Screen
from random import choice

tim = Turtle()
tim.shape("turtle")



def cor():
    random_color = choice(["yellow", " gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy",
                           "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate",
                           "brown", "black","gray"])
    return random_color



def draw_shapes(turtle, size, angle, shape):
    for i in range(shape):
        turtle.forward(size)
        turtle.right(angle)


for a in range(3,22):
    angle = 360 / a
    tim.color(cor())
    draw_shapes(tim, 120, angle, a)

screen = Screen()
screen.exitonclick()
