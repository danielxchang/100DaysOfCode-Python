from turtle import Turtle, Screen
import random

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']


def create_racers():
    turtle_racers = []
    for idx in range(len(colors)):
        t = Turtle(shape='turtle')
        t.penup()
        t.color(colors[idx])
        t.goto(x=-230, y=(-120 + (idx * 50)))
        turtle_racers.append(t)
    return turtle_racers


def move_turtles(racers):
    for racer in racers:
        if racer.xcor() >= 230:
            return racer.pencolor()
        rand_distance = random.randint(0, 10)
        racer.forward(rand_distance)


def turtle_race():
    screen = Screen()
    screen.setup(width=500, height=400)
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
    turtle_racers = create_racers()

    is_race_on = False
    if user_bet in colors:
        is_race_on = True

    while is_race_on:
        if winner := move_turtles(turtle_racers):
            is_race_on = False
            print(f"You {'won!' if user_bet == winner else 'lost.'} The {winner} turtle finished first!")

    screen.bye()


if __name__ == "__main__":
    turtle_race()
