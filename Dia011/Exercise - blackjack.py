# blackjack
from art import logo
from random import choice

print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
"""Lista de cartas dos jogadores pc e humano"""
jogador_pc = []
jogador_humano = []

"""Total de pontos Pc e humano"""
total_humano = 0
total_pc = 0

"""Gera uma carta aleatoria"""


def sorteio(quem):
    carta = choice(cards)
    quem.append(carta)


"""Gera as 2 cartas inicviais de cada jogador e pc"""


def jogada_inicial():
    sorteio(jogador_pc)
    sorteio(jogador_pc)
    sorteio(jogador_humano)
    sorteio(jogador_humano)


jogada_inicial()


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def vitoria():
    if total_humano == 21 or total_pc == 21:
        # verificar em lista quem ganhou.. terminar
        print("HJHHHHHHHHHHHHH")


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

"""Verifica a pontuação total dos jogadores ( pc e humano"""


def estorou(jogador, total):
    total -= total
    for pontos in jogador:
        total += pontos
    return total


"""imprime quais as cartas dos jogadores e o total de pontos"""
total_pc = estorou(jogador_pc, total_pc)
# nao esquecer de alterar para mostra apenasw a primeira carta do pc.
print(f"as cartas do computador são: {jogador_pc} totalizando {total_pc} pontos")

total_humano = estorou(jogador_humano, total_humano)
print(f"as suas cartas são: {jogador_humano} totalizando {total_humano} pontos")

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
"""Colocar aqui a verificação de Blackjack e a tranformação do AS em 11"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def jogada_pc():
    print("completar função")


#
# humano

""" da mais cartas ao jogador"""
mais_cartas = True
while mais_cartas == True:
    print("a jogador Humano")
    print(f" suas cartas atualmente são{jogador_humano}")
    cont = input("voce deseja mais cartas? S/N")

    if cont == "s":
        sorteio(jogador_humano)
        # chama função de verificação se estourou
        total_humano = estorou(jogador_humano, total_humano)
        print(f"Voce recebeu a carta {jogador_humano[-1]}, totalizando {total_humano}")
        if total_humano > 21:
            print(" fim de game vc perdeu!")
            break
    else:
        mais_cartas = False
        print(" vez do Computador...")
        jogada_pc()

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# pc
""" da mais cartas ao pc"""
mais_cartas_pc = True
while mais_cartas_pc == True:
    print("a jogador pc")
    print(jogador_pc)

    if total_pc > 17:
        mais_cartas_pc = False
        print("Fim de game os resultados são...")
    else:
        sorteio(jogador_pc)
        # chama função de verificação se estourou
        total_pc = estorou(jogador_pc, total_pc)
    if total_pc > 21:
        print(" fimde game Computador perdeu!")
        break

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# def cartas_jogador(quem):
#     quem.append(sorteio())
# jogador_pc.append(sorteio())
# jogador_pc.append(sorteio())


""" prints de referencia"""
print(f"Jogador pc ficou com as cartas que a um total de {total_pc}")
print(jogador_pc)
print(f"jogador Humano ficou com as cartas que da um total de {total_humano}")
print(jogador_humano)
