import os
from art import logo

def clearConsole():
    command = 'clear'
    os.system(command)

def retrieve_bid():
    while True:
        if len(bidder := input("What is your name? ")) > 0:
            break
        else:
            print("Please enter your name.")

    while True:
        try:
            bid = int(input("What is your bid? "))
            break
        except:
            print("Please enter a numeric bid.")

    while True:
        more_bids = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        if len(more_bids) == 0 or more_bids not in ['yes', 'no']:
            continue

        more_bids = False if more_bids == "no" else True
        clearConsole()
        break

    return bidder, bid, more_bids

def blind_auction():
    bids = {}
    finished = False

    print(logo)
    print("Welcome to our blind auction! Please enter your bid!\n"
          "Keep in mind the first highest bid (in case of a tie) will be declared the winner.\n")

    while not finished:
        bidder, bid, more_bids = retrieve_bid()
        bids[bidder] = bid
        if not more_bids:
            finished = True

    winner = max(bids, key=bids.get)
    max_bid = "{:,}".format(bids[winner])
    print(f'RESULTS:\nThe winner is {winner.capitalize()} with a bid of ${max_bid}!\n')

if __name__ == "__main__":
    blind_auction()