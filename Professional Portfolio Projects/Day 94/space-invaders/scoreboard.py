from turtle import Turtle

ALIGNMENT = "right"
FONT = ("Courier", 30, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(350, -360)
        self.color("white")
        self.display_scoreboard()

    def display_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def ending_message(self, result):
        self.goto(0, 0)
        message = "CONGRATULATIONS! YOU WON!" if result == "w" else "GAME OVER"
        self.write(message, align="center", font=("Courier", 40, 'normal'))

    def update_score(self):
        self.clear()
        self.score += 20
        self.display_scoreboard()
