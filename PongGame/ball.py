from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.width = 20
        self.height = 20
        self.color('white')
        self.shape('circle')
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        self.penup()
        # self.speed('slowest')
        x_pos = self.xcor() + self.x_move
        y_pos = self.ycor() + self.y_move
        self.goto(x_pos, y_pos)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.penup()
        self.speed('fastest')
        self.goto(0, 0)
        self.bounce_x()
        self.move()
