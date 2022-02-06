#importaçoes
from art import logo,vs
from game_data import data
from random import randint


#
"""testes"""
#
# opcao = data[2]['name']
# print(opcao)

"""________________"""

#1 copia a base de dados para uma nova lista temporaria
base_atual_game = data.copy()

#randomico = int
#2

#primeiro_item = base_atual_game[randomico]
#base_atual_game.pop(randomico)

def a_opcao():
    def item_randomico():
        randomico_local = randint(0, len(base_atual_game))

        return randomico_local
    randomico = item_randomico()
    primeiro_item = base_atual_game[randomico]
    base_atual_game.pop(randomico)


    return primeiro_item
a_opcao()


#3 escolher primeiro dado de maneira randomica apaga ele da lista





#==========================



#primeiro_item = {}
'''
primeiro_item = base_atual_game[randomico]
base_atual_game.pop(randomico)
'''

#se fosse uma lista
#rapaz = primeiro_item.insert(0,base_atual_game.pop(base_atual_game[randomico]))
'''
segundo_item = []

print(primeiro_item)
print(primeiro_item["name"])
print(base_atual_game)
'''
#4 escolher segundo dado. de maneira randomica e apaga ele da lista

#print(primeiro)

#6 perguntar e armazenar opção do jogador

#7 verificar resposta. # se errado retornar com pontuação e feedback ao jogador

#8 acertadando tranforma segundo dado em primeiro dado,
#
#9retorna ao 4

