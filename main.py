import pandas

#Read NATO alphabet from file
nato_alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")

#Create dictionary from NATO alphabet
nato_alphabet_dict ={row.letter:row.code for (index,row) in nato_alphabet_data.iterrows()}

#Have the user inputer their name (needs to have each letter become uppercase for the dictionary keys to match
user_name = input("Enter a name:").upper()
name_to_nato_alpha =  [nato_alphabet_dict[f"{letter}"] for letter in user_name]

#print out the name with letter from NATO alphabet
print(name_to_nato_alpha)