from turtle import Turtle, Screen, backward

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(20)


def move_backward():
    tim.backward(20)


def move_counter_clockwise():
    tim.right(20)


def move_clockwise():
    tim.left(20)


def clear_all():
    tim.reset()


while True:
    screen.listen()
    # when we pass a function we are passing the function without () , only name
    screen.onkey(key='w', fun=move_forward)
    screen.onkey(key='s', fun=move_backward)
    screen.onkey(key='a', fun=move_counter_clockwise)
    screen.onkey(key='d', fun=move_clockwise)
    screen.onkey(key='c', fun=clear_all)
    screen.exitonclick()
