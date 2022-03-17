# with open('arquivo1.txt', 'r') as arq1:
#     for linha in arq1:
#         with open('arquivo2.txt', 'r') as arq2:
#             for linha2 in arq2:
#                 if linha == linha2:
#                     result.append(int(linha))
#

# result = [int(linha) for linha in open('arquivo1.txt', 'r') if
#           int(linha) in [int(linha2) for linha2 in open('arquivo2.txt', 'r')]]

result = [int(linha) for linha in open('arquivo1.txt', 'r') if
          int(linha) in [int(linha2) for linha2 in open('arquivo2.txt', 'r')]]

# Write your code above 👆

print(result)

# list comprehesion

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_list = [number for number in numbers if number % 2 == 0]
# print(new_list)
#
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#
# new_list2 = []
# for number in numbers:
#     if number % 2 == 0:
#         new_list2.append(number)
# print(new_list2)
#
#
# new_list2 = [number + 1 for number in numbers]

# names = ['maria', 'jose', 'pedro', 'joao', 'maria', 'jose', 'pedro', 'joao', 'maria', 'jose', 'pedro', 'joao']
