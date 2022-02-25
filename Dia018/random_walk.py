import random
from turtle import Turtle as t, Screen, colormode
from random import choice, randint

quadro = t()

colormode(255)
def size():
    size = randint(10, 40)
    return size


quadro.speed(180)

def cor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    quadro.color(r, g, b)
    return r, g, b


# def cor():
#     random_color = choice(["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat",
#                            "SlateGray", "orange", "red", "maroon", "violet", "magenta", "purple", "navy",
#                            "blue", "skyblue", "cyan", "lightgreen", "green", "darkgreen", "chocolate",
#                            "brown", "black", "gray"])
#     return random_color

def directions():
    direction = choice([0, 90, 180, 270])
    return direction

for i in range(3000):
    quadro.pensize(size())
    quadro.color(cor())
    print(i)
    print(cor())
    quadro.forward(20)
    quadro.left(directions())

screen = Screen()
screen.exitonclick()
