from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(20)


screen.listen()
# when we pass a function we are passing the function without () , only name
screen.onkey(key='space', fun=move_forward)

screen.exitonclick()
