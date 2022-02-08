# Number Objetivos do jogo de adivinhação:

# Inclua um logotipo de arte ASCII.
from art import logo
import random

print(logo)

# Gerar o numero aleatorio
NU_MAGICO = int(random.randint(0, 100))
print(NU_MAGICO)
tentativas = 0
# Permitir que o jogador envie um palpite para um número entre 1 e 100.
print("@" * 50)
print("TENTE ADVINHAR O NUMERO QUE ESTOU PENSANDO")
print("@" * 50)
level = input("Qual o nivel de Dificuldade 'facil' ou 'Dificil' ? \n").lower()
if "dificil" in level:
    tentativas += 10
else:
    tentativas += 5

palpite = 0

# Verifica o palpite do usuário em relação à resposta real. Imprima "Muito alto". ou "Muito baixo". dependendo da
# resposta do usuário.


while tentativas > 0:
    palpite = int(input(f"Você tem {tentativas} chances.\n"))
    if palpite == NU_MAGICO:
        break
    elif palpite > NU_MAGICO:
        print("Muito alto")
    else:
        print("Muito baixo")
    tentativas -= 1

if tentativas == 0:
    print(f"Infelismente acabaram as tentativas, você perdeu! o numero era {NU_MAGICO}")
else:
    print(f"parabens voce acertou o numero{NU_MAGICO}")

# Se eles acertaram a resposta, mostre a resposta real ao jogador.
# Acompanhe o número de voltas restantes.
# Se eles ficarem sem turnos, forneça feedback ao jogador.
# Inclua dois níveis de dificuldade diferentes (por exemplo, 10 palpites no modo fácil, apenas 5 palpites no
# modo difícil).
