from turtle import Turtle, Screen


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.back(10)


def move_counter_clockwise():
    tim.left(10)


def move_clockwise():
    tim.right(10)


def clear_screen():
    tim.reset()


actions = {
    "w": move_forwards,
    "s": move_backwards,
    "a": move_counter_clockwise,
    "d": move_clockwise,
    "c": clear_screen
}


def etch_a_sketch():
    global tim
    tim = Turtle()
    tim.speed("fastest")
    screen = Screen()
    screen.listen()

    for trigger, fn in actions.items():
        screen.onkey(key=trigger, fun=fn)

    screen.exitonclick()


if __name__ == "__main__":
    etch_a_sketch()