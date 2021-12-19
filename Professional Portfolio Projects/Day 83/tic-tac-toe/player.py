class Player:
    def __init__(self, num):
        self.turn = num + 1
        self.marks = {
            1: 'X',
            2: 'O'
        }

    def take_turn(self):
        print(f"TURN: PLAYER {self.turn}")
        while True:
            try:
                row = int(input("Enter the row (1-3): "))
                column = int(input("Enter the column (1-3): "))
                if row < 1 or row > 3 or column < 1 or column > 3:
                    print("Please enter a number between 1 and 3.\n")
                    continue
                break
            except ValueError:
                print("Please enter a number between 1 and 3.\n")
        return row, column, self.marks[self.turn]