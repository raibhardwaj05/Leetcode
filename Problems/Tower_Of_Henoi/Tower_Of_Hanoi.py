from turtle import Screen
from Disk import Disc
from Rods import Rod
import time

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

disc_height = 20

rod_positions = {
    "src" : -250,
    "hlp" : 0,
    "dest" : 250
}

rods = {
    "src" : [],
    "hlp" : [],
    "dest" : []
}

num_disc = disc.discs
disc_list = disc.disc_list

for d in disc_list:
    rods["src"].append(d)

def move_turtle(discs, x_target, y_target):
    current_x, current_y = discs.position()

    steps = 20
    travel_x = (x_target - current_x)/steps
    travel_y = (y_target - current_y)/steps

    for i in range(20):
        current_x += travel_x
        current_y += travel_y
        discs.goto(current_x, current_y)
        s.update()
        time.sleep(0.05)

def move(num_discs, source, helper, destination):
    if num_discs == 0:
        return

    move(num_discs - 1, source, destination, helper)

    discs = source.pop()

    if destination is rods["src"]:
        rod_x_coord = rod_positions["src"]
    elif destination is rods["hlp"]:
        rod_x_coord = rod_positions["hlp"]
    else:
        rod_x_coord = rod_positions["dest"]

    rod_y_coord = -185 + len(destination) * disc_height

    move_turtle(discs, rod_x_coord, rod_y_coord)
    destination.append(discs)

    move(num_discs - 1, helper, source, destination)

move(len(disc_list), rods["src"], rods["hlp"], rods["dest"])

s.update()
s.exitonclick()
