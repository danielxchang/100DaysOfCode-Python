# # import csv
# #
# # # with open("weather_data.csv", mode="r") as weather_file:
# # #     data = weather_file.readlines()
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if (temp := row[1]) != 'temp':
# #             temperatures.append(int(temp))
# #     print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(type(data["temp"]))
#
# # data_dict = data.to_dict()
# # print(data_dict)
#
# # temp_list = data['temp'].to_list()
# # print(data['temp'].max())
# # print(data.condition)
#
# # print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == 'Monday']
# fahrenheit = lambda temp: (temp * (9 / 5) + 32)
# monday_temp = int(monday.temp)
# # print(monday_temp)
# # print(fahrenheit(monday_temp))
#
#
# data_dict = {
#     "students": ["Amy", "James", "Bill"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
#

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_colors_data = data["Primary Fur Color"]
fur_colors = fur_colors_data.drop_duplicates().to_list()[1:]
fur_colors_list = fur_colors_data.to_list()

data_dict = {
    'Fur Color': fur_colors,
    'Count': []
}

for fur_color in fur_colors:
    count = fur_colors_list.count(fur_color)
    data_dict['Count'].append(count)

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")



