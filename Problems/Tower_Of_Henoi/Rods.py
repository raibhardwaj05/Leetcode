from turtle import Turtle

class Rod(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.hideturtle()
        self.penup()
        self.pensize(10)
        self.color("white")
        self.x_cord = -250
        self.y_cord = -200
        self.move = 0

    def create(self):
        for i in range(1, 4):
            self.goto(self.x_cord + self.move, self.y_cord)
            self.pendown()
            self.goto(self.xcor(), self.ycor() + 350)
            self.penup()
            self.move += 250

        self.goto(-300, -200)
        self.pendown()
        self.goto(300, -200)
      
