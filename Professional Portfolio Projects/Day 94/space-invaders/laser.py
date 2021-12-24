from turtle import Turtle

ALIEN_LASER_DISTANCE = 15
CANNON_LASER_DISTANCE = 30


class Laser(Turtle):
    def __init__(self, position, turtle):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.2, stretch_len=0.75)
        self.penup()
        self.type = turtle

        if turtle == 'alien':
            self.setheading(270)
            self.color("white")
            self.set_starting_position(position)
        else:
            self.setheading(90)
            self.color("red")
            self.set_starting_position(position)

    def set_starting_position(self, position):
        x, y = position
        if self.type == 'alien':
            self.goto((x, y - 20 ))
        else:
            self.goto((x, y + 20))

    def move(self):
        if self.type == 'alien':
            self.forward(ALIEN_LASER_DISTANCE)
        else:
            self.forward(CANNON_LASER_DISTANCE)
