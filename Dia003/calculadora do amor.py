# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

nomes = name1+name2.lower()
nome_pontos_true  = nomes.count("t") + nomes.count("r") + nomes.count("u") + nomes.count("e")
nome_pontos_love  = nomes.count("l") + nomes.count("o") + nomes.count("v") + nomes.count("e")
valor = int(f"{str(nome_pontos_true) + str(nome_pontos_love)}")

if valor < 10 or valor > 90:
    print(f"Your score is {valor}, you go together like coke and mentos.")

elif valor > 40 and valor < 50:
    print(f"Your score is {valor}, you are alright together.")
else:
    print(f"Your score is {valor}.")    