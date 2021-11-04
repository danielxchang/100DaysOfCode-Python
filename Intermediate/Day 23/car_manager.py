from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y_BOUNDS = (-250, 250)
Y_POSITIONS = [y for y in range(-250, 251, 40)]
X_START = 310
WEST = 180


class Car(Turtle):
    """
    Models the car
    """

    def __init__(self):
        """
        inherits from Turtle class and creates a car object
        """
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(X_START, random.choice(Y_POSITIONS))
        self.setheading(WEST)

    def move(self, move_distance):
        """
        moves the car move_distance units
        :param move_distance: int
        """
        self.forward(move_distance)


class CarManager:
    """
    Models the Car Manager
    """
    def __init__(self):
        """
        initializes an empty cars list and sets car_speed to the starting distance
        """
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        """
        generates a new car and appends to cars list
        """
        if random.randint(1, 6) == 1:
            self.cars.append(Car())

    def remove_car(self, car):
        """
        removes Car Object from cars list
        :param car: Car Object
        """
        car.hideturtle()
        self.cars.pop(0)

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
