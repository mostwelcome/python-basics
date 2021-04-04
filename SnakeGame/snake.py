from turtle import Turtle, down

MOVE_SNAKE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
INITIAL_POSITION = 0


class Snake:
    def __init__(self):
        self.list_segment = []
        self.create_snake()
        self.head = self.list_segment[0]

    def create_snake(self):
        INITIAL_POSITION
        for _ in range(3):
            self.add_segment(INITIAL_POSITION)

    def extend(self):
        '''add a new segment to the snake'''
        self.add_segment(self.list_segment[-1].xcor())

    def add_segment(self, position):
        tim = Turtle()
        tim.penup()
        tim.goto(position, 0)
        tim.shape("square")
        tim.color('white')
        position -= 20
        self.list_segment.append(tim)

    def move(self):
        for seg_num in range(len(self.list_segment)-1, 0, -1):
            new_x = self.list_segment[seg_num-1].xcor()
            new_y = self.list_segment[seg_num-1].ycor()
            self.list_segment[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_SNAKE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
