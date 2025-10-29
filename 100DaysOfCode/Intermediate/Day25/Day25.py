# # reading data froma CSV

# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()

# #     print(data)

# # data doesnt look good but can use libraries to help read csv nicer
# import csv
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temps = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temps.append(int(row[1]))
# #     print(temps)

# # use pandas to perform data analysis
# import pandas
# # pandas takes the first row as the column titles, then the rest is the data
# # data is a dataframe, is beasically the equilvant of the excell sheet
# # just one of the column, its a series, and its equailit to a list
# data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# data_list = data["temp"].to_list()

# print(sum(data_list)/len(data_list))
# # how we can get rows based on conditions
# print(data[data.temp == data.temp.max()])



# # creating a data frame from scratch

# students = {
#     "Students": ["Amy", "James", "Angela"],
#     "Scores": [76, 56, 65]
# }

# data  = pandas.DataFrame(students)
# print(data)

# # conversion to csv

# data.to_csv("student.csv")
#-----------------------------------------------------------------------------------------------------------
# squirrel dataset 

import pandas

data = pandas.read_csv("nys_data.csv")

fur_color_data = (data["Primary Fur Color"].dropna()).to_list()

fur_colors = {"Fur Color": [], "Count": []}
for color in fur_color_data:
    if color in fur_colors["Fur Color"]:
        idx = fur_colors["Fur Color"].index(color)
        fur_colors["Count"][idx] +=1
    else:
        fur_colors["Fur Color"].append(color)
        fur_colors["Count"].append(1)


print(fur_colors)
data = pandas.DataFrame(fur_colors)
data.to_csv("SquirrelColors.csv")


