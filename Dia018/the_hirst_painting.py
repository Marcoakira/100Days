from turtle import Turtle, Screen, colormode
from random import choice

artist = Turtle()
artist.pensize(20)
colormode(255)

artist.penup()
artist.left(180)
artist.forward(250)
# artist.left(180)
artist.left(90)
artist.forward(250)

artist.speed(180)

def color():
    color_tuple = (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (
        170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (
                  14, 98, 70), (
                      232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (
                  19, 86, 89), (
                      82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (
                      168, 99, 102)
    color_list = list(color_tuple)
    return choice(color_list)


def mover():
    for _ in range(10):
        artist.pencolor(color())
        artist.pendown()
        artist.forward(0)
        artist.penup()
        artist.forward(50)

def voltar():

    for _ in range(10): # 10 times
        mover()
        artist.left(90)
        artist.forward(50)
        artist.left(90)
        artist.forward(500)
        artist.right(180)

voltar()

screen = Screen()
screen.exitonclick()
