

# TODO: create a dictionary with the following keys:















#
# import pandas as pd
#
# student_dict = {
#     'name': ['Arya', 'Samwell', 'Jon', 'Sansa', 'Robb', 'Bran', 'Rickon'],
#     'age': [14, 14, 16, 12, 17, 8, 16],
#     # 'name': ['Ana', 'Felipe', 'Rafael', 'João', 'Maria', 'José'],
#     # 'age': [19, 17, 18, 19, 20, 18],
# }
#
# # for (key, value) in student_dict.items():
# #     print(key, value)
#
# student_df = pd.DataFrame(student_dict)
# print(student_df)
#
# for (index, row) in student_df.iterrows():
#     print( row.name)
#     # if row['name'] == 'Jon':
#     #     print(index, row)
#         # print( row.age)


'''Exercício 26: Dicionário com compreensão'''

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆
#
# weather_f = { key: (value * 9/5) + 32 for key, value in weather_c.items() }
#
# # Write your code 👇 below:
#
#
#
# print(weather_f)


''' Ecercise 1'''

# names = ['Socrates', 'Archimedes', 'Plato', 'Aristotle',]

# studantes_scores = {student : new_value for student in name}

# jeito A
# passed_students = {student: values for student,values in studantes_scores if values >= 60 }
