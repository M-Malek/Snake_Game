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

        self.high_score = 0
        self.load_high_score()

        self.score_updater()
        self.shut_down = False

    def add_score(self):
        self.score += 1
        self.score_updater()

    def score_updater(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align="center", font=font)

    def score_reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.score_updater()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=font)

    def save_high_score(self):
        with open("core/high_score.txt", mode="w") as file:
            file.write(str(self.high_score))

    def load_high_score(self):
        with open("core/high_score.txt") as file:
            score = file.read()
            self.high_score = int(score)
