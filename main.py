import pandas

nato_alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet_dict ={row.letter:row.code for (index,row) in nato_alphabet_data.iterrows()}

user_name = input("Enter a name:").upper()
name_to_nato_alpha =  [nato_alphabet_dict[f"{letter}"] for letter in user_name]

print(name_to_nato_alpha)