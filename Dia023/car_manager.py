from turtle import Turtle
from random import randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
a_cor = COLORS[randint(0, len(COLORS) - 1)]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
posicao = []

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1,2)
        self.color(a_cor)
        self.speed(0)
        self.penup()
        self.goto(-300, randint(-280, 280))
        self.move()

    def move(self):
        while True:
            self.forward(STARTING_MOVE_DISTANCE)
            self.left(randint(0, 360))
            if self.xcor() > 300:
                self.goto(-300, randint(-280, 280))
        # self.forward(STARTING_MOVE_DISTANCE)
        # self.forward(MOVE_INCREMENT)
        # if self.xcor() > 300:
        #     self.goto(-300, 0)

    def criarposicao(self):
        for b in range(0,200, 10):
            posicao.append(b)
        print(posicao)

    def criar_carros(self):
        for i in range(0,5):
            CarManager()
            CarManager().criarposicao()
            CarManager().move()

