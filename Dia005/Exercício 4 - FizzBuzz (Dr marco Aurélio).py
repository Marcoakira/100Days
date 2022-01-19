# Instruções
# Você vai escrever um programa que imprime automaticamente a solução do jogo FizzBuzz.
#
# Seu programa deve imprimir cada número de 1 a 100 por vez.
#
# Quando o número é divisível por 3, em vez de imprimir o número, deve imprimir "Fizz".
#
# Quando o número é divisível por 5, em vez de imprimir o número, deve imprimir "Buzz".`
#
#   E se o número for divisível por 3 e 5, por exemplo, 15, em vez do número, deve imprimir "FizzBuzz"

fizz = "Fizz"
buzz = "Buzz"

for numero in range(1,101):
    if numero % 3 ==0 and numero % 5 == 0:
        print(f'{fizz}{buzz}')
    elif numero % 3 == 0:
        print(fizz)
    elif numero % 5 == 0:
        print(buzz)
    else: print(numero)


