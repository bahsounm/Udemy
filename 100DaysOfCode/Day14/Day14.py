# Higher Lower Game
import game_data as data
import art
import random as rand
import os

def get_option(already_used):
    option = rand.choice(data.data)
    while option["name"] in already_used:
        option = rand.choice(data.data)
    already_used.append(option["name"])
    return option, already_used

def print_question(option_a, option_b):
    print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}")
    print(art.vs)
    print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}")

def check_answer(a, b):
    if a > b:
        return "A"
    elif a < b:
        return "B"
    else:
        return None


def higher_lower():
    winning = True
    score = 0
    already_used = []
    
    option_a, already_used = get_option(already_used)
    while winning:
        option_b, already_used = get_option(already_used)
        
        print(art.logo)
        if score != 0:
            print(f"You're right!. Current Score: {score}")
        print_question(option_a, option_b)
        choice = input("Who has more follwoers? Type 'A' or 'B': ")
        
        ans = check_answer(option_a["follower_count"], option_b["follower_count"])

        if choice == ans:
            score +=1
            if choice == "B":
                option_a = option_b
            os.system('cls')
        else:
            winning = False
            os.system('cls')
            print(art.logo)
            print(f"Sorry, that's wrong. Final Score: {score}")

higher_lower()