import math

import turtle


t = turtle.Turtle()
t.speed(0)
def draw_fract_serp(x, y, length, depth):
    if (depth > 0):
        draw_fract_serp(x, y, length / 2, depth - 1)
        draw_fract_serp(x + length / 2, y , length / 2, depth - 1)
        draw_fract_serp(x + length / 4, y + math.sqrt((length/2)**2 - (length/4)**2), length / 2, depth - 1)
    else:
        t.up()
        t.goto(x, y)
        t.down()
        for i in range(0, 3):
            t.forward(length)
            t.left(120)


draw_fract_serp(-300, -300, 600, 5)
s = turtle.Screen()
