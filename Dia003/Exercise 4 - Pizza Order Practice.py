# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇



pizza_price = 0
pepperoni = 0
cheese = 0


if size == "S":
    pizza_price = 15
    if add_pepperoni == "Y":
        pepperoni += 2

elif size == "M":
    pizza_price = 20
    if add_pepperoni == "Y":
        pepperoni += 3

elif size == "L":
    pizza_price = 20
    if add_pepperoni == "Y":
        pepperoni += 3


if extra_cheese == "Y":
    pizza_price += 1

print(f"O valor da pizza{pizza_price} no total de {pizza_price+pepperoni+cheese} ")
print(f" o peperone é {pepperoni}")