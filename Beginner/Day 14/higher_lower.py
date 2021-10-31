from art import logo, vs
from random import choice
from game_data import data
import os

def clearConsole():
    command = 'clear'
    os.system(command)

def random_choice():
    return choice(data)

def compare(a, b, guess):
    if a['follower_count'] > b['follower_count']:
        return guess == "A"
    else:
        return guess == "B"

def guess_A_or_B(A, B):
    while True:
        if (guess := input("Who has more followers? Type 'A' or 'B': ").upper()) in ['A', 'B']:
            return compare(A, B, guess)
        else:
            print("Please enter 'A' or 'B'.")

def format_data(person):
    return f"{person['name']}, {person['description']}, from {person['country']}"

def game():
    alive = True
    score = 0
    last_person = None
    while True:
        clearConsole()
        print(logo)

        if not alive:
            print(f"Sorry, that's wrong. Final score: {score}\n")
            break
        elif score != 0:
            print(f"You're right! Current score: {score}")

        a = random_choice() if last_person == None else last_person
        while (b := random_choice()) == a:
            continue
        last_person = b

        print(f"Compare A: {format_data(a)}.")
        print(vs)
        print(f"Against B: {format_data(b)}.")

        if guess_A_or_B(a, b):
            score += 1
        else:
            alive = False

if __name__ == "__main__":
    game()