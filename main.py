from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

start_pos = [(0, 0), (-20, 0), (-40, 0)]
snake_segments = []

for pos in start_pos:
    segment = Turtle(shape="square")
    segment.penup()
    segment.color("white")
    segment.goto(pos)
    snake_segments.append(segment)
    screen.update()

is_game_on = True
while is_game_on:
    for snake_seg in snake_segments:
        snake_seg.forward(10)
        screen.update()
        time.sleep(1)

screen.exitonclick()
