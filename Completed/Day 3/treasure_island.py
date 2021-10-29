def play_game(snippets):
 snippets = list(map(lambda text: text + '\n', snippets))

 if input(snippets[0]).lower() != "left":
  return snippets[8]
 elif input(snippets[1]).lower() != "wait":
  return snippets[7]
 elif (choice := input(snippets[2]).lower()) != "yellow":
  if choice == "red":
   return snippets[3]
  elif choice == "blue":
   return snippets[5]
  else:
   return snippets[6]
 else:
  return snippets[4]

def main():
 # ASCII art from https://ascii.co.uk/art/treasureisland
 print('''
 *****************************************************************
  _                                     _     _                 _
 | |                                   (_)   | |               | |
 | |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
 | __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
 | |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
  \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
 *****************************************************************
 ''')


 print("Welcome to Treasure Island.")
 print("Your mission is to find the treasure.")

 snippets = [
  'You\'re at a crossroad. Where do you want to go? Type "left" or "right"',
  'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.',
  "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?",
  "It's a room full of fire. Game Over.",
  "You found the treasure! You Win!",
  "You enter a room of beasts. Game Over.",
  "You chose a door that doesn't exist. Game Over.",
  "You get attacked by an angry trout. Game Over.",
  "You fell into a hole. Game Over."
 ]

 print(play_game(snippets))



if __name__ == "__main__":
 main()