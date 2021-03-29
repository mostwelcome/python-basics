from turtle import Turtle
from random import random
timmy = Turtle()


def change_color():
    '''This function generates the random color for the turtle'''
    R = random()
    B = random()
    G = random()
    timmy.color(R, G, B)


timmy.speed(40)


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        change_color()
        timmy.circle(50)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(5)
