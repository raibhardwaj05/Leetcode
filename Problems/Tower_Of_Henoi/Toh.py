from turtle import Screen, Turtle
from Disk import Disc
from Rods import Rod
from Autoplay import Autoplay
from Status import Status
from typing import Any

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
    d.og_color = d.fillcolor()

# select the "disc" "from the rod" is initially None
selected_disc: dict[str, Any] = {"disc": None, "from_rod": None}

# creating object of Autoplay class that will auto solve the Tower Of Hanoi
autoplay = Autoplay(len(disc_list), s, rods, rod_positions, status)

def reset_game():
    global selected_disc, rods, disc_list, status

    for rod_stack in rods.values():
        rod_stack.clear()

    selected_disc["disc"] = None
    selected_disc["from_rod"] = None

    for d in disc_list:
        rods["src"].append(d)

    t = Turtle()
    t.color("red")
    t.penup()
    t.hideturtle()
    t.goto(0, 250)
    t.write("You Lose: Solution", align="center", font=("Arial", 15, "bold"))
    autoplay.move(len(disc_list), rods["src"], rods["hlp"], rods["dest"])

    status.remaining = status.total_step
    s.update()

# x → the x-coordinate of the mouse click
# y → the y-coordinate of the mouse click
# d=d → the current disc d from the loop.
def move_on_click(x, y, disc):
    global rods, selected_disc

    # if the selected disc is the topmost then only select
    for rod_name, rod_stack in rods.items():
        if rod_name and rod_stack[-1] == disc:
            if selected_disc["disc"] is None:
                selected_disc["disc"] = disc
                selected_disc["from_rod"] = rod_name
                disc.color("red") #highlight
            else:
                # to move from selected rod to destination rod
                from_rod = selected_disc["from_rod"]
                moving_disc = selected_disc["disc"]

                # if rod is not empty or rod disc is greater than moving disc then only move
                if (not rod_stack) or (rod_stack[-1].shapesize()[1] > moving_disc.shapesize()[1]):
                    rods[from_rod].pop()
                    rod_x_cord = rod_positions[rod_name]
                    rod_y_coord = -185 + len(rod_stack) * disc_height
                    autoplay.move_turtle(moving_disc, rod_x_cord, rod_y_coord)
                    rod_stack.append(moving_disc)
                    status.decrease()
                    s.update()

                    if status.remaining <= 0:
                        reset_game()

                moving_disc.fillcolor(moving_disc.og_color)
                selected_disc["disc"] = None
                selected_disc["from_rod"] = None

# on click handler
for d in disc_list:
    d.onclick(lambda x, y, d=d: move_on_click(x, y, d))


s.update()
s.mainloop()
