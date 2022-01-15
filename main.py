import turtle
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

start_pos = [(0, 0), (-20, 0), (-40, 0)]

for pos in start_pos:
    segment = Turtle(shape="square")
    segment.color("white")
    segment.goto(pos)

screen.exitonclick()
