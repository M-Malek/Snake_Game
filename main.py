from turtle import Screen, Turtle
from snake import Snake
import time

# Screen initialize + screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create snake from Snake class
snake = Snake()

# Listen to user controls: how to control snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main game loop
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
