class Board:
    def __init__(self):
        self.matrix = [-1 for _ in range(9)]

    def print_board(self):
        for i, cell in enumerate(self.matrix):
            if i in [2, 5]:
                print(f'{cell if cell != -1 else " "}', end="")
                print(f'\n{"-" * 10}')
            elif i == 8:
                print(f'{cell if cell != -1 else " "}', end="")
            else:
                print(f'{cell if cell != -1 else " "} | ', end="")
        print('\n')

    def check_choice(self, row, column):
        cell_idx = 3 * row - (3 - column) - 1
        if self.matrix[cell_idx] == -1:
            return cell_idx
        else:
            return -1

    def update_board(self, row, column, mark):
        cell_idx = self.check_choice(row, column)
        self.matrix[cell_idx] = mark
        return self.is_winner(mark)

    def is_draw(self):
        return -1 not in self.matrix

    def is_winner(self, mark):
        winning_idx_combos = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]
        for combo in winning_idx_combos:
            combo_set = [self.matrix[idx] for idx in combo]
            if combo_set.count(mark) == 3:
                return True
        return False
