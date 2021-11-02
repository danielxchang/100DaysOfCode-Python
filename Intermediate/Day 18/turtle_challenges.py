import turtle as t
from random import randint, choice


def draw_square(turtle):
    draw_polygon(turtle, 4)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


def draw_polygon(turtle, sides):
    angle = 360 / sides
    turtle.pencolor(random_color())
    for _ in range(sides):
        turtle.forward(100)
        turtle.right(angle)


def dashed_line(turtle, dashes):
    for _ in range(dashes):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(5)
        turtle.pendown()


def random_walk(turtle, steps):
    directions = [0, 90, 180, 270]
    turtle.hideturtle()
    turtle.pensize(10)
    turtle.speed("fastest")
    for _ in range(steps):
        turtle.pencolor(random_color())
        turtle.setheading(choice(directions))
        turtle.forward(50)


def spirograph(turtle, gap):
    turtle.hideturtle()
    turtle.speed("fastest")
    count = 0
    for angle in range(0, 360, gap):
        turtle.pencolor(random_color())
        turtle.setheading(angle)
        turtle.circle(100)
        count += 1
    print(count)



tim = t.Turtle()
tim.shape('turtle')
tim.color("turquoise")
t.colormode(255)

# Challenge 1
# draw_square(tim)

# Challenge 2
# dashed_line(tim, 15)

# Challenge 3
# for sides in range(3, 11):
#     draw_polygon(tim, sides)

# Challenge 4
# random_walk(tim, 100)

# Challenge 5
spirograph(tim, 1)

screen = t.Screen()
screen.exitonclick()

