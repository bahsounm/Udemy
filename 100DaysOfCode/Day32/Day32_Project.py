# Automated Birthday Wisher

import pandas as pd
import datetime as dt
import random as rand
import smtplib
# 1. Update the birthdays.csv
data = pd.read_csv("birthdays.csv")
birthdays = {}
# lets format the biorthdays csv to a dictionary
for i in range(len(data)):
    person = data.iloc[i]
    birthdays[person.names] = {"email": person.email, "year":int(person.year), "month": int(person.month), "day": int(person.day)}

# 2. Check if today matches a birthday in the birthdays.csv
date_today = dt.datetime.now()
year, month, day = int(date_today.year), int(date_today.month), int(date_today.day)

need_to_wish = []

for name in birthdays:
    if birthdays[name]["month"] == month and birthdays[name]["day"] == day:
        need_to_wish.append(name)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if need_to_wish:
    letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

    for name in need_to_wish:
        letter_choice = rand.choice(letters)

        with open("letter_templates/{}".format(letter_choice)) as f:
            contents = f.read()
        
        birthday_msg = contents.replace("[NAME]", name)

    # 4. Send the letter generated in step 3 to that person's email address.

    MY_EMAIL = "hassunaBazuna02@gmail.com"
    MY_PASS = "zjubmrjulerkhqcf"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASS)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthdays[name]["email"], msg="Subject:HAPPY BIRTHDAY {}\n\n{}".format(name, birthday_msg))




