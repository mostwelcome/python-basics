from turtle import Turtle, penup

ALLIGNMENT_LEFT = 'center'
ALLIGNMENT_RIGHT = 'center'
FONT = ('Arial', 80, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        self.left_score = 0
        self.right_score = 0
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.speed('fastest')
        self.goto(-180, 180)
        self.write(f'{self.left_score}', True,
                   align=ALLIGNMENT_LEFT, font=FONT)
        self.goto(180, 180)
        self.write(f'{self.right_score}', True,
                   align=ALLIGNMENT_LEFT, font=FONT)

    def left_scoreboard(self):
        self.left_score += 1
        self.update_scoreboard()

    def right_scoreboard(self):
        self.right_score += 1
        self.update_scoreboard()
