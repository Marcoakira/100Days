# importaçoes
from art import logo, vs
from game_data import data
from random import randint

# 1 copia a base de dados para uma nova lista temporaria
base_atual_game = data.copy()


# função que seleciona um dicionario aleatorio da lista, retorna ele, e apaga ele da lista
def a_opcao():
    def item_randomico():
        randomico_local = randint(0, len(base_atual_game))

        return randomico_local

    randomico = item_randomico()
    item = base_atual_game[randomico]
    base_atual_game.pop(randomico)

    return item


# apresentação


print(logo)
print("\nSEJA BEM VINDO AO MEGA JOGO HIGHER LOWER\n Escolha qual tem mais seguidores\n\n")


# 3 escolher primeiro dado de maneira randomica apaga ele da lista
def quem_ganhou():
    if primeiro_item_top['follower_count'] > segundo_item['follower_count']:
        certo = 'a'
    else:
        certo = 'b'
    return certo


acertou = True
pontos = 0
primeiro_item_top = a_opcao()
while len(base_atual_game) > 0 and acertou == True:
    segundo_item = a_opcao()
    print(
        f"Compare A: {primeiro_item_top['name']}, a {primeiro_item_top['description']}, from {primeiro_item_top['country']}")
    print(vs)
    print(f"Against B: {segundo_item['name']}, a {segundo_item['description']}, from {segundo_item['country']}\n")

    escolha = input("Who has more followers? Type 'A' or 'B': ").lower()
    ganho = quem_ganhou()
    if escolha == ganho and len(base_atual_game) == 0:
        print(f"UAUUUUUUUUUU !!!!!!!!! Voce Acertou era a opção {ganho}, Você ZEROUUUU O GAMEEE, INCRIVELLL")
    elif escolha == ganho:
        pontos += 1
        print(f"Parabens voce acertou a resposta certa é a {escolha.upper()} "
              f"\nesta com {pontos} pontos, faltam {len(base_atual_game)} para voce zerar o game.")
        primeiro_item_top = segundo_item
    else:
        print(f"Nao foi dessa vez :( , a resposta certa era {ganho}, Voce fez {pontos} pontos.\n Volte sempre.")
        acertou = False

# ==========================


# primeiro_item = {}
'''
primeiro_item = base_atual_game[randomico]
base_atual_game.pop(randomico)
'''

# se fosse uma lista
# rapaz = primeiro_item.insert(0,base_atual_game.pop(base_atual_game[randomico]))

# 4 escolher segundo dado. de maneira randomica e apaga ele da lista

# print(primeiro)

# 6 perguntar e armazenar opção do jogador

# 7 verificar resposta. # se errado retornar com pontuação e feedback ao jogador

# 8 acertadando tranforma segundo dado em primeiro dado,
#
# 9retorna ao 4
