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
SPEED_INCREASE = 0.75


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
        self.setheading(self.random_angle())
        self.move_speed = DEFAULT_SPEED

    def move(self):
        """
        moves the ball forward
        """
        self.forward(MOVEMENT_DISTANCE)

    def bounce(self, obj):
        """
        changes the exit angle of the ball after a bounce and increases ball speed
        :param obj: string representing object being bounced off of
        """
        angle = self.heading() % 360
        if 0 < angle < 90:  # bounce in quadrant I
            new_angle = QUADRANTS['IV'] if obj == "wall" else QUADRANTS['II']
        elif 90 < angle < 180:  # bounce in quadrant II
            new_angle = QUADRANTS['III'] if obj == "wall" else QUADRANTS['I']
        elif 180 < angle < 270:  # bounce in quadrant III
            new_angle = QUADRANTS['II'] if obj == "wall" else QUADRANTS['IV']
        else:  # bounce in quadrant IV
            new_angle = QUADRANTS['I'] if obj == "wall" else QUADRANTS['III']
        self.setheading(new_angle)
        if obj == "paddle":
            self.move_speed *= SPEED_INCREASE

    def random_angle(self):
        """
        obtains a random angle based off which side of the game
        :return: int random angle
        """
        self.side *= -1
        if self.side == 1:
            angle = random.randint(40, 50)
        else:
            angle = random.randint(130, 140) * random.choice([1, -1])
        return angle

    def refresh(self):
        """
        refreshes the ball back to the center after one round ends, resets move_speed,
        and sends ball to other side
        """
        self.home()
        self.setheading(self.random_angle())
        self.move_speed = DEFAULT_SPEED
