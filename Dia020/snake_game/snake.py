from turtle import Screen, Turtle


screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("gray")
# screen.title("O meu game da serpente")
# screen.tracer(0)

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.all_cobras = []
        self.create_snake()
        self.head = self.all_cobras[0]

    def create_snake(self):
        # Create snakes
        for snake_index in STARTING_POSITIONS:
            new_snake = Turtle("square")
            new_snake.color("white")
            new_snake.penup()
            new_snake.goto(snake_index)
            self.all_cobras.append(new_snake)

    def move(self):

        # Move the snake
        for seg_num in range(len(self.all_cobras) - 1, 0, -1):
            new_x = self.all_cobras[seg_num - 1].xcor()
            new_y = self.all_cobras[seg_num - 1].ycor()
            self.all_cobras[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # control the snake
    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)


    def move_down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def moviments(self):
        screen.listen()

        screen.onkey(key="Up", fun=self.move_up)
        screen.onkey(key="Down", fun=self.move_down)
        screen.onkey(key="Left", fun=self.move_left)
        screen.onkey(key="Right", fun=self.move_right)

    # def xcor(self):
    #     return self.head.xcor()
    # def ycor(self):
    #     return self.head.ycor()

# screen.exitonclick()
