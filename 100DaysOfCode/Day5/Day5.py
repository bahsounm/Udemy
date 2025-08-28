# Using a for loop with lists
import random
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)

# or

for fruit in range(0, len(fruits)):
    print(fruits[fruit])

#-------------------------------------------------------------------------------

scores = random.sample(range(1,101), 15)
maxx = -1
for score in scores:
    if score > maxx:
        maxx = score
print(max(scores))
print(f"The highest score is {maxx}")