from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
Y_BOUNDS = (0, 250)
Y_POSITIONS = [y for y in range(-250, 251, 40)]
X_START = 310
WEST = 180


class Block(Turtle):
    """
    Models the block
    """
    def __init__(self, color, position):
        """
        inherits from Turtle class and creates a block object
        """
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2)
        self.color(color)
        self.penup()
        self.goto(position)
        # self.setheading(WEST)


class BlockManager:
    """
    Models the Block Manager
    """
    def __init__(self):
        """
        initializes an empty blocks list
        """
        self.blocks = []
        for i in range(len(COLORS)):
            color = COLORS[i]
            y = 25 + 30 * i
            for j in range(15):
                x = -350 + j * 50
                position = (x, y)
                self.blocks.append(Block(color, position))

    def remove_block(self, block):
        """
        removes Car Object from cars list
        :param car: Car Object
        """
        block.hideturtle()
        block.goto(-500, 0)

    def move_cars(self):
        """
        moves the cars in car list and calls remove_car for any cars that have surpassed the left bounds
        """
        for car in self.cars:
            car.move(self.car_speed)
            if car.xcor() < -400:
                self.remove_car(car)

    def increase_speed(self):
        """
        increases the car_speed once a level is cleared
        """
        self.car_speed += MOVE_INCREMENT
