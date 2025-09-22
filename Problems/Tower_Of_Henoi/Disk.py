import random
from turtle import Turtle

class Disc:
    def __init__(self, rod, screen):
        self.s = screen
        self.R = rod
        self.discs = int(self.s.textinput("Tower of Hanoi", "Number of Disks"))
        self.disc_height = 20
        self.disc_list = []

    def random_color(self):
        r = random.uniform(0.4, 0.9)
        g = random.uniform(0.4, 0.9)
        b = random.uniform(0.4, 0.9)
        return r, g, b

    def create_disc(self):
        for i in range(self.discs, 0, -1):
            t = Turtle("square")
            t.color(self.random_color())
            t.shapesize(stretch_len= i*1.5, stretch_wid= 1)
            t.penup()

            t.goto(self.R.rod[0].xcor(), self.R.y_cord + 15 + (self.discs - i) * self.disc_height)
            self.disc_list.append(t)
