from turtle import Turtle
from random import random, choice
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

directions = [0, 90, 180, 270]


def change_color():
    '''This function generates the random color for the turtle'''
    R = random()
    B = random()
    G = random()
    timmy.color(R, G, B)


timmy.speed(10)
# spreed up
timmy.pensize(10)
# increase pen width
timmy.shape('turtle')
for _ in range(200):
    change_color()
    timmy.forward(30)
    timmy.setheading(choice(directions))


screen.exitonclick()
