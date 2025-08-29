# BlackJack
import art
import random as rand
import os

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def deal_card(num_of_cards=1):
    """This func determines what hand the players will get"""
    hand = []
    for i in range(num_of_cards):
        hand.append(rand.choice(cards))
    return hand

def calc_hand(hand):
    """This func takes the hand and calculates the score"""
    s = sum(hand)
    if 11 in hand and s > 21:
        s = s-10
    return s



def blackjack():
    """This is the main func that will simulate blackjack"""
    players = {"user": {"hand": deal_card(2)}, 
               "cpu":  {"hand": deal_card(1)},
               }
    players["user"]["score"] = calc_hand(players["user"]["hand"])
    players["cpu"]["score"]  = calc_hand(players["cpu"]["hand"])

    # Logic for Player
    while players["user"]["score"] < 21:
        print(f"    Your cards: {players['user']['hand']}, current score: {players['user']['score']}")
        print(f"    Computer's first card: {players['cpu']['hand'][0]}")
        if input("Type 'y' to get another card, type 'n' to pass: ").lower() != 'y':
            break
        players["user"]["hand"] += (deal_card(1))
        players["user"]["score"] = calc_hand(players["user"]["hand"])

    
    # Logic for the CPU
    while players["cpu"]["score"] < 17 and players["user"]["score"] <= 21:
        players["cpu"]["hand"].extend(deal_card(1))
        players["cpu"]["score"] = calc_hand(players["cpu"]["hand"])


    print(f"    Your Final Hand: {players['user']['hand']}, Final score: {players['user']['score']}")
    print(f"    Computer's Final Hand: {players['cpu']['hand']}, Final score: {players['cpu']['score']}")
    
    
    user, cpu = players["user"]["score"], players["cpu"]["score"]
    if user > 21:
        print("You Lose")
    elif cpu > 21 or user > cpu:
        print("You Win")
    elif user == cpu:
        print("Draw")
    else:
        print("You Lose")



while True:
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play == "y":
        os.system('cls')
        print(art.title)
        blackjack()
    else:
        break