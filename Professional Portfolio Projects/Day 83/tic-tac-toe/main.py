import os
from art import logo
from board import Board
from player import Player


def clear_console(board):
    command = 'clear'
    os.system(command)
    print(logo)
    board.print_board()


def tic_tac_toe():
    players = [Player(0), Player(1)]
    board = Board()
    turn = 0

    while True:
        clear_console(board)

        while True:
            row, column, mark = players[turn].take_turn()
            if board.check_choice(row, column) != -1:
                break
            else:
                clear_console(board)
                print("That spot has been taken. Pick an open spot.")

        if board.update_board(row, column, mark):
            clear_console(board)
            print(f"GAME OVER! Player {turn + 1} has won!\n")
            break

        if board.is_draw():
            clear_console(board)
            print(f"IT'S A DRAW!\n")
            break

        turn = 1 if turn == 0 else 0

    if input("Would you like to play again? Enter 'y' to play again: ").lower() == 'y':
        tic_tac_toe()


if __name__ == '__main__':
    tic_tac_toe()
