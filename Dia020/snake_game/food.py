from turtle import Turtle
from random import randint


#
# def position_generator():
#     """
#     Generates random coordinates for the food.
#     """
#     return randint(-300, 300), randint(-300, 300)


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.shapesize(0.5)  # size of food, tamanho padrão é 20 x 20, assim como o snake, ela fica então mais pequena
        self.speed('fastest')
        self.position_generatorx = randint(-380, 380)  # width of the screen
        self.position_generatory = randint(-280, 280)  # height of the screen
        self.goto(self.position_generatorx, self.position_generatory)

        # fazer com que a comida apareça em uma posição aleatória

    def move(self):
        self.goto(randint(-380, 380), randint(-280, 280))  # move the food to a random position
