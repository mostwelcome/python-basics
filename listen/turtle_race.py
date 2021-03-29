from turtle import Turtle, Screen
import random as rnd
screen = Screen()
screen.setup(width=500, height=400)
colors = ['red', 'blue', 'green', 'yellow', 'purple']


user_bet = screen.textinput(title="make your bet",
                            prompt="which color you want to choose?")

all_turtle = []
i = 0
diff = 0
while i < 5:
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230, y=-160+diff)
    i += 1
    diff += 80
    all_turtle.append(tim)

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for tim in all_turtle:
        if tim.xcor() > 230:
            is_race_on = False
            wining_color = tim.pencolor()
            print(wining_color)
            if wining_color == user_bet:
                print('ohooo !! you won')
            else:
                print(f'You loose,The wining color is {wining_color}')
        random_position = rnd.randint(0, 10)
        tim.forward(random_position)
screen.exitonclick()
