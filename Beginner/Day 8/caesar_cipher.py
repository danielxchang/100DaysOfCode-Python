from ascii_letters import letters
from art import logo
import os

def clearConsole():
    command = 'clear'
    os.system(command)

def caesar(message, shift, mode):
    cipher = []

    if mode == "encode":
        direction = "encoded"
    else:
        direction = "decoded"
        shift *= -1

    for char in message:
        if 97 <= (char_low := ord(char.lower())) <= 122:
            idx = char_low % 97
            cipher.append(letters[(idx + shift) % len(letters)])
        else:
            cipher.append(char)

    print(f"\nHere's the {direction} result: {''.join(cipher)}")

def validate_inputs():
    while True:
        mode = input("\nType 'encode' to encrypt or 'decode' to decrypt:\n")
        if mode.lower() not in ["encode", "decode"]:
            print("\nPlease enter 'encode' or 'decode'.")
            continue
        break

    while True:
        message = input("\nType your message:\n")
        if len(message) == 0:
            print("You entered an empty message. There is nothing to encode/decode!")
            continue
        break

    while True:
        try:
            shift = int(input("\nType the shift number:\n"))
            break
        except:
            print("Please enter a number value in shift number!")

    return mode, message, shift

def main():
    print(logo)
    finished = False
    while not finished:
        mode, message, shift = validate_inputs()
        caesar(message, shift, mode)

        while True:
            repeat = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
            if repeat not in ["no", "yes"]:
                print("\nPlease enter yes or no!")
            else:
                if repeat == 'no':
                    finished = True
                break
        clearConsole()

    print("\nBye Bye!\n")

if __name__ == "__main__":
    main()