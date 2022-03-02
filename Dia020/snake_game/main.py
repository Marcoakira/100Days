from turtle import Screen, distance
from snake import Snake
from time import sleep
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("gray")
screen.title("O meu game da serpente")
screen.tracer(0)

snake = Snake()

snake.moviments()
food = Food()

game_is_on = True

print(f' comida{food.xcor(), food.ycor()}')
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()


    #detectar colisão com a comida
    # if snake.head.xcor() == food.xcor() and snake.head.ycor() == food.ycor():
    if snake.head.distance(food) < 15:
        food.move()
        print("Você pegou a comida!")



screen.exitonclick()
