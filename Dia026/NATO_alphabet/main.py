# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas as pd


name = "Angela".upper()

# with open('nato_phonetic_alphabet.csv', 'r') as f:
npa = pd.read_csv('nato_phonetic_alphabet.csv')

# for letra in name:
#     print(letra)
#     for (index, row) in npa.iterrows():
#         if row.letter == letra:
#             print(row.code)



# nome_nato = {row.letter: row.code  for (index, row) in npa.iterrows() if row.letter in name}


# print(nome_nato)


# print(npa)

phonetic_dict = {row.letter: row.code  for (index, row) in npa.iterrows()}
word =  input("Enter a word: ").upper()

output_list = [phonetic_dict[letra] for letra in word]

print(output_list)


# print(new_dict)
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

