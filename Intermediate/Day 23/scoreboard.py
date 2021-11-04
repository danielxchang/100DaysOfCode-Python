from turtle import Turtle

FONT = ("Courier", 24, "normal")
POSITION = (-280, 260)


class Scoreboard(Turtle):
    """
    models the scoreboard
    """
    def __init__(self):
        """
        inherits from Turtle class and initializes the scoreboard
        """
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(POSITION)
        self.display_level()

    def display_level(self):
        """
        writes the scoreboard onto the top left of the screen
        """
        self.write(f"Level: {self.level}", align='left', font=FONT)

    def update_level(self):
        """
        Updates the scoreboard to display the next level
        """
        self.clear()
        self.level += 1
        self.display_level()

    def game_over(self):
        """
        writes the game over message to player
        """
        self.home()
        self.write("GAME OVER", align='center', font=FONT)
