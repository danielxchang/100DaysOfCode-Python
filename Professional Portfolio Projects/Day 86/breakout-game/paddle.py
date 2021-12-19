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
        self.setheading(DIRECTIONS['east'])
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.goto(position)

    def go_right(self):
        """
        moves paddle right when up key is pressed
        """
        if self.xcor() <= 330:
            self.forward(30)

    def go_left(self):
        """
        moves paddle down when down key is pressed
        """
        if self.xcor() >= -330:
            self.backward(30)
