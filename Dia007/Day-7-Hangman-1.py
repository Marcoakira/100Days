import random

word_list = ["aardvark", "baboon", "camel"]

palavra_escolhida = random.choice(word_list)
palavra_jogador = "_"*len(palavra_escolhida)

print("#"*78)
print("SEJA BEM VINDOS AO SUPER MEGA HIPER JOGO DA FORCA, TENTE NAO MORRER HAHAHAHHA")
print("#"*78)
print(palavra_escolhida)
while palavra_jogador != palavra_escolhida:
    letra = input("escolha uma letra: \n")
    for l in range(0,len(palavra_escolhida)):
        if palavra_escolhida[l] == letra:
            palavra_jogador[l] = letra
            print(palavra_jogador)


print(palavra_escolhida)
print(palavra_jogador)