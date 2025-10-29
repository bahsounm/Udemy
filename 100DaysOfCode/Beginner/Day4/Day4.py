# Random Module
import random as rand
import Day4_Mod

# randint chooses a random number between a and b

print(rand.randint(1,10))
# How we can create our own module
print(Day4_Mod.my_fav_num)

print(rand.random())
#-------------------------------------------------------------------------------
# Offset and Appending Items to Lists
# Note the use of offset here ius reffering to index

province = ["Ontario", "Manitoba", "Nova Scotia", "Quebec", "British Columbia"]

# this is how we can access the elements in the list. Note: it starts at 0
print(province[0])

# can do changes
province[0] = "Ontario Baby"
print(province[0])

# we can add to the list
print(province)
province.append("Yukon")
print(province)

# we can add multiple items to the list
province.extend(["North West Territories", "Nunavut"])
print(province)
# we can pop the last item
province.pop()
print(province)

# we can speicfy what we want to remove
province.remove("Ontario Baby")
print(province)

# we can insert at a specific location
province.insert(0, "Hello World")
print(province)

# we can also clear the list
# province.clear()
# print(province)
#-------------------------------------------------------------------------------
# we want to print a random element from the list of provinces

rand_prov = rand.randint(0, len(province)-1)
print(province[rand_prov])
# or
print(rand.choice(province))
#-------------------------------------------------------------------------------
# Working with nested lists and index errors


