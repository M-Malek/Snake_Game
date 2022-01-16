from turtle import Turtle


class Snake:
    # Initialize snake class
    def __init__(self):
        self.START_POS = [(0, 0), (-20, 0), (-40, 0)]
        self.MOVE_VALUE = 20
        self.snake_segments = []
        self.initialize_snake()

    # Set snake on board
    def initialize_snake(self):
        for pos in self.START_POS:
            segment = Turtle(shape="square")
            segment.penup()
            segment.color("white")
            segment.goto(pos)
            self.snake_segments.append(segment)

    # Let snake move forward (note: this method is responsible only for moving snake by MOVE_VALUE, not for snake
    # direction)
    def move(self):
        for seg_int in range(len(self.snake_segments) - 1, 0, -1):
            x_pos = self.snake_segments[seg_int - 1].xcor()
            y_pos = self.snake_segments[seg_int - 1].ycor()
            self.snake_segments[seg_int].goto(x_pos, y_pos)
        self.snake_segments[0].forward(self.MOVE_VALUE)

    # Method responsible for prevent instant change of snake direction
    def prevent_instant_change(self):
        pass

    # Methods responsible for changing snake direction
    def up(self):
        head = self.snake_segments[0]
        head.setheading(90)

    def down(self):
        head = self.snake_segments[0]
        head.setheading(270)

    def left(self):
        head = self.snake_segments[0]
        head.setheading(180)

    def right(self):
        head = self.snake_segments[0]
        head.setheading(0)
