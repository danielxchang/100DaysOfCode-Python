from random import choice
import os
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def clearConsole():
    command = 'clear'
    os.system(command)

def hit():
    return choice(cards)

def score(hand):
    total = sum(hand)

    if total <= 21:
        if total == 21 and len(hand) == 2:
            return 0
        return total
    else:
        aces = hand.count(11)
        for i in range(aces):
            if total > 21:
                total -= 10
                hand[hand.index(11)] = 1
        return total

def add_or_pass():
    while True:
        if (ans := input("\nType 'y' to get another card, type 'n' to pass: ")) not in ['y', 'n']:
            print("Please enter 'y' or 'n'.")
        else:
            return ans

def update_dealer(dealer):
    while 0 < score(dealer) < 17:
        dealer.append(hit())

def print_result(player, dealer):
    p_score = score(player)
    d_score = score(dealer)
    print(f"\n\tYour final hand: {player}, final score: {p_score}")
    print(f"\tComputer's final hand: {dealer}, final score: {d_score}\n")

    if p_score == 0 and d_score != 0:
        result = "Blackjack! You win 😁"
    elif d_score == 0 and p_score != 0:
        result = "Dealer Blackjack. You lose 😭"
    elif p_score > 21 and d_score <= 21:
        result = "You went over. You lose 😭"
    elif d_score > 21 and p_score <= 21:
        result = "Opponent went over. You win 😁"
    elif d_score > p_score and d_score < 22:
        result = "Opponent wins. You lose 😭"
    elif p_score > d_score and p_score < 22:
        result = "You win! 😁"
    else:
        result = "It's a draw. Play another round!"

    print(result.upper())

def display_round(player, dealer, last=False):
    #print(f"\nPlayer: {player}, Dealer: {dealer}\n")
    if not last:
        print(f"\n\tYour cards: {player}, current score: {score(player)}")
        print(f"\tComputer's first card: {dealer[0]}")
        return add_or_pass()
    else:
        update_dealer(dealer)
        print_result(player, dealer)

def play_game():
    player = [hit() for _ in range(2)]
    dealer = [hit() for _ in range(2)]
    while True:
        if score(player) == 0 or score(dealer) == 0:
            display_round(player, dealer, last=True)
            break
        elif display_round(player, dealer) == 'n':
            display_round(player, dealer, last=True)
            break
        else:
            player.append(hit())

            if score(player) >= 21:
                display_round(player, dealer, last=True)
                break

def start_game():
    print(logo)
    while True:
        if (start := input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ")) == 'y':
            clearConsole()
            print(logo)
            play_game()
        elif start == 'n':
            break
        else:
            print("Please enter 'y' or 'n'.")
            continue

if __name__ == '__main__':
    start_game()