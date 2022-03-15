# TODO import data of weather.csv normal method

# data = []
# with open ('weather_data.csv') as f:
#     data_weather = f.readlines()
#     for line in data_weather:
#         replace_line = line.replace('\n', '')
#         data.append(replace_line)
#
# print(data)
#

# TODO import data of weather.csv with csv module
# import csv
#
# with open ('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)


# jeito 2
# data = csv.reader(data_file)
# temp_temperature = []
# temperature = []
#
#
#
#
# for row in data:
#     temp_temperature.append(row[1])
# print(temp_temperature)
# for line in range(1, len(temp_temperature)):
#     temperature.append(int(temp_temperature[line]))
# print(temperature)


# TODO import data of weather.csv with pandas
import pandas as pd

data = pd.read_csv('weather_data.csv')
print(data[::-1])



# TODO import data of brazil_states.json
