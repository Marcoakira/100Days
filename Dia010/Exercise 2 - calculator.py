from art import logo

print(logo)

print("\n\n")

#add
def add(n1,n2):
    return n1+n2

#subtract
def sub(n1,n2):
    return n1 - n2

#multiply
def mul(n1,n2):
    return n1*n2

#Divide
def div(n1,n2):
    return n1 /n2

operations = {
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}

num1 = int(input("fist number: \n"))
num2 = int(input("second number: \n"))
for k in operations:
    print(k)
operation_symbol = input("Qual o simbulo?")
caculation_function = operations[operation_symbol]
answer = caculation_function(num1,num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")



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