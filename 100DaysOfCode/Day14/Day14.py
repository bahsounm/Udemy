# Higher Lower Game
import game_data as data
import art
import random as rand

print(art.logo)

score = 0

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



def higher_lower():
    winning = True
    already_used = []
    option_a, already_used = get_option(already_used)
    while winning:
        option_b, already_used = get_option(already_used)

        print_question(option_a, option_b)

        choice = input("Who has more follwoers? Type 'A' or 'B': ")

        if (option_a['follower_count'] > option_b["follower_count"] and choice == 'A') or (option_a['follower_count'] < option_b["follower_count"] and choice == 'B'):
            
        else:
            winning = False

higher_lower()