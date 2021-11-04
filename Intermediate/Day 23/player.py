from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
NORTH = 90


class Player(Turtle):
    """
    models the player
    """
    def __init__(self):
        """
        Inherits from Turtle class and initializes player
        """
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("turquoise")
        self.setheading(NORTH)
        self.go_to_start()

    def go_to_start(self):
        """
        positions player at STARTING_POSITION
        """
        self.goto(STARTING_POSITION)

    def move(self):
        """
        moves player MOVE_DISTANCE units
        """
        self.forward(MOVE_DISTANCE)

    def at_finish_line(self):
        return True if self.ycor() > FINISH_LINE_Y else False
