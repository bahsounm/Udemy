# Tip Calculator
print("Welcome to the print Calculator!")
bill_total = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))/100
split = int(input("How many people to split the bill? "))
print(f"Each person should pay {round((bill_total+ bill_total*tip)/split, ndigits=2)}")