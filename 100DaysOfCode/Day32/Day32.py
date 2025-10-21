import smtplib

# first param is the location / identity of the email, gmail, hotmail, yahoo, etc

my_email = "hassunaBazuna02@gmail.com"
passw = "zjubmrjulerkhqcf"

# with smtplib.SMTP("smtp.gmail.com") as connection: 
#     connection.starttls() # ensures our connection is secure 

#     connection.login(user=my_email, password=passw)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="mhbahsou@gmail.com", 
#         msg="Subject:This is a Test\n\nHello this is a test from the application"
#     )


import datetime as dt
import random as rand
# # getting date time
# time_now = dt.datetime.now()
# print(time_now,"\n",time_now.year, time_now.month, time_now.day)
# # creating our own date time
# date_of_birth = dt.datetime(year=2002, month=7,day=9)



# motivational quote email sender
import smtplib
import datetime as dt
import random as rand
MY_EMAIL = "hassunaBazuna02@gmail.com"
MY_PASS = "zjubmrjulerkhqcf"
time_now = dt.datetime.now()
weekday = time_now.weekday()

if weekday == 1:
    with open("quotes.txt") as f:
        all_quotes = f.readlines()
        quote = rand.choice(all_quotes)
    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASS)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject:Monday Motivation\n\n{}".format(quote))