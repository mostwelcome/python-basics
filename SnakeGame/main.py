from turtle import Screen, Turtle
from snake import Snake
from food import Food
import random
import turtle
import time
screen = Screen()


class swag:
    def __init__(self):
        pass


screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
list_segment = []
screen.title('Welcome to snake game')

snake = Snake()
screen.update()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

ob = Food()
is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()
