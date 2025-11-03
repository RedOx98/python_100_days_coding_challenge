import pandas
import pandas as pd
# letter_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

letter = pd.read_csv("nato_phonetic_alphabet.csv")
letter_dict = letter.to_dict()
whole_dict = pandas.DataFrame(letter)

# print(whole_dict)
# Looping through dictionaries:
word = input("input something")
final_name = {}
# for (index, row) in whole_dict.iterrows():
full_dict = {row.letter:row.code for (index, row) in whole_dict.iterrows()}

output_list = {letter: full_dict[letter] for letter in word if letter in full_dict}

print(output_list)




# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

