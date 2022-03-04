from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_right():
    tim.right(10)


def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def home():
    tim.home()
    tim.clear()


def moviments():
    screen.listen()
    screen.onkey(key="w", fun=move_forwards)
    screen.onkey(key="s", fun=move_backwards)
    screen.onkey(key="a", fun=turn_left)
    screen.onkey(key="d", fun=move_right)
    screen.onkey(key="h", fun=home)


moviments()
screen.exitonclick()