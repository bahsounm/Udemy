import pandas as pd
#TODO 1. Create a dictionary in this format:
df = pd.read_csv('nato_phonetic_alphabet.csv')
new_dict = {}
for (index, row) in df.iterrows():
    new_dict[row.letter] = row.code

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phoentic():
    word = input("Enter word: ")
    try:
        phonetic_code = [new_dict[item] for item in list(word.upper())]
    except KeyError:
        print("Sorry, only letter in the alphabet please")
        generate_phoentic()
    else:
        print(phonetic_code)
        
generate_phoentic()
