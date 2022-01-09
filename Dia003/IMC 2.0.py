# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# Deve informar a interpretação de seu IMC com base no valor do IMC.

# Abaixo de 18,5 eles estão abaixo do peso
# Acima de 18,5, mas abaixo de 25, eles têm um peso normal
# Acima de 25, mas abaixo de 30, eles estão ligeiramente acima do peso
# Acima de 30, mas abaixo de 35, eles são obesos
# Acima de 35 eles são clinicamente obesos.

imc = weight / (height ** 2)
print(imc)

imc = round(weight / (height ** 2))
print(imc)
imc = round(weight / (height ** 2),2)
print(imc)
imc = round(weight / (height ** 2),3)
print(imc)

# outra forma de fazer isso
imc = float(f'{(weight / (height ** 2)):.2f}')
print(type(imc))
print(imc)
if imc < 18.5:
    print(f"Your BMI is {imc}, you are underweight.")
elif imc < 25:
    print(f"Your BMI is {imc}, you have a normal weight.")
elif imc <30:
    print(f"Your BMI is {imc}, you are slightly overweight.")
elif imc <35:
    print(f"Your BMI is {imc}, you are obese.")
else:
    print(f"Your BMI is {imc}, you are clinically obese.")
print(imc)