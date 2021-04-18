from turtle import Turtle, penup

ALLIGNMENT = 'center'
FONT = ('Arial', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        self.highest_score =0
        super().__init__()

    def write_score(self, score):
        self.clear()
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.write(f'Score : {score}', True,
                   align=ALLIGNMENT, font=FONT)
        self.hideturtle()

    def game_over_scoreboard(self):
        self.goto(0, 0)
        self.write('Game over', True,
                   align=ALLIGNMENT, font=FONT)


    def reset(self):
        if self.score < self.highest_score:
            self.highest_score = self.score
        self.score = 0

    