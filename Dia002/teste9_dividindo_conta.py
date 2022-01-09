

conta = float(input("Qual o valor da conta"))
amigos = int(input("Sera dividido em quantas pessoas? "))
gorjeta = int(input("qual a % da gorjeta? "))

v_gorjeta = (gorjeta /100) * conta
valor_cada = (conta + v_gorjeta) / amigos

print(f"o valor para cada pessoa é de R${valor_cada:.2f}")