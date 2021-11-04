from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from turtle import Screen, Turtle
import time


def draw_center_line(num_of_dashes):
    """
    Draws center line
    :param num_of_dashes: int
    """
    mid_line = Turtle()
    mid_line.color("white")
    mid_line.penup()
    mid_line.goto(0, 300)
    mid_line.setheading(270)
    for _ in range(int(num_of_dashes/2)):
        mid_line.pendown()
        mid_line.forward(630/num_of_dashes)
        mid_line.penup()
        mid_line.forward(630/num_of_dashes)


def hit_paddle(ball, paddle):
    """
    determines if ball collides with paddle
    :param ball: Ball object
    :param paddle: Paddle object
    :return: True or False
    """
    return ball.distance(paddle) < 50 and abs(ball.xcor()) >= 325


def pong():
    """
    starts the pong game
    """
    # Set up screen
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)

    # Initialize center line
    draw_center_line(25)

    # Instantiate paddles, ball and scoreboard
    right_paddle = Paddle((350, 0))
    left_paddle = Paddle((-350, 0))
    ball = Ball()
    scoreboard = Scoreboard()

    # Set up right/left paddle key listeners
    screen.listen()
    screen.onkey(right_paddle.up, "Up")
    screen.onkey(right_paddle.down, "Down")
    screen.onkey(left_paddle.up, "w")
    screen.onkey(left_paddle.down, "s")

    # Core pong game logic
    is_game_on = True
    while is_game_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # Detect collision with wall
        if ball.ycor() >= 285 or ball.ycor() <= -280:
            ball.bounce("wall")

        # Detect collision with paddle
        if hit_paddle(ball, left_paddle) or hit_paddle(ball, right_paddle):
            ball.bounce("paddle")

        # Detect ball goes out of bounds right-side
        if ball.xcor() >= 420:
            ball.refresh()
            scoreboard.update_score('left')

        # Detect ball goes out of bounds left-side
        if ball.xcor() <= -420:
            ball.refresh()
            scoreboard.update_score('right')

        # End game if one player hits 3 points
        if scoreboard.left_score == 3 or scoreboard.right_score == 3:
            is_game_on = False
            scoreboard.game_over()

    screen.exitonclick()


if __name__ == "__main__":
    pong()
