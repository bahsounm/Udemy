# Debugging

def my_func():
    for i in range(1, 21):
        if i == 20:
            print("We got to 20")

my_func()
# nothjing is getting printed why?

# 1) Describe the problem: suppsoed to print at 20 but for loop never gets to 20 because for loop range is not inclsuve of the greater bound. the assumpotion in thecode here is that i reaches 20

import random as rand

dice = ["1", "2", "3", "4", "5", "6"]

dice_num = rand.randint(1,6)
# add this to see
print(dice_num)
print(dice[dice_num])

# 2) reproduce the bug. see how it happens and what causes it. aafter adding the  print we see that the rand int between 1 and 6 sometimes produces 6 because the lsit is 0-5 not 6


 