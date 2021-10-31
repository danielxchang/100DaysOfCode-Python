from random import randint

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

def determine_result(player, computer):
    if player == computer:
        result = "Draw!"
    else:
        if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
            result = "You win!"
        else:
            result = "You lose!"

    return result

def get_player_choice():
    while True:
        try:
            player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
            if 0 <= player_choice <= 2:
                break
            else:
                print("Number entered not between 0, 1, or 2\n")
        except:
            print("Please enter a number between 0, 1, or 2\n")

    return player_choice

if __name__ == '__main__':
    player_choice = get_player_choice()
    comp_choice = randint(0, 2)
    print(choices[player_choice])
    print("Computer chose:\n" + choices[comp_choice])
    print(determine_result(player_choice, comp_choice))