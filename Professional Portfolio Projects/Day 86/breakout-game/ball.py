from turtle import Turtle
import random

MOVEMENT_DISTANCE = 15
QUADRANTS = {
    "I": 45,
    "II": 135,
    "III": 225,
    "IV": -45
}
DEFAULT_SPEED = 0.1
SPEED_INCREASE = 1.005
START_POSITION = (0, -255)


class Ball(Turtle):
    """
    models the ball
    """
    def __init__(self):
        super().__init__()
        self.side = -1
        self.shape("circle")
        self.color("DeepPink")
        self.penup()
        self.goto(START_POSITION)
        self.setheading(self.random_angle())
        self.move_speed = MOVEMENT_DISTANCE

    def move(self):
        """
        moves the ball forward
        """
        self.forward(self.move_speed)

    def bounce(self, obj):
        """
        changes the exit angle of the ball after a bounce
        :param obj: string representing object being bounced off of
        """
        angle = self.heading() % 360
        new_angle = 45
        if obj == 'top':
            if 0 < angle <= 90:
                new_angle = QUADRANTS['IV']
            elif 90 < angle <= 180:
                new_angle = QUADRANTS['III']
        elif obj == 'side':
            if 0 < angle <= 90:
                new_angle = QUADRANTS['II']
            elif 90 < angle <= 180:
                new_angle = QUADRANTS['I']
            elif 180 < angle < 270:
                new_angle = QUADRANTS['IV']
            else:
                new_angle = QUADRANTS['III']
        elif obj == 'block':
            if 0 < angle <= 90:
                new_angle = QUADRANTS['IV']
            elif 90 < angle <= 180:
                new_angle = QUADRANTS['III']
            elif 180 < angle < 270:
                new_angle = QUADRANTS['II']
            else:
                new_angle = QUADRANTS['I']
            self.move_speed *= SPEED_INCREASE
        else:
            if 180 < angle < 270:
                new_angle = QUADRANTS['II']
            else:
                new_angle = QUADRANTS['I']
        self.setheading(new_angle)

    def random_angle(self):
        """
        obtains a random angle
        :return: int random angle
        """
        return random.randint(45, 135)

    def refresh(self):
        """
        refreshes the ball back to the center after one round ends, resets move_speed,
        and sends ball to other side
        """
        self.goto(START_POSITION)
        self.setheading(self.random_angle())
        self.move_speed = DEFAULT_SPEED
