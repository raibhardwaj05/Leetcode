from turtle import Screen
from Rods import Rod
from Disk import Disc

s = Screen()
s.setup(800, 600)
s.bgcolor("Black")
s.colormode(1)
s.tracer(0)

R = Rod()
R.create()
R.label()

disc = Disc(R, s)
disc.create_disc()

s.update()
s.exitonclick()
