from random import choice, shuffle
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_random_chars(n_letters, n_symbols, n_numbers):
    characters = []
    for i in range(n_letters):
        characters.append(choice(letters))
    for i in range(n_symbols):
        characters.append(choice(symbols))
    for i in range(n_numbers):
        characters.append(choice(numbers))
    return characters

def create_password(n_letters, n_symbols, n_numbers):
    characters = generate_random_chars(n_letters, n_symbols, n_numbers)
    shuffle(characters)
    return "".join(characters)

def pw_parameters():
    while True:
        try:
            letters = int(input("How many letters would you like in your password?\n"))
            symbols = int(input("How many symbols would you like?\n"))
            numbers = int(input("How many numbers would you like?\n"))
            break
        except:
            print("Please re-enter password requirements you would like\n")

    return letters, symbols, numbers

def main():
    print("Welcome to the PyPassword Generator!")
    n_letters, n_symbols, n_numbers = pw_parameters()
    print(create_password(n_letters, n_symbols, n_numbers))

if __name__ == "__main__":
    main()