from turtle import Screen, Turtle
import turtle

timmy = Turtle()
screen = Screen()
timmy.shape('turtle')
timmy.color('red')
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)

x = 0
for i in range(7):
    x += 5
    timmy.forward(x)
    timmy.penup()
    timmy.forward(5)
    timmy.pendown()

screen.exitonclick()
