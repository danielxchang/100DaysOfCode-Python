from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


def select_mode(screen):
    choices = ['easy', 'medium', 'hard', 'insane']
    choice = screen.textinput("Welcome to the Snake Game!",
                              "Select the difficulty level: easy/medium/hard/insane").lower()
    return choice if choice in choices else "medium"


def set_speed(choice):
    if choice == "easy":
        speed = 0.15
    elif choice == "hard":
        speed = 0.075
    elif choice == "insane":
        speed = 0.05
    else:  # Defaults to medium
        speed = 0.1
    return speed


def snake_game():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    mode = select_mode(screen)
    refresh = set_speed(mode)

    screen.tracer(0)
    screen.listen()

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard(mode)

    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(refresh)

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            scoreboard.update_score()
            snake.extend()

        # Detect collision with wall
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 \
                or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            scoreboard.restart()
            snake.reset_snake()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.restart()
                snake.reset_snake()

        snake.move()


if __name__ == "__main__":
    snake_game()
