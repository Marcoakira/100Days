from turtle import Turtle
from scoreboard import Scoreboard
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

scoreboard = Scoreboard()
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('blue')
        self.shape('turtle')
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        print('move')
        self.forward(MOVE_DISTANCE)
        if self.ycor() > FINISH_LINE_Y:
            scoreboard.update_score()
            self.goto(STARTING_POSITION)


