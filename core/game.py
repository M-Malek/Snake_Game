from turtle import Screen
from core.snake import Snake
from core.food import Food
from core.scoreboard import Score
import time


def main_game():
    # Screen initialize + screen setup
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    # Create snake from Snake class
    snake = Snake()
    food = Food()
    score = Score()

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

        # Food collision:
        if snake.SNAKE_HEAD.distance(food) < 15:
            food.new_food()
            score.add_score()
            snake.extend_snake()
            # print(score.score)

        # Wall collision:
        if snake.SNAKE_HEAD.xcor() >= 290 or snake.SNAKE_HEAD.xcor() <= -290 or snake.SNAKE_HEAD.ycor() >= 290 or \
                snake.SNAKE_HEAD.ycor() <= -290:
            is_game_on = False
            score.game_over()

        # Snake collision:
        for segment in snake.snake_segments[1:]:
            if snake.SNAKE_HEAD.distance(segment) < 10:
                is_game_on = False
                score.game_over()

    screen.exitonclick()
