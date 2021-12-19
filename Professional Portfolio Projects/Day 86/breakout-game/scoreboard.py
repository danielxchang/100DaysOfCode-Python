from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 60, 'normal')


class Scoreboard(Turtle):
    """
    Models the scoreboard used to keep track of the score
    """
    def __init__(self):
        """
        Inherits from superclass Turtle and initializes scoreboard display to 0
        """
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.sety(200)
        self.color("white")
        self.display_scoreboard()

    def display_scoreboard(self):
        """
        displays scoreboard
        """
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """
        displays game over when player loses
        """
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def cleared(self):
        """
        displays level cleared screen when all blocks are taken out
        """
        self.goto(0, 0)
        self.write("CLEARED LEVEL", align=ALIGNMENT, font=FONT)

    def update_score(self):
        """
        updates scoreboard
        """
        self.clear()
        self.score += 1
        self.display_scoreboard()
