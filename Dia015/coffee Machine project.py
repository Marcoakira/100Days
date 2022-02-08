
#Dicionario de itens com seus requisitos
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

#tabela de capacidades da maquina.
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# teste print(MENU['espresso']['ingredients']['water'])
#depois colocar a opçao apenas se tiver recursos
client_option = input(f'What would you like?  '
                      f'(\033[1;31mE\033[mspresso/\033[1;31mL\033[matte/\033[1;31mC\033[mappuccino): ').lower()

""" função que cobra"""

preco = MENU[client_option]["cost"]
print(preco)
print(type(preco))
total_pago = float(0)
def cobrando(valor, l_total_pago):


    while valor > l_total_pago:

        print("insira as moedas ( coins)")
        quarters = 0.25 * int(input("Quantas moedas de quarters $0.25: "))
        dimes =  0.10 * int(input("Quantas moedas de dimes $0.10: "))
        nickles = 0.05 * int(input("Quantas moedas de nickles $0.05: "))
        pennies = 0.01 * int(input("Quantas moedas de pennies 0.01: "))

        def soma():
            total = quarters + dimes + nickles + pennies
            return total
        print(total_pago)

        l_total_pago = total_pago + soma()

        print(l_total_pago)
        if valor == l_total_pago:
            print(f" Estamos preparando seu {client_option} ")
        else:
            print(f'o {client_option} custa {MENU[client_option]["cost"]}, você inseriu {l_total_pago}, ainda faltam'
                  f' {MENU[client_option]["cost"] - l_total_pago:.2f}')
        return l_total_pago

total_pago = cobrando(valor=preco, l_total_pago=total_pago)



"""

# 3 sabores de café quente{
Espresso: 50ml water, 18g coffee [prince 1.50]
latte: 200ml water, 24g coffee, 150ml milk [prince 2.50]
Cappuccino: 250ml water, 24 coffee, 100ml milk [prince 3.00]
}

# capacidade da maquina
# trabalha com moedas

# digitando report envia um relatorio de quanto tem na maquita de recursos

1. print report
2 check resources sufficient ?
3 process coins
4 check transaction successful?
5 make coffee

"""
# aTODO: 1. print report of all coffee machine resources

