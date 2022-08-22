import colorgram
import random
from turtle import Turtle, Screen

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_col = (r, g, b)
    rgb_colors.append(new_col)
tim = Turtle()
s = Screen()
s.colormode(255)
tim.up()
tim.goto(-300, -300)
tup = random.choice(rgb_colors)
for i in range(0, 10):
    for _ in range(0, 10):
        tup = random.choice(rgb_colors)
        tim.dot(20, tuple(tup))
        tim.forward(60)
    if i % 2 == 0:
        tim.left(90)
        tim.forward(60)
        tim.left(90)
        tim.forward(60)
    else:
        tim.right(90)
        tim.forward(60)
        tim.right(90)
        tim.forward(60)

s.exitonclick()

# print(rgb_colors)

# #rgb_colors = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
#               (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
#               (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
#               (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129),
#               (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
