from turtle import Turtle

font = ("Courier", 14, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.score = 0
        self.score_updater()

    def add_score(self):
        self.score += 1
        self.score_updater()

    def score_updater(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=font)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=font)
