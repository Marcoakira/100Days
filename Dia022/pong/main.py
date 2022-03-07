# TODO: import the necessary modules

from turtle import Screen
from paddle import Paddle

# TODO: create the screen

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')

paddle1 = Paddle(-350,0)
paddle2 = Paddle(350,0)

# movimentação do paddle
screen.listen()
# movimentação do paddle 1
screen.onkey(paddle1.paddle_up, 'w')
screen.onkey(paddle1.paddle_down, 's')
# movimentação do paddle 2
screen.onkey(paddle2.paddle_up, 'Up')
screen.onkey(paddle2.paddle_down, 'Down')


# TODO: create and move a paddle

game_is_running = True
while game_is_running:
    screen.update()


# TODO: Crate anothe paddle

# TODO: create and move a ball



# TODO: Detect collision with wall and bounce

# TODO: Detect collision with paddle

# TODO: Detect when paddle misses

# TODO: Keep score

screen.exitonclick()