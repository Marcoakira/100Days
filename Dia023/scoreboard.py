from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-300, 260)
        self.score = 0
        self.write(f"Score: {self.score}", align='center', font=FONT)



    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align='center', font=FONT)
