from turtle import Turtle

X_POSITIONS = [x for x in range(-300, 301, 100)]
Y_POSITIONS = [y for y in range(-200, 1, 45)]


class Bunker(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('green')
        self.shapesize(stretch_wid=2, stretch_len=0.3)
        self.penup()
        self.goto(position)


class BunkerManager:
    def __init__(self):
        self.bunkers = []
        for y in Y_POSITIONS:
            for x in X_POSITIONS:
                for num in range(0, 51, 10):
                    position = (x + num, y)
                    self.bunkers.append(Bunker(position))

    def remove_bunker(self, bunker):
        bunker.hideturtle()
        self.bunkers.pop(self.bunkers.index(bunker))

