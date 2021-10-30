from art import logo
import os

def clearConsole():
    command = 'clear'
    os.system(command)

def add(first, second):
    return first + second

def subtract(first, second):
    return first - second

def multiply(first, second):
    return first * second

def divide(first, second):
    return first / second

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def validate_inputs(char, type_char):
    try:
        if type_char == "op":
            if char in ['+', '-', '*', '/']:
                return char
            else:
                print("Please enter one of the four operators.")
        elif len(char) == 0:
            return False
        else:
            return float(char)

    except ValueError:
        print("Please enter a number.")
        return False

def get_inputs(first):
    while True:
        if op := validate_inputs(input("Pick an operation: "), "op"):
            break

    while True:
        if second := validate_inputs(input("What's the next number? "), "number"):
            break

    result = operations[op](first, second)
    print(f'{first} {op} {second} = {result}')

    while True:
        continue_calc = input(f"Type 'y' to continue calculating with {round(result, 2)}, or type 'n' to start a new calculation: ")

        if continue_calc not in ['n', 'y']:
            print("Please enter 'y' or 'n'.")
        elif continue_calc == 'n':
            clearConsole()
            return
        else:
            break

    print('\n')
    get_inputs(result)

def calculator():
    print(logo)
    while True:
        if first := validate_inputs(input("What's the first number? "), "number"):
            break

    for op in operations:
        print(op)

    get_inputs(first)
    calculator()

if __name__ == "__main__":
    calculator()