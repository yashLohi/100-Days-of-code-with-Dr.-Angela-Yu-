# with open("weather_data.csv.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
# # with open("weather_data.csv.csv") as data_file:
# #     data = csv.reader(data_file)
# #
# #     for row in data:
# #         print(row)
#
# with open("weather_data.csv.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#
#         if row[1] != "temp":            # print(row[1])
#             temperature.append(int(row[1]))
#     print(temperature)


import pandas
#
# # data = pandas.read_csv("weather_data.csv.csv")
# # print(data)
#
data = pandas.read_csv("weather_data.csv.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(len(temp_list))
#
#
# # average = sum(temp_list) / len(temp_list)
# # print(average)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # get data in coloums
# print(data["condition"])
# print(data.condition)


# get data in row
print(data[data.day == "Monday"])
print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)