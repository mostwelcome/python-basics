from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
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

food = Food()
scoreboard = Scoreboard()
is_game_on = True
score = 0
scoreboard.write_score(score)
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision of food and snake
    if snake.head.distance(food) < 20:
        food.refresh()
        score += 1
        scoreboard.write_score(score)
        snake.extend()

    # detect collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.game_over_scoreboard()

    # detect collision with its own tail
    # if head collides with any segement with the tails
    for segment in snake.list_segment[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over_scoreboard()

screen.exitonclick()
