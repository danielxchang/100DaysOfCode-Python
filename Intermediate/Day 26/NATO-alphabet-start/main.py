import pandas

# TODO 1. Create a dictionary in this format:
nato_data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row[0]: row[1] for idx, row in nato_data.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        nato_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Please enter only letters in the alphabet.")
        generate_phonetic()
    else:
        print(nato_list)


generate_phonetic()
