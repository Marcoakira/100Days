# TODO: create one CSV squirrel_count.csv file with Series about colors and count of squirrels

import pandas as pd

central_park = pd.read_csv('2018_central_park_squirrel_census_-_Squirrel_Data.csv')

squirrel_collors_count = central_park['Primary Fur Color'].value_counts()

squirrel_collors_count.to_csv('squirrel_count.csv')











# import pandas as pd
#
# data = pd.read_csv('weather_data.csv')
# # print(type(data))
# # print(data[::-1])
# # print(type(data['temp']))
#
# data.to_dict()
#
# temp_list = data['temp'].to_list()
# print(temp_list)
#
# #
# # avarage = sum(temp_list) / len(temp_list)
# #
# # print(
# #     f'A temperatura média é {avarage}')
# #
# # # outra forma de fazer
# #
# # print(data['temp'].mean())
#
# # print(f"the max value is {data['temp'].max()}")
#
# # print(data[data.day == 'Saturday'])
# #
# # print(data[data['temp'] == data.temp.max()])
# #
# # mondays = data[data.day == 'Monday']
#
# # print(mondays)
#
# # print(mondays.condition)
# '''
# # convertendo farhenheit para celsius
# '''
# # as_temp = data.temp
# #
# # print(as_temp)
# #
# # def f(x):
# #     x = x * 1.8 + 32
# #     return float(x)
# #
# # as_temp = as_temp.apply(f)
# #
# # print(as_temp)
#
# '''
# # create a dataframe from scratch
# '''
#
# data_dict = {
#     'student': ['Ana', 'Bia', 'Carlos', 'Daniel', 'Eduardo', 'Fernando'],
#     'score': [9.5, 8, 7.5, 8.5, 9, 6]
# }
# pd_data_dict = pd.DataFrame(data_dict)
#
# print(pd_data_dict)
#
# pd_data_dict.to_csv('new_data.csv')