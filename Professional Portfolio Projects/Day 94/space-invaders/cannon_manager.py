from turtle import Turtle, register_shape
from laser import Laser

STARTING_POSITION = (0, -275)
DIRECTIONS = {
    "east": 0,
    "north": 90,
    "west": 180,
    "south": 270
}
SHIP_GIF = "turtle-gifs/ship.gif"
LIVES = 3


class Cannon(Turtle):
    def __init__(self, position):
        super().__init__()
        register_shape(SHIP_GIF)
        self.create_cannon(position)
        self.laser = None

    def create_cannon(self, position):
        self.shape(SHIP_GIF)
        self.penup()
        self.color("green")
        self.goto(position)

    def go_right(self):
        if self.xcor() <= 330:
            self.forward(30)

    def go_left(self):
        if self.xcor() >= -330:
            self.backward(30)

    def fire_laser(self):
        if not self.laser:
            self.laser = Laser(self.position(), 'cannon')

    def remove_laser(self):
        self.laser.hideturtle()
        self.laser = None


class CannonManager:
    def __init__(self):
        self.cannons = [Cannon((-350 + i * 50, -350)) for i in range(3)]

    @staticmethod
    def set_active_cannon(cannon):
        cannon.goto(STARTING_POSITION)
