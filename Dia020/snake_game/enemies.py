from turtle import Turtle, Screen
from random import randint

screen = Screen()



class VilaoRed(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('triangle')
        self.penup()
        self.color('red')

        # self.goto(0, 0)


    def mover_esquerda(self):
        if self.xcor() > -400:
            self.setheading(180)
            self.forward(60)
        else:
            self.setheading(0)
            self.forward(40)


    def mover_direita(self):
        if self.xcor() < 400:
            self.setheading(0)
            self.forward(60)
        else:
            self.setheading(180)
            self.forward(40)


    def mover_cima(self):
       if self.ycor() < 300:
            self.setheading(90)
            self.forward(60)
       else:
            self.setheading(270)
            self.forward(20)



    def mover_baixo(self):
        if self.ycor() > -300:
            self.setheading(270)
            self.forward(60)
        else:
            self.setheading(90)
            self.forward(40)




#
# vilao1 = VilaoRed()
# vilao2 = VilaoRed()
# vilao2.color('purple')
# onde1 = {
#             0:vilao1.mover_esquerda,
#         1:vilao1.mover_direita,
#         2:vilao1.mover_cima,
#         3:vilao1.mover_baixo
#         }
# onde2 = {
#             0:vilao2.mover_esquerda,
#         1:vilao2.mover_direita,
#         2:vilao2.mover_cima,
#         3:vilao2.mover_baixo
#         }
#
#
# def mover_vilao1():
#         para = randint(0, 3)
#         onde1[para]()
#
# def mover_vilao2():
#         para = randint(0, 3)
#         onde2[para]()
# def os_inimigos():
#     while True:
#         mover_vilao1()
#         mover_vilao2()
#
#
# os_inimigos()