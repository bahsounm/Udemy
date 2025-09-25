import random as rand
# List comprehension
new_list = [n*2 for n in range(1,5)]
print(new_list)

# Conditional List comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
new_list = [name for name in names if len(name) < 5 ]
print(new_list)

# dictionary comprehension using a lsit
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

student_scores = {student:rand.randint(50,100) for student in names}
print(student_scores)

# dictionary comprehension using another dict
passed_students = {student:score for student,score in student_scores.items() if score > 70}
print(passed_students)

# iterating over a pandaData frame

my_class = {
    "students":["angelo", "mia", "chris"],
    "scores" :[90, 75, 60]

}

import pandas

class_dataframe = pandas.DataFrame(my_class)

print(class_dataframe)

# loop through each rows of the data frame
for (index, row) in class_dataframe.iterrows():
    print(row.students)