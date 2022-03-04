from turtle import Turtle

ALINHAMENTO = "center"
FONT = ("Arial", 14, "normal")

class Placar(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 250)
        self.color('white')
        self.score = 0
        self.write(f'Pontuação: {self.score}', align=ALINHAMENTO, font=FONT)
        self.hideturtle()

    def update(self):
        self.clear()
        self.score += 1
        self.write(f'Pontuação: {self.score}', align=ALINHAMENTO, font=FONT)

class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 0)
        self.color('red')
        self.score = 0
        self.write(f'GAME OVER ', align=ALINHAMENTO, font=("Arial", 50, "normal"))
        self.hideturtle()



