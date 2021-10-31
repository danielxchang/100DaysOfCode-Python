from random import randint
from art import logo

def set_difficulty():
    while True:
        mode = input("Choose the difficulty. Easy or hard mode? Type 'easy' or 'hard' to select the mode: ").lower()
        if mode not in ['easy', 'hard']:
            print("Please type 'easy' or 'hard' to select difficulty level and start game!")
            continue
        break
    return mode

def num_of_turns(mode):
    easy_turns, hard_turns = 10, 5
    return easy_turns if mode == 'easy' else hard_turns

def check_guess(guess, answer):
    if guess == answer:
        print(f"You got it! The answer was {answer}.")
        return True
    elif guess > answer:
        print("Too high.")
    else:
        print("Too low")
    return False

def retrieve_guess():
    while True:
        try:
            guess = int(input("Make a guess: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Guess must be an integer between 1 and 100.")
        except:
            print("Please enter an integer between 1 and 100.")

def guessing_game(mode):
    answer = randint(1, 100)
    turns = num_of_turns(mode)
    print(f"answer is {answer}")
    for turn in range(turns):
        print(f"You have {turns} attempt{'' if turns == 1 else 's'} remaining to guess the number.")

        if check_guess(retrieve_guess(), answer):
            break

        turns -= 1
        if turns > 0:
            print("Guess again.\n")
        else:
            print(f"You've run out of guesses, you lose. The answer was {answer}.\n")

if __name__ == "__main__":
    print(logo)
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    guessing_game(set_difficulty())