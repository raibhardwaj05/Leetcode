import turtle
from turtle import Screen, Turtle
from Disk import Disc
from Rods import Rod
from Autoplay import Autoplay
from Status import Status

# --- Screen Setup ---
s = Screen()
s.setup(1000, 600)
s.bgcolor("Black")
s.colormode(1)
s.tracer(0)

# --- Rod and Disc Creation ---
R = Rod()
R.create()
R.label()

disc = Disc(R, s)
disc.create_disc()
status = Status()

# --- Disc & Rod Settings ---
disc_height = 20
rod_positions = {"src": -350, "hlp": 0, "dest": 350}
rods = {"src": [], "hlp": [], "dest": []}

num_disc = disc.discs
disc_list = disc.disc_list

# Place discs on src rod
for i, d in enumerate(disc_list):
    rods["src"].append(d)
    d.og_color = d.fillcolor()
    d.goto(rod_positions["src"], -185 + i * disc_height)
    d.showturtle()

s.update()

# --- Selected disc state ---
selected_disc: dict[str, any] = {"disc": None, "from_rod": None}

# --- Autoplay ---
autoplay = Autoplay(len(disc_list), s, rods, rod_positions, status)

# --- Reset game ---
def reset_game():
    global rods, selected_disc

    for rod_stack in rods.values():
        rod_stack.clear()

    selected_disc["disc"] = None
    selected_disc["from_rod"] = None

    for i, d in enumerate(disc_list):
        rods["src"].append(d)
        x = rod_positions["src"]
        y = -185 + i * disc_height
        d.goto(x, y)
        d.fillcolor(d.og_color)

    t = Turtle()
    t.color("red")
    t.penup()
    t.hideturtle()
    t.goto(0, 250)
    t.write("You Lose: Solution", align="center", font=("Arial", 15, "bold"))

    status.remaining = status.total_step
    autoplay.move(len(disc_list), rods["src"], rods["hlp"], rods["dest"])

    s.update()

# --- Onkey Hint ---
def hint():
    reset_game()
    autoplay.move(len(disc_list), rods["src"], rods["hlp"], rods["dest"])

# --- Helper to get disc size ---
def get_disk_size(disk):
    return disk.shapesize()[1]


# --- Manual rod-based click listener ---
selected_rod = None

def handle_click(x, y):
    global selected_rod, disc_list, rods

    clicked_rod = None
    for rod, xpos in rod_positions.items():
        if xpos - 80 < x < xpos + 80:  # rod area
            clicked_rod = rod
            break
    if not clicked_rod:
        return

    if selected_rod is None:
        if rods[clicked_rod]:
            selected_rod = clicked_rod
        return

    if selected_rod != clicked_rod and rods[selected_rod]:
        src = rods[selected_rod]
        dest = rods[clicked_rod]

        if (not dest) or (get_disk_size(src[-1]) <= get_disk_size(dest[-1])):
            disc_to_move = src.pop()
            rod_x_coord = rod_positions[clicked_rod]
            rod_y_coord = -185 + len(dest) * disc_height
            autoplay.move_turtle(disc_to_move, rod_x_coord, rod_y_coord)
            dest.append(disc_to_move)
            status.decrease()

            if status.remaining <= 0 and len(rods["dest"]) != len(disc_list):
                reset_game()

            elif status.remaining <= 0 and len(rods["dest"]) == len(disc_list):
                t = Turtle()
                t.color("orange")
                t.penup()
                t.hideturtle()
                t.goto(0, 230)
                t.write("You Win\nMove to Next Level", align="center", font=("Arial", 15, "bold"))


    selected_rod = None

s.listen()
s.onkey(key= "h", fun = hint)

# --- Bind the new click listener ---
s.onscreenclick(handle_click)
s.update()
s.mainloop()
