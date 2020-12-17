from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0

    def update_score(self):
        self.score += 1
        updated_score = f"Score : {self.score}"
        self.clear()
        self.write(updated_score, move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.color("yellow")
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
