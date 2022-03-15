from turtle import Turtle, Screen
import pandas as pd

''' Screen '''

screen = Screen()
# screen.setup(width=800, height=600)
screen.title('US States Game - by Marco Aurélio Menezes (100 Dias)')
imagem = 'blank_states_img.gif'
screen.addshape(imagem)
turtle = Turtle()
turtle.shape(imagem)

''' Pandas '''
data = pd.read_csv('50_states.csv')
all_states = data.state.to_list()


''' Funções '''

answer_state = screen.textinput(title='Acerte o nome dos Estados',prompt= 'Qual estado você sabe o nome?')
print(answer_state)

if answer_state in all_states:
    print('Você acertou!')
    t = Turtle()
    t.hideturtle()
    t.penup()
    answer = data[data.state == answer_state]
    t.goto(int(answer.x), int(answer.y))
    t.write(answer.state.item(), font=('Arial', 30, 'normal'))
# else:
#     print('Você errou!')

# if anser_state is one state of the 50 states


















screen.exitonclick()
