from turtle import Screen, Turtle
from time import sleep

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("gray")
screen.title("O meu game da serpente")
screen.tracer(0)

# le_goto_x = 0
position_nitial = [(0, 0), (-20, 0), (-40, 0)]
all_cobras = []

# Create 3 turtles
for snake_index in position_nitial:
    new_snake = Turtle(shape="square")
    new_snake.color("white")
    new_snake.penup()
    new_snake.goto(snake_index)
    all_cobras.append(new_snake)
print(all_cobras)

game_is_on = True

while game_is_on:
    screen.update()
    sleep(0.1)

    for seg_num in range(len(all_cobras), 0, -1):
        new_x = all_cobras[seg_num -1].xcor()
        new_y = all_cobras[seg_num - 1].ycor()
        all_cobras[seg_num].goto(new_x,new_y)
# for cobra in all_cobras:
#     cobra.forward(20)

# if cobra.xcor() > screen.window_width() / 2:
#     game_is_on = False
#     print("Game Over")

# Criando o objeto da cobra

#
# class Cobra(Turtle):
#     def __init__(self,position):
#         super().__init__()
#         self.shape("square")
#         self.color("white")
#         self.turtlesize(1)
#         self.penup()
#         self.speed(0)
#         self.position = 0
#         self.goto(position, 0)
#         self.direction = "stop"
#
#
#     def pos(self):
#         self.goto(0, 0)
#         self.position += 20
# ²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²
# def go_up(self):
#     self.direction = "up"
#
# def go_down(self):
#     self.direction = "down"
#
# def go_left(self):
#     self.direction = "left"
#
# def go_right(self):
#     self.direction = "right"
#

# cobra001 = Cobra(0)
# cobra002 = Cobra(-20)


screen.exitonclick()
