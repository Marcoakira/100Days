from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-300, 260)
        self.score = 0




    def update_score(self):

        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align='center', font=FONT)

