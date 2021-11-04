import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def turtle_crossing():
    # Setup screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    # Instantiate class objects
    player = Player()
    car_manager = CarManager()
    scoreboard = Scoreboard()

    # Set up key listener
    screen.listen()
    screen.onkey(player.move, "Up")

    # Core game logic
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        car_manager.generate_car()

        # Check for collision of player and car
        for car in car_manager.cars:
            if abs(car.ycor() - player.ycor()) < 15 and abs(car.xcor() - player.xcor()) < 25:
                game_is_on = False
                scoreboard.game_over()

        # Check for player clearing level
        if player.at_finish_line():
            player.go_to_start()
            scoreboard.update_level()
            car_manager.increase_speed()

        car_manager.move_cars()

    screen.exitonclick()


if __name__ == "__main__":
    turtle_crossing()
