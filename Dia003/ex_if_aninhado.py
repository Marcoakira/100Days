print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

altura_permitida = 120
if height >= altura_permitida:
  idade = int(input("Qual sua idade?"))
  if idade < 12:
    print("o valor da entrada é 5 reais.")
  elif idade <=18:
    print("O valor da entrada é 7 reais.")
  else:
    print("O valor da entrada é 12 reais.")
  print("bom passeio")
else:
  print("sinto muito, mas vc não tem altura suficiente")