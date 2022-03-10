import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard



screen = Screen()
screen.tracer(0)
screen.bgcolor('gray')
screen.setup(width=800, height=600)

scoreboard = Scoreboard()
player = Player()

#move player
screen.listen()
screen.onkeypress(player.move, 'w')


game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()





screen.exitonclick()