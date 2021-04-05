from turtle import Turtle
import turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        # screen
        self.height = 100
        self.width = 20
        self.right_x_pos = 350
        self.right_y_pos = 0
        self.left_x_pos = -350
        self.left_y_pos = 0
        # self.paddle = Turtle()

    def create_paddle(self, position):
        print(position)
        print('here')
        self.shape('square')
        self.color('white')
        # default height and width is 20,20 , so wi
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        if position == 'right':
            self.setpos(self.right_x_pos, self.right_y_pos)
        elif position == 'left':
            self.setpos(self.left_x_pos, self.left_y_pos)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
