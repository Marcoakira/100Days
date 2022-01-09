print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

altura_permitida = 120
if height >= altura_permitida:
  idade = int(input("Qual sua idade?"))
  if idade < 12:
    entrada = 5
    print("o valor da entrada  criança é 5 reais.")
  elif idade <=18:
    entrada = 7
    print("O valor da entrada adolescente é 7 reais.")
  else:
    entrada = 12
    print("O valor da entrada adulto é 12 reais.")

  fotos = input("voce deseja tirar uma foto por 3 reais? S/N").strip().upper()
  if fotos == "S":
    entrada += 3
    print(f" valor total da entra com foto é de {entrada}")

  print("bom passeio")

else:
  print("sinto muito, mas vc não tem altura suficiente")