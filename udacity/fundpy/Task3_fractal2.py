import math
import time
import turtle


time.sleep(3)
t = turtle.Turtle()
t.speed(0)
def draw_first_triang(x, y, length):
    t.up()
    t.goto(x, y)
    t.down()
    for i in range(0, 3):
        t.forward(length)
        t.left(120)

def draw_second_triang(x, y, length):
    t.up()
    t.goto(x, y)
    t.down()
    for i in range(0, 3):
        t.forward(length)
        t.right(120)


def draw_lines(x, y, length, depth):
    if (depth > 0):
        draw_second_triang(x + length / 4, y + math.sqrt((length/2)**2 - (length/4)**2), length/2)
        draw_lines(x, y, length /2, depth - 1)
        draw_lines(x + length / 2, y, length /2, depth - 1)
        draw_lines(x + length / 4, y + math.sqrt((length/2)**2 - (length/4)**2), length / 2, depth - 1)





draw_first_triang(-300, -300, 600)
draw_lines(-300, -300, 600, 5)
s = turtle.Screen()
s.onclick(draw_first_triang)
s.exitonclick()