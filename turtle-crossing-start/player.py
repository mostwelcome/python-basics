from turtle import Turtle
import turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.shape('turtle')
        self.color('blue')

    def move(self):
        x_pos = self.xcor()
        y_pos = self.ycor()
        self.penup()
        self.setpos(x_pos, y_pos+MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def go_to_start(self):
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
