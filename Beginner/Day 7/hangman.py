from random import choice
import os
from re import finditer
from hangman_art import stages, logo
from hangman_words import word_list

def clearConsole():
    command = 'clear'
    os.system(command)

def output_outcome(lives):
    if lives == 0:
        print("Game over, you lose!\n")
    else:
        print("Congratulations! You win!\n")

def is_valid_guess(guess):
    if type(guess) is str and len(guess) == 1:
        return 97 <= ord(guess) <= 122

def play_game(lives, chosen_word):
    blanks = ["_" for _ in range(len(chosen_word))]
    guesses = []

    while '_' in blanks and lives > 0:
        guess = input("Guess a letter: ").lower()
        clearConsole()
        if not is_valid_guess(guess):
            print("Please enter a single letter!")
        elif guess in guesses:
            print(f"You've already guessed {guess}.")
        else:
            guesses.append(guess)
            matches = [match.start() for match in finditer(guess, chosen_word)]
            if len(matches) > 0:
                for match in matches:
                    blanks[match] = guess
            else:
                lives -= 1
                last = "lost your last" if lives == 0 else "lose a"
                print(f"You guessed {guess}, that's not in the word. You {last} life.")

        print(" ".join(blanks))
        print(stages[lives])

    output_outcome(lives)

def main():
    print(logo)
    lives = 6
    chosen_word = choice(word_list)
    play_game(lives, chosen_word)

if __name__ == "__main__":
    main()


