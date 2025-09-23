# Mail Merge

# lets first grav all the names of the poeple we would like to invite

with open("Input/Names/names.txt") as file1:
    names_contents = file1.read()
    names = names_contents.split("\n")
    # print(names)

# now we are going to grab our starting letter, grab the contents and replace the [Name] with the desired name

with open("Input/Letters/starting_letter.txt") as file2:
    letter_contents = file2.read()

for name in names:
    with open(f"Output/ReadyToSend/Letter_to_{name}.txt", mode="w") as file3:
        4, 11
        file3.write(letter_contents[:5] + name + letter_contents[11:])

    