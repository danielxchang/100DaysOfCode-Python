from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from turtle import Screen
from block_manager import BlockManager
import time


def breakout():
    """
    starts the breakout game
    """
    # Set up screen
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Breakout")
    screen.tracer(0)


    # Instantiate paddle, ball and scoreboard
    paddle = Paddle((0, -275))
    ball = Ball()
    scoreboard = Scoreboard()
    block_manager = BlockManager()

    # Set up paddle key listeners
    screen.listen()
    screen.onkey(paddle.go_right, "Right")
    screen.onkey(paddle.go_left, "Left")

    # Core game logic
    is_game_on = True
    while is_game_on:
        time.sleep(0.1)
        screen.update()
        ball.move()

        # Detect collision with top wall
        if ball.ycor() >= 285:
            ball.bounce("top")

        # Detect collision with side wall
        if ball.xcor() >= 385 or ball.xcor() <= -385:
            ball.bounce("side")

        # Detect collision with paddle
        if ball.ycor() <= -255 and paddle.distance(ball) <= 50:
            ball.bounce("paddle")

        # Detect collision with block
        for block in block_manager.blocks:
            if abs(block.ycor() - ball.ycor()) < 15 and abs(block.xcor() - ball.xcor()) < 25:
                block_manager.remove_block(block)
                ball.bounce("block")
                scoreboard.update_score()
                if scoreboard.score == len(block_manager.blocks):
                    scoreboard.cleared()
                    is_game_on = False
                    break

        # End game if balls slips past paddle
        if ball.ycor() < -310:
            is_game_on = False
            scoreboard.game_over()

    screen.exitonclick()


if __name__ == "__main__":
    breakout()
