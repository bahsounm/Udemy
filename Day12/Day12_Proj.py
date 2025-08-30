# The Number Guessing Game
import art
import random as rand

def num_guess_game(difficulty):
    if difficulty == 'easy':
        num_of_tries = 10
    else:
        num_of_tries = 5
    
    num_to_guess = rand.randint(1,100)
    guessed_correct = False

    while guessed_correct == False and num_of_tries > 0:
        guess = input(f"You have {num_of_tries} attempts remaining to guess the number\nMake a Guess: ")

        if guess == num_to_guess:
            guessed_correct == True
            print(f"You got it! The answer was {num_to_guess}")
        elif guess > num_to_guess:
            print("Too High. \nGuess Again.")
        elif guess < num_to_guess:
            print("Too Low. \nGuess Again.")
        num_of_tries-=1
        
print(art.title)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
num_guess_game(difficulty)
