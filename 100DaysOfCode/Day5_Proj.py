# Create a Password Generator
import random as rand

print("Welcome to the PyPassword Generator!")

num_of_letters = int(input("How many letters would you like in your password? "))
num_of_symbols = int(input("How many symbols would you like? "))
num_of_numbers = int(input("How many numbers would you like? "))


letters = ['a','b','c','d','e','f','g','h','i','j','j','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols = ['!','#','$','%','&','(',')','*','+']
numbers = ['0', '1','2','3','4','5','6','7','8','9']


our_chars = []

for i in range(num_of_numbers):
    our_chars.append(numbers[rand.randint(0, len(numbers)-1)])
for i in range(num_of_symbols):
    our_chars.append(symbols[rand.randint(0, len(symbols)-1)])
for i in range(num_of_letters):
    our_chars.append(letters[rand.randint(0, len(letters)-1)])

# password = ""
# n = len(our_chars)
# for i in range(n):
#     index = rand.randint(0, len(our_chars)-1)
#     password += our_chars[index]
#     our_chars.remove(our_chars[index])

# print(password)

# or

password = ""
rand.shuffle(our_chars)
for i in our_chars:
    password += i
print(password)

