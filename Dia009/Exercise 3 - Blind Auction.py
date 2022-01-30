#from replit import clear
from art import logo
print(logo)

#HINT: You can call clear() to clear the output in the console.



lances = []
proximo = "s"


while proximo == "s":
    nome = str(input("Qual o seu nome? \n"))
    aposta = int(input("Qual o valor da sua aposta? \n"))
    proximo = str(input("Mais alguem vai apostar? S ou N")).lower()
    lance = {"nome": nome, "aposta": aposta}
    lances.append(lance)
    #clear()

#lances = [{'nome': 'batata', 'aposta': 152}, {'nome': 'joaquim', 'aposta': 23}, {'nome': 'rafaelo', 'aposta': 26}, {'nome': 'ranito', 'aposta': 30}]
maior_aposta = {'nome': 'null', 'aposta': 0}

for pos, cont in enumerate(lances):
    # print(pos)
    # print(cont)
    if lances[pos]["aposta"] > maior_aposta["aposta"]:
        maior_aposta = lances[pos]

print(f"a maior aposta foi de  {maior_aposta['nome']} no valor de {maior_aposta['aposta'] }\n")


print(lances)
