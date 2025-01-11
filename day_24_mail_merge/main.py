with open("Input/Names/invited_names.txt") as data:
    names = data.read().split("\n")
    for name in names:
        with open("Input/Letters/starting_letter.txt") as file:
            with open(f"Output/ReadyToSend/{name}.txt", mode="w") as letter:
                letter.write(file.read().replace("[name]", name))
