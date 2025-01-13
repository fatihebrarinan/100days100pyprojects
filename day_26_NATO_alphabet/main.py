import pandas

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # Access key and value
#     pass

# student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # Access index and row
#     # Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

Nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")

Nato_dict = {row.letter: row.code for (index, row) in Nato_df.iterrows()}

is_valid = False
while not is_valid:
    try:
        word = input("Write a word: ").upper()
        output_list = [Nato_dict[letter] for letter in word]
        print(output_list)
        is_valid = True
    except KeyError:
        print("Sorry, only letter in the alphabet please.")


# Another way of doing it:
def generate_phonetic():
    word = input("Write a word: ").upper()
    try:
        output_list = [Nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letter in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

# generate_phonetic()
