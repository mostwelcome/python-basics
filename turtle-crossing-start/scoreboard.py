FONT = ("Courier", 24, "normal")

from turtle import Turtle, xcor
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280,240)
        self.write(f'Level:{self.level}',align='left',font=FONT)

    def increase_level(self):
        self.level +=1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Level:{self.level}',align='left',font=FONT)

    def game_over(self):
        self.penup()
        self.goto(-90,0)
        self.write('Game Over',align='left',font=FONT)