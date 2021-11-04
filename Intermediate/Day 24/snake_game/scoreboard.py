from turtle import Turtle
import csv

ALIGNMENT = "center"
FONT = ("Courier", 20, 'normal')


class Scoreboard(Turtle):
    """
    Models the scoreboard used to keep track of the score
    """
    def __init__(self, mode):
        """
        Inherits from superclass Turtle and initializes scoreboard display to 0
        """
        super().__init__()
        self.score = 0
        self.mode = mode
        self.high_scores = self.load_current_high_score()
        self.high_score = int(self.high_scores[self.mode])
        self.hideturtle()
        self.sety(270)
        self.color("white")
        self.display_scoreboard()

    @staticmethod
    def load_current_high_score():
        """
        reads data.txt file and returns high scores
        :return: list of high scores
        """
        with open("data.txt", mode="r") as file:
            csv_reader = csv.DictReader(file)
            return csv_reader.__next__()

    def update_high_score_file(self):
        with open("data.txt", mode="w") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=list(self.high_scores.keys()))
            writer.writeheader()
            writer.writerow(self.high_scores)

    def display_scoreboard(self):
        """
        displays scoreboard
        """
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def restart(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.high_scores[self.mode] = self.high_score
            self.update_high_score_file()
        self.score = 0
        self.display_scoreboard()

    def update_score(self):
        """
        updates scoreboard
        """
        self.score += 1
        self.display_scoreboard()
