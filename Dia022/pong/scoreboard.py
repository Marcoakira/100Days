from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('gray')
        self.penup()
        self.hideturtle()
        self.goto(0,250)
        self.l_score = 0
        self.r_score = 0
        self.update_score()
        #self.write(f'{self.l_score} - {self.r_score}', align='center', font=('Courier', 24, 'normal'))

    def update_score(self):
        self.clear()
        self.write(f'{self.l_score} - {self.r_score}', align='center', font=('Courier', 24, 'normal'))

    def update_score_r(self):
        self.r_score += 1
        self.update_score()

    def update_score_l(self):
        self.l_score += 1
        self.update_score()