from cannon_manager import CannonManager
from alien_manager import AlienManager
from bunker_manager import BunkerManager
from scoreboard import Scoreboard
from turtle import Screen, Turtle
import time


def set_key_listeners(screen, cannon):
    screen.listen()
    screen.onkey(cannon.go_right, "Right")
    screen.onkey(cannon.go_left, "Left")
    screen.onkey(cannon.fire_laser, "space")


def space_invaders():
    # Set up screen
    screen = Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("black")
    screen.title("Space Invaders")
    screen.tracer(0)

    # Instantiate game elements
    cannon_manager = CannonManager()
    alien_manager = AlienManager()
    bunker_manager = BunkerManager()
    scoreboard = Scoreboard()
    footer = Turtle("square")
    footer.shapesize(stretch_len=40, stretch_wid=0.05)
    footer.penup()
    footer.color("white")
    footer.goto((0, -305))

    # Set up cannon key listeners and active cannon
    cannon = cannon_manager.cannons.pop()
    set_key_listeners(screen, cannon)
    cannon_manager.set_active_cannon(cannon)

    is_game_on = True
    while is_game_on:
        time.sleep(0.1)
        screen.update()
        alien_manager.move_aliens()
        alien_manager.fire_lasers()

        for laser in alien_manager.lasers:
            laser.move()

        if cannon.laser:
            cannon.laser.move()

            if cannon.laser.ycor() > 400:
                cannon.remove_laser()
            else:
                for bunker in bunker_manager.bunkers:
                    if abs(bunker.ycor() - cannon.laser.ycor()) <= 10 and abs(bunker.xcor() - cannon.laser.xcor()) < 7:
                        bunker_manager.remove_bunker(bunker)
                        cannon.remove_laser()
                        break

        # Detect alien collisions with bunkers
        for alien in alien_manager.aliens:
            for bunker in bunker_manager.bunkers:
                if abs(bunker.ycor() - alien.ycor()) < 27 and abs(bunker.xcor() - alien.xcor()) < 7:
                    bunker_manager.remove_bunker(bunker)
                    break

        # Detect collisions with alien
        for alien in alien_manager.aliens:
            if alien.ycor() <= -235:
                cannon.hideturtle()
                for cannon in cannon_manager.cannons:
                    cannon.hideturtle()
                screen.tracer(1)
                scoreboard.ending_message('l')
                is_game_on = False
                break
            if not cannon.laser:
                break
            if abs(alien.ycor() - cannon.laser.ycor()) < 15 and abs(alien.xcor() - cannon.laser.xcor()) < 15:
                alien_manager.remove_alien(alien)
                cannon.remove_laser()
                alien_manager.increase_speed()
                scoreboard.update_score()
                if len(alien_manager.aliens) == 0:
                    screen.tracer(1)
                    scoreboard.ending_message('w')
                    is_game_on = False
                break

        # Detect collisions with alien laser
        for laser in alien_manager.lasers:
            if laser.ycor() < -300:
                alien_manager.remove_laser(laser)

            if abs(laser.ycor() - cannon.ycor()) < 25 and abs(laser.xcor() - cannon.xcor()) < 20:
                alien_manager.remove_laser(laser)
                if cannon.laser:
                    cannon.remove_laser()
                cannon.hideturtle()
                if len(cannon_manager.cannons) == 0:
                    screen.tracer(1)
                    scoreboard.ending_message('l')
                    is_game_on = False
                    break
                else:
                    screen.tracer(1)
                    cannon = cannon_manager.cannons.pop()
                    set_key_listeners(screen, cannon)
                    cannon_manager.set_active_cannon(cannon)
                    screen.tracer(0)
                    break

            if cannon.laser:
                if abs(laser.ycor() - cannon.laser.ycor()) < 10 and abs(laser.xcor() - cannon.laser.xcor()) < 15:
                    alien_manager.remove_laser(laser)
                    cannon.remove_laser()
                    break

            for bunker in bunker_manager.bunkers:
                if abs(bunker.ycor() - laser.ycor()) < 25 and abs(bunker.xcor() - laser.xcor()) < 7:
                    bunker_manager.remove_bunker(bunker)
                    alien_manager.remove_laser(laser)
                    break

    screen.exitonclick()


if __name__ == "__main__":
    space_invaders()
