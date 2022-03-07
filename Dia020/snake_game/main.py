# out
# from random import randint
from turtle import Screen
from time import sleep
# in
from snake import Snake
from food import Food
from scoreboard import Placar,GameOver
from paredes import criar_paredes
# from enemies import VilaoRed



criar_paredes()
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("gray")
screen.title("O meu game da serpente")
screen.tracer(0)

snake = Snake()

snake.moviments()
food = Food()
placar = Placar()

####
#
# vilao1 = VilaoRed()
# vilao2 = VilaoRed()
# vilao2.color('purple')
# onde1 = {
#     0: vilao1.mover_esquerda,
#     1: vilao1.mover_direita,
#     2: vilao1.mover_cima,
#     3: vilao1.mover_baixo
# }
# onde2 = {
#     0: vilao2.mover_esquerda,
#     1: vilao2.mover_direita,
#     2: vilao2.mover_cima,
#     3: vilao2.mover_baixo
# }
#
#
# def mover_vilao1():
#     para = randint(0, 3)
#     onde1[para]()
#
#
# def mover_vilao2():
#     para = randint(0, 3)
#     onde2[para]()
#
#
# def os_inimigos():
#     mover_vilao1()
#     mover_vilao2()
####

game_is_on = True

print(f' comida{food.xcor(), food.ycor()}')
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()
    # os_inimigos()

    # detectar colisão com a comida
    # if snake.head.xcor() == food.xcor() and snake.head.ycor() == food.ycor():
    if snake.head.distance(food) < 15:
        food.move()
        snake.extend()
        placar.update()

        print("Você pegou a comida!")

    # detectar colisão com a parede
    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        print("Você morreu!")
        GameOver()
        game_is_on = False

    # detectar colisão com a própria cobra
    for segment in snake.all_cobras[1:]:
        if segment.distance(snake.head) < 10:
            print("Você morreu!")
            GameOver()
            game_is_on = False

    # detectar colisão com o vilão









    # if snake.head.distance(vilao1) < 15:
    #     print("Você morreu para o vilhao!")
    #     GameOver()
    #     game_is_on = False

screen.exitonclick()
