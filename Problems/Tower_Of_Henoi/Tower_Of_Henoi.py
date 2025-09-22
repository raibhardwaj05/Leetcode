from turtle import Screen
from Rods import Rod

s = Screen()
s.setup(800, 600)
s.bgcolor("Black")
s.tracer(0)

R = Rod()
R.create()

s.update()
s.exitonclick()
