from turtle import Turtle, register_shape
from laser import Laser
import random

X_POSITIONS = [x for x in range(-250, 251, 50)]
Y_POSITIONS = [y for y in range(250, 351, 50)]
LEVEL_SHIFT = 10
ALIEN_GIF = "turtle-gifs/alien.gif"


class Alien(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape(ALIEN_GIF)
        self.penup()
        self.goto(position)

    def move(self, direction, speed):
        if direction == 'R':
            self.forward(speed)
        else:
            self.backward(speed)


class AlienManager:
    def __init__(self):
        register_shape(ALIEN_GIF)
        self.aliens = []
        for y in Y_POSITIONS:
            for x in X_POSITIONS:
                position = (x, y)
                self.aliens.append(Alien(position))
        self.direction = "R"
        self.alien_speed = 5
        self.lasers = []

    def remove_alien(self, alien):
        alien.hideturtle()
        self.aliens.pop(self.aliens.index(alien))

    def switch_direction(self):
        self.direction = "L" if self.direction == "R" else "R"

    def move_aliens(self):
        for alien in self.aliens:
            alien.move(self.direction, self.alien_speed)
        self.check_for_wall()

    def check_for_wall(self):
        alien_xcors = [alien.xcor() for alien in self.aliens]
        max_xcor = max(alien_xcors)
        min_xcor = min(alien_xcors)

        if max_xcor > 350 or min_xcor < -350:
            self.switch_direction()
            self.lower_aliens()

    def lower_aliens(self):
        for alien in self.aliens:
            alien.sety(alien.ycor() - LEVEL_SHIFT)

    def increase_speed(self):
        self.alien_speed *= 1.02

    def fire_lasers(self):
        for alien in self.aliens:
            if not random.randint(0, 100):
                self.lasers.append(Laser(alien.position(), 'alien'))

    def remove_laser(self, laser):
        laser.hideturtle()
        self.lasers.pop(self.lasers.index(laser))

