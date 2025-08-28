# Hangman Project
import random as rand
import Day7_words as d7w
import Day7_art as d7a

def hangman():
    
    chosen_word = rand.choice(d7w.word_bank)
    placeholder = "_" * len(chosen_word)
    lives = 6
    letters_left = len(chosen_word)

    d7a.hangman_pics.reverse()
    current_gallow = d7a.hangman_pics[lives]

    print(chosen_word)
    print(current_gallow)
    print(f"Word to Guess: {placeholder}")

    while lives >0:
        count = 0
        print("*"*10 + str(lives)+ "/6 LIVES LEFT*"*10)
        user_guess = input("Make a guess? (lowercase please) ").lower()
        
        while user_guess in placeholder or len(user_guess) != 1:
            user_guess = input("*** You have already chosen this letter\nMake another guess? (lowercase please) ***").lower()
       
        for i in range(len(chosen_word)):
            if chosen_word[i] == user_guess:
                letters_left -=1
                count +=1
                temp = list(placeholder)
                temp[i] = user_guess
                placeholder = ''.join(temp)
            
            if letters_left == 0:
                return True
        
        if count == 0:
            lives -=1
        
        print(d7a.hangman_pics[lives])
        print(f"Word to Guess: {placeholder}")
    
    return False

if hangman():
    print("***************YOU WIN***************")
else:
    print("***************YOU LOSE***************")


    
