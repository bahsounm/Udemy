# Rock Paper Scissors
import random as rand

choice = int(input("what do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))

possible_hands = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""", """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""", """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]

comp_choice = rand.randint(0,2)

print(possible_hands[choice])
print("\nComputer Chose:\n")
print(possible_hands[comp_choice])

if choice == comp_choice:
    print("You Tied")
elif (choice == 0 and comp_choice == 2) or (choice == 1 and comp_choice == 0) or (choice == 2 and comp_choice == 1):
    print("You Win")
else:
    print("You Lose")