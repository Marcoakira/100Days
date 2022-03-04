from turtle import Turtle


class Parede(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.speed(0)
        self.color('black')

    def medidas(self,shap1,shap2,gotox,gotoy):
        self.shapesize(shap1, shap2)
        self.goto(gotox, gotoy)
def criar_paredes():
    parede_esquerda = Parede()
    parede_esquerda.medidas(28,0.5,-390,0)
    parede_direita = Parede()
    parede_direita.medidas(28, 0.5, 390, 0)
    # self.parede_cima = self.medidas(28, 0.5, -390, 0)
    # self.parede_baixo = self.medidas(28, 0.5, -390, 0)



