from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
DIRECTIONS = {
    "east": 0,
    "north": 90,
    "west": 180,
    "south": 270
}


class Snake:
    """
    Models the snake in the snake game
    """
    def __init__(self):
        """
        initializes empty list for the snake segments and calls create_snake method
        """
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def create_snake(self):
        """
        creates snake segments and appends to snake list
        """
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """
        creates snake segment
        :return: snake segment object
        """
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """
        extends snake by creating new segment and attaching to tail of snake
        """
        self.add_segment(self.segments[-1].position())

    def move(self):
        """
        moves the snake segments forward
        """
        for i in range(1, len(self.segments)):  # Iterates through non-head segments & moves to position of next segment
            next_segment_pos = self.segments[-(i + 1)].position()
            self.segments[-i].goto(next_segment_pos)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """
        orients head north/up as long as not positioned facing south
        """
        if self.head.heading() != DIRECTIONS['south']:
            self.head.setheading(DIRECTIONS['north'])

    def down(self):
        """
        orients head south/down as long as not positioned facing north
        """
        if self.head.heading() != DIRECTIONS['north']:
            self.head.setheading(DIRECTIONS['south'])

    def right(self):
        """
        orients head east/right as long as not positioned facing west
        """
        if self.head.heading() != DIRECTIONS['west']:
            self.head.setheading(DIRECTIONS['east'])

    def left(self):
        """
        orients head west/left as long as not positioned facing east
        """
        if self.head.heading() != DIRECTIONS['east']:
            self.head.setheading(DIRECTIONS['west'])
