# Write your code below this line 👇

def prime_checker(number):
    se_dividi =0
    for numero in range(1,number+1):
        if number % numero == 0:
            se_dividi += 1
    if se_dividi == 2:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
