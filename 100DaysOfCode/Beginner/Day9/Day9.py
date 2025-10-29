# Python Dictionaries

a = "a"

d = {a: 1, 
     "b": 2,
     "c": 3
    }

print(d[a])

# this is a way of adding to a dictionary, or depending on the key this could be a way of editing a value
d["d"] = 4

print(d)

# Note you cannot have the same key twice, it will just refer to the same thing
print("")
for item in d:
    print(item) # item is the key
    print(d[item]) # use the item to get the value since hte item is the key

#-------------------------------------------------------------------------------

# Nested List in dictionary

travel_log = {"France": ["Paris", "Lille", "Dijon"],
              "Canada": ["Toronto", "Montreal"]
             }

# print Lille

print(travel_log["France"][1])

# nested list in in list

nested_list = ["a", "b", ["c", "d"]]
print(nested_list[2][1])

