from art import logo

print(logo)

print("\n\n")


# add
def add(n1, n2):
    return n1 + n2


# subtract
def sub(n1, n2):
    return n1 - n2


# multiply
def mul(n1, n2):
    return n1 * n2


# Divide
def div(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}


def calculadora():
    # """ esse programa é uma calculadora que calcula os calculos calculentos"""

    num1 = float(input("fist number: \n"))
    operation_symbol = input("Qual o simbulo?")
    num2 = float(input("second number: \n"))

    for k in operations:
        print(k)

    caculation_function = operations[operation_symbol]
    first_answer = caculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {first_answer}")

    fim = input("deseja continuar?")
    second_answer = first_answer
    while fim != "n":
        operation_symbol = input("Qual o simbulo? ")
        num3 = float(input("3Qual novo valor? : \n"))
        new_caculation_function = operations[operation_symbol]
        temp_answer = new_caculation_function(first_answer, num3)
        print(f"{second_answer} {operation_symbol} {num3} = {temp_answer}")
        second_answer = temp_answer
        fim = input("deseja continuar?")
    sair = input(" deseja sair? S/N")
    if sair != "n":
        calculadora()


calculadora()

# operation_symbol = input("Qual o simbulo? ")
# num3 = int(input("Qual novo valor? : \n"))
# new_caculation_function = operations[operation_symbol]
# second_answer = new_caculation_function(first_answer,num3)
# print(second_answer)
# print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")

# num1 = int(input("fist number: \n"))
# num2 = int(input("second number: \n"))
#
# for k in operations:
#     print(k)
# tipo = input("qual tipo de operacao:")
# print(tipo)
# print(type(tipo))
# #print(f"{num1}{tipo}{num2}")
#
# function = operations[tipo]
# resposta = function(num1,num2)
# print(resposta)
#
# num1 = int(input("fist number: \n"))
# tipo = input("qual tipo de operacao:")
# num2 = int(input("second number: \n"))
#
# function = operations[tipo]
# function = function()
# print(type(function))
# function(num1,num2)
# print(function)
