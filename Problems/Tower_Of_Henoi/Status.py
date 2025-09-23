from turtle import Turtle
from Disk import Disc

Align = "center"
Font2 = ("Arial", 15, "bold")

class Status:
    def __init__(self):
        self.num_disc = Disc.discs
        self.total_step = (2 ** self.num_disc) - 1
        self.remaining = self.total_step
        self.steps = Turtle()
        self.steps.color("green")
        self.steps.hideturtle()
        self.steps.penup()
        self.steps.goto(-450, 260)
        self.update_status()

    def update_status(self):
        self.steps.clear()
        self.steps.write(f"Steps: {self.remaining}", align= Align, font= Font2)

    def decrease(self):
        self.remaining -= 1
        self.update_status()