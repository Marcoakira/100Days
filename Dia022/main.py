# TODO: import the necessary modules

from turtle import Turtle, Screen


# TODO: create the screen


screen = Screen()

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

screen.bgcolor("lightgreen")
screen.title("Dia 22")
screen.setup(width=800, height=600)

class Jogadores(Turtle):
    def __init__(self, x, y):
        Turtle.__init__(self)
        self.penup()
        self.goto(x, y)
        self.penup()
        self.shape("square")
        self.color("black")
        self.shapesize(1,5)

    def move_up(self):
        if self.ycor() < 300:
            self.seth(90)
            self.forward(20)
    def move_down(self):
        if self.ycor() > -300:
            self.seth(270)
            self.forward(20)


    def movimentos1(self):

        screen.listen()

        screen.onkey(key="w", fun=self.move_up)
        screen.onkey(key="s", fun=self.move_down)
    def movimentos2(self):

        screen.listen()

        screen.onkey(key="Up", fun=self.move_up)
        screen.onkey(key="Down", fun=self.move_down)




# TODO: create and move a paddle

jogador1 = Jogadores(-350, 0)
jogador2 = Jogadores(350, 0)

jogador1.movimentos1()
jogador2.movimentos2()

# TODO: Crate anothe paddle

# TODO: create and move a ball

class Bola(Turtle):
    def __init__(self, x, y):
        Turtle.__init__(self)
        self.penup()
        self.goto(x, y)
        self.penup()
        self.shape("circle")
        self.color("red")
        self.shapesize(1,1)
        self.speed(1)

        self.seth(90)
    def bola_rolando(self,):

        self.forward(10)
        # if self.xcor() > 350:
        #     direcao = direcao + 90
        # if self.xcor() < -350:
        #     self.direcao = direcao + 90
        if self.ycor() > 200:
            self.seth(270)
        # if self.ycor() < -300:
        #     direcao = 90



bola = Bola(0, 0)
while True:
    bola.bola_rolando()
    screen.exitonclick()




# TODO: Detect collision with wall and bounce

# TODO: Detect collision with paddle

# TODO: Detect when paddle misses

#TODO: Keep score

