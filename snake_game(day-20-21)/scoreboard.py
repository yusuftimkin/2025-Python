from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.score_write()

    def score_write(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 12, "normal"))
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 20, "normal") )

        
