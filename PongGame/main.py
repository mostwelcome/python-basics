from turtle import Screen, Turtle

from paddle import Paddle
from ball import Ball
from score_board import Scoreboard
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

paddle_right = Paddle()

paddle_right.create_paddle('right')

paddle_left = Paddle()
paddle_left.create_paddle('left')

screen.listen()
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")

screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")

score_left = 0
score_right = 0

scoreboard = Scoreboard()


ball = Ball()
game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    screen.tracer(True)
    # ball.speed('slowest')
    ball.move()

    # detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # need to bounce the ball
        ball.bounce_y()

    # detect collision with the paddle
    if ball.distance(paddle_right) < 70 and ball.xcor() > 330:
        ball.bounce_x()
        ball.ball_speed *= 0.9

    if ball.distance(paddle_left) < 70 and ball.xcor() < -330:
        ball.bounce_x()
        ball.ball_speed *= 0.9

    # if paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_scoreboard()

    if ball.xcor() < -380:
        ball.reset_position()
        ball.ball_speed = 0.1
        scoreboard.right_scoreboard()

screen.exitonclick()
