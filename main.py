import turtle
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

for snake in range(0, 2):
    new_snake = Turtle()
    new_snake.shape("square")
    new_snake.setx(snake*10)

screen.exitonclick()
