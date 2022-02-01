#blackjack
from random import choice
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
#print(type(cards[2]))
jogador_pc = []
jogador_humano = []

total_humano = 0
total_pc = 0

def sorteio(quem):
    carta = choice(cards)
    quem.append(carta)

def jogada_inicial():
    sorteio(jogador_pc)
    sorteio(jogador_pc)
    sorteio(jogador_humano)
    sorteio(jogador_humano)

jogada_inicial()

def estorou(jogador,total):
    for pontos in jogador:
        total += pontos
    return total

total_pc = estorou(jogador_pc,total_pc)


print(f"as cartas do computador são: {jogador_pc}")


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

mais_cartas = True
while mais_cartas == True:
    print("a jogador Humano")
    print(jogador_humano)
    cont = input("voce deseja mais cartas? S/N")
    if cont == "n":
        mais_cartas = False
        print("Fim de game os resultados são...")
    else:
        sorteio(jogador_humano)
        total_humano = estorou(jogador_humano, total_humano)
    if total_humano > 21 or total_pc > 21:
        print(" fimde game vc perdeu!")
        break

# def cartas_jogador(quem):
#     quem.append(sorteio())
# jogador_pc.append(sorteio())
# jogador_pc.append(sorteio())




print("Jogador pc ficou com as cartas")
print(jogador_pc)
print("jogador Humano ficou com as cartas")
print(jogador_humano)