# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age = int (age)
meses = 90*12 - age * 12
semanas = 90*52 - age * 52
dias = 90*365 - age * 365

print(f"You have {dias} days, {semanas} weeks, and {meses} months left.")


