from turtle import Turtle, Screen

from random import random
timmy = Turtle()
timmy.shape('turtle')
screen = Screen()


def change_color():
    R = random()
    B = random()
    G = random()
    timmy.color(R, G, B)


for num_of_sides in range(3, 11):
    change_color()
    for i in range(1, num_of_sides+1):
        timmy.color()
        angle = (360/num_of_sides)
        timmy.forward(100)
        timmy.right(angle)

screen.exitonclick()
