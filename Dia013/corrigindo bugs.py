############DEBUGGING#####################

# # Describe Problem
# python in range, ( numero inicial, para um numero antes desse numero, se colocarmos o numero 20, ekle trabalha
# até o 19)
#def my_function():
#  for i in range(1, 21):
#    if i == 20:
#      print("You got it")
#my_function()

# # Reproduce the Bug
#(o range de numeros ia de 0, a 5 e nao de 1 a 6)
#from random import randint
#dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
#dice_num = randint(0, 5)
#print(dice_imgs[dice_num])

# # Play Computer
#(nao existia uma regra par ao ano 1994 e para anos inferiores a a 1980)
#year = int(input("What's your year of birth?"))
#if year > 1980 and year < 1994:
#  print("You are a millenial.")
#elif year >= 1994:
#  print("You are a Gen Z.")
#else:
#  print("voce é de outra geração")

# # Fix the Errors
#(faltou converter age em inteiro par acomparar, e tranformar o print em uma f string)
#age = int(input("How old are you?"))
#if age > 18:
#  print(f"You can drive at age {age}.")

# #Print is Your Friend
#pages = 0
#word_per_page = 0
#pages = int(input("Number of pages: "))
#word_per_page == int(input("Number of words per page: "))
#total_words = pages * word_per_page
#print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#       b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])