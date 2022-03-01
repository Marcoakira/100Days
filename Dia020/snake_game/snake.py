from turtle import Screen, Turtle
from time import sleep

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("gray")
screen.title("O meu game da serpente")
screen.tracer(0)

position_nitial = [(0, 0), (-20, 0), (-40, 0)]

all_cobras = []

# Create snakes
for snake_index in position_nitial:
    new_snake = Turtle(shape="square")
    new_snake.color("white")
    new_snake.penup()
    new_snake.goto(snake_index)
    all_cobras.append(new_snake)
print(all_cobras)

game_is_on = True

# control the snake
def move_right():
    all_cobras[0].right(90)
def move_left():
    all_cobras[0].left(90)
def moviments():
    screen.listen()

    screen.onkey(key="a", fun=move_left)
    screen.onkey(key="d", fun=move_right)

moviments()

while game_is_on:
    screen.update()
    sleep(0.1)
    # Move the snake
    for seg_num in range(len(all_cobras) - 1, 0, -1):
        new_x = all_cobras[seg_num - 1].xcor()
        new_y = all_cobras[seg_num - 1].ycor()
        all_cobras[seg_num].goto(new_x, new_y)

    all_cobras[0].forward(20)


screen.exitonclick()
