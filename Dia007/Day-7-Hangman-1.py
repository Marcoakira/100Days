import random

word_list = ["aardvark", "baboon", "camel"]

palavra_escolhida_pc = random.choice(word_list)
palavra_escolhida = list(palavra_escolhida_pc)
palavra_jogador_pc = "_" * len(palavra_escolhida)
palavra_jogador = list(palavra_jogador_pc)
print(palavra_escolhida)
print("#" * 78)
print("SEJA BEM VINDOS AO SUPER MEGA HIPER JOGO DA FORCA, TENTE NAO MORRER HAHAHAHHA")
print("#" * 78)
# torcar por um len de letras faladas.
letras_faladas = []
while palavra_escolhida != palavra_jogador:
    letra = input(" Escolha uma letra")

    vezes_que_aparecem = 0
    for l in range(0, len(palavra_escolhida)):

        if palavra_escolhida[l] == letra:
            palavra_jogador[l] = letra
            vezes_que_aparecem += 1

    if vezes_que_aparecem == 0:
        letras_faladas.append(letra)

    print(f"apareceram {vezes_que_aparecem}Vezes a letra {letra}")

    print(palavra_jogador)
    print(f"voce ja disse errado as letras:{letras_faladas}")
    print(f"você ainda tem {5 - len(letras_faladas)} chances")
    if len(letras_faladas) >= 5:
        print(f"sinto muito voce perdeu, a palavra era {palavra_escolhida_pc}")
        break
if palavra_escolhida == palavra_jogador:
    print(f"parabens voce ganhou acertou a palavra: {palavra_escolhida_pc}")
