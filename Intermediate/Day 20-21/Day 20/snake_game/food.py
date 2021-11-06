from turtle import Turtle
import random


class Food(Turtle):
    """
    models food snake is chasing
    """
    def __init__(self):
        """
        inherits from turtle class and initializes food object in random position
        """
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """
        Refreshes the position of food after snake eats previous one
        """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)