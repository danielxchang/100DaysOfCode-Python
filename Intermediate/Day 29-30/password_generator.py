from random import choice, shuffle, randint

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_random_chars(n_letters, n_symbols, n_numbers):
    letters_list = [choice(letters) for _ in range(n_letters)]
    symbols_list = [choice(symbols) for _ in range(n_symbols)]
    numbers_list = [choice(numbers) for _ in range(n_numbers)]
    return letters_list + symbols_list + numbers_list


def create_password():
    characters = generate_random_chars(randint(8, 10), randint(2, 4), randint(2, 4))
    shuffle(characters)
    return "".join(characters)
