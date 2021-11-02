# import colorgram

# img_colors = colorgram.extract('image.jpg', 30)
# colors = [(clr.rgb.r, clr.rgb.g, clr.rgb.b) for clr in img_colors]
# print(colors)

import turtle as t
import random

color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40),
              (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148),
              (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171),
              (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100),
              (107, 127, 153), (174, 94, 97), (176, 192, 209)]


def select_color():
    return random.choice(color_list)


# 10 x 10 dots - 20 in size spaced 50
def create_painting(turtle, dot_size, gap, offset):
    turtle.penup()
    turtle.hideturtle()
    for y in range(10):
        for x in range(10):
            position = (x * gap - offset, y * gap - offset)
            turtle.setpos(position)
            turtle.dot(dot_size, select_color())
            turtle.forward(gap)


def hirst_dots():
    tim = t.Turtle()
    t.colormode(255)
    tim.speed("fastest")
    create_painting(tim, dot_size=20, gap=50, offset=250)
    screen = t.Screen()
    screen.exitonclick()


if __name__ == "__main__":
    hirst_dots()
