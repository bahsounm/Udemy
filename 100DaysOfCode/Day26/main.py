import pandas as pd
#TODO 1. Create a dictionary in this format:
df = pd.read_csv('nato_phonetic_alphabet.csv')
new_dict = {}
for (index, row) in df.iterrows():
    new_dict[row.letter] = row.code

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter word: ")

phonetic_code = [new_dict[item] for item in list(word.upper())]

print(phonetic_code)
