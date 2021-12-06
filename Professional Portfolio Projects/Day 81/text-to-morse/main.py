from art import logo
import os

characters = {
    'letters': {
        'A': '01',
        'B': '1000',
        'C': '1010',
        'D': '100',
        'E': '0',
        'F': '0010',
        'G': '110',
        'H': '0000',
        'I': '00',
        'J': '0111',
        'K': '101',
        'L': '0100',
        'M': '11',
        'N': '10',
        'O': '111',
        'P': '0110',
        'Q': '1101',
        'R': '010',
        'S': '000',
        'T': '1',
        'U': '001',
        'V': '0001',
        'W': '011',
        'X': '1001',
        'Y': '1011',
        'Z': '1100'
    },
    'numbers': {
        '0': '11111',
        '1': '01111',
        '2': '00111',
        '3': '00011',
        '4': '00001',
        '5': '00000',
        '6': '10000',
        '7': '11000',
        '8': '11100',
        '9': '11110'
    },
    'punctuation': {
        ' ': "/",
        '.': '010101',
        ',': '110011',
        '?': '001100',
        '\'': '011110',
        '!': '101011',
        '/': '10010',
        '(': '10110',
        ')': '101101',
        '&': '01000',
        ':': '111000',
        ';': '101010',
        '=': '10001',
        '+': '01010',
        '-': '100001',
        '_': '001101',
        '"': '010010',
        '$': '0001001',
        '@': '011010',
        '¿': '00101',
        '¡': '110001'
    }
}


def clear_console():
    command = 'clear'
    os.system(command)


def text_to_morse_converter():
    print(logo)
    string = input("Please enter string to convert: ").upper()
    morse_code = []

    # Loop through string and construct morse_code list
    for char in string:
        if char in characters['letters']:
            morse_code.append(characters['letters'][char])
        elif char in characters['numbers']:
            morse_code.append(characters['numbers'][char])
        elif char in characters['punctuation']:
            morse_code.append(characters['punctuation'][char])

    # Loop through morse_code list and construct morse_code string
    morse_code_message = ""
    for morse_char in morse_code:
        for char in morse_char:
            if char == '1':
                morse_code_message += '-'
            elif char == '0':
                morse_code_message += '.'
            else:
                morse_code_message += char
        morse_code_message += " "

    # Output result
    print(f"Morse Code Message:\n{morse_code_message}\n")

    if input("Would you like to convert another piece of text? (Enter 'y' to re-run program)\n").lower() == 'y':
        clear_console()
        text_to_morse_converter()
    else:
        return


if __name__ == "__main__":
    text_to_morse_converter()
