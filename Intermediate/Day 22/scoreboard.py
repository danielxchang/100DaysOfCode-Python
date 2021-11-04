from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, 'normal')


class Scoreboard(Turtle):
    """
    Models the scoreboard used to keep track of the score
    """
    def __init__(self):
        """
        Inherits from superclass Turtle and initializes scoreboard display to 0
        """
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()
        self.penup()
        self.sety(200)
        self.color("white")
        self.display_scoreboard()

    def display_scoreboard(self):
        """
        displays scoreboard
        """
        self.write(f"{self.left_score} {self.right_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """
        displays game over when player loses
        """
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def update_score(self, scorer):
        """
        updates scoreboard
        """
        self.clear()
        if scorer == "left":
            self.left_score += 1
        else:
            self.right_score += 1
        self.display_scoreboard()
