from turtle import Screen
from Disk import Disc
from Rods import Rod
from Autoplay import Autoplay
from Status import Status

# screen Setup
s = Screen()
s.setup(1000, 600)
s.bgcolor("Black")
s.colormode(1)
s.tracer(0)

# Rod and Disc Creation
R = Rod()
R.create()
R.label()

disc = Disc(R, s)
disc.create_disc()
status = Status()

# declare disc height, rod positions and rod stacks
disc_height = 20

rod_positions = {
    "src" : -350,
    "hlp" : 0,
    "dest" : 350
}

rods = {
    "src" : [],
    "hlp" : [],
    "dest" : []
}

# get the number of discs and append them into the source rod
num_disc = disc.discs
disc_list = disc.disc_list

for d in disc_list:
    rods["src"].append(d)

# creating object of Autoplay class that will auto solve the Tower Of Hanoi
autoplay = Autoplay(len(disc_list), s, rods, rod_positions, status)

# Calling function to Solve
autoplay.move(len(disc_list), rods["src"], rods["hlp"], rods["dest"])

s.update()
s.exitonclick()
