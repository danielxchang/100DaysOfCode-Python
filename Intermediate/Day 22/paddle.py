from turtle import Turtle

DIRECTIONS = {
    "east": 0,
    "north": 90,
    "west": 180,
    "south": 270
}


class Paddle(Turtle):
    """
    models the paddle
    """
    def __init__(self, position):
        """
        inherits from Turtle class and calls create_paddle function
        :param position: tuple of paddle position
        """
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        """
        creates paddle for side passed as parameter
        :param position: tuple of paddle position
        """
        self.shape("square")
        self.penup()
        self.setheading(DIRECTIONS['north'])
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.goto(position)

    def up(self):
        """
        moves paddle up when up key is pressed
        """
        if self.ycor() <= 250:
            self.forward(20)

    def down(self):
        """
        moves paddle down when down key is pressed
        """
        if self.ycor() >= -230:
            self.backward(20)
