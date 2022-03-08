# TODO: import the necessary modules

from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard

# TODO: create the screen

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
scoreboard = Scoreboard()

paddle1 = Paddle(-350,0)
paddle2 = Paddle(350,0)

ball = Ball()

# movimentação do paddle
screen.listen()
# movimentação do paddle 1
screen.onkey(paddle1.paddle_up, 'w')
screen.onkey(paddle1.paddle_down, 's')
# movimentação do paddle 2
screen.onkey(paddle2.paddle_up, 'Up')
screen.onkey(paddle2.paddle_down, 'Down')


# TODO: create and move a paddle


time_sleep = 0.1
game_is_running = True
while game_is_running:
    sleep(time_sleep)
    screen.update()
    ball.move()
    # destecta colisão com a borda
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_v()
    # detecta colisão com os paddles
    if ball.distance(paddle2) < 50 and ball.xcor() > 320 or ball.distance(paddle1) < 50 and ball.xcor() < -320:
        print('made contact')
        ball.bounce_h()

    # detecta ponto direita
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.update_score_r()
        print('ponto direita')
        time_sleep -= 0.001
    # detecta ponto esquerda
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.update_score_l()
        print('ponto esquerda')
        time_sleep -= 0.001






# TODO: Crate anothe paddle

# TODO: create and move a ball



# TODO: Detect collision with wall and bounce

# TODO: Detect collision with paddle

# TODO: Detect when paddle misses

# TODO: Keep score

screen.exitonclick()