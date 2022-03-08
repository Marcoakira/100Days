from turtle import Turtle
from time import sleep


class Ball(Turtle):
    def __init__(self, ):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_v(self):
        self.y_move *= -1

    def bounce_h(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        sleep(2)
        self.bounce_v()
        
