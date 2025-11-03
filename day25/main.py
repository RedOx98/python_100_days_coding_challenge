import csv
import pandas

# data = pandas.read_csv("weather_data.csv")
# with open("weather_data.csv") as data:
#     line = csv.reader(data)
#     temp = []
#     for d in line:
#         if d[1] != 'temp':
#             temp.append(d[1])
#         # print(d)
# # temp.remove("temp")
# print(temp)
# 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv
# # print(data_dict)
# temp_list = data["temp"]
# print(data.condition)
# print(data[data.day == "Monday"])
# print(type(data))
# print(data["temp"].max())
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# temp = monday.temp
# # 1 degs == 2.12Farenheit
# # x degs == x
# deg_farenheit = (temp * 2.12)
# print(deg_farenheit)


# pd.to_csv("new_data.csv")
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# data_dict = data.to_dict()
# pd = pandas.DataFrame(data_dict)
# # age = data[data.Age == "Adult"]
# color_list = {
#
#         "color": "",
#         "count": ""
# }
color_count = data["Primary Fur Color"].value_counts().reset_index()

color_count.columns = ["colors", "count"]
color_count.to_csv("fur_count_analysis.csv")
# # for _ in colors:
# #     color_list["color"] = _
# #     color_list["count"] = data[colors[_]]
# #     print(data[colors == colors[_]])
#
# with open("fur_count_analysis.csv") as dat:
#     viewd = dat.read()
#     print(viewd)
# print(colors)

data = pandas.read_csv("fur_count_analysis.csv")
dictw = data.to_dict()
viewd = pandas.DataFrame(dictw)
print(viewd)