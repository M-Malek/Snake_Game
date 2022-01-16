class Snake:
    def __init__(self):
        self.start_pos = [(0, 0), (-20, 0), (-40, 0)]
        self.snake_segments = []
        self.initialize_snake()

    def initialize_snake(self):
        from turtle import Turtle
        for pos in self.start_pos:
            segment = Turtle(shape="square")
            segment.penup()
            segment.color("white")
            segment.goto(pos)
            self.snake_segments.append(segment)

    def move(self):
        from turtle import Turtle
        for seg_int in range(len(self.snake_segments) - 1, 0, -1):
            x_pos = self.snake_segments[seg_int - 1].xcor()
            y_pos = self.snake_segments[seg_int - 1].ycor()
            self.snake_segments[seg_int].goto(x_pos, y_pos)
        self.snake_segments[0].forward(20)
