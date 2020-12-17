from turtle import Turtle
import random

FOOD_COLOR = "#16a596"


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(FOOD_COLOR)
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    # refreshes food location
    def refresh(self):
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.goto(random_x, random_y)
