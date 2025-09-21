"""
Tower of Hanoi Visualization with Turtle Graphics
- Follows all Tower of Hanoi rules
- Moves one disk at a time
- Never places larger disk on a smaller one
"""

import turtle
import time

# Screen setup
SCREEN_WIDTH, SCREEN_HEIGHT = 900, 500
BASE_Y = -180
PEG_X = [-250, 0, 250]
DISK_HEIGHT = 25
MIN_DISK_WIDTH = 50
DISK_WIDTH_STEP = 20   # reduce to avoid overlap
ANIMATION_DELAY = 0.3  # seconds between moves

# ---------------- Disk Class ----------------
class Disk(turtle.Turtle):
    def __init__(self, size_index, color):
        super().__init__(visible=False)
        self.size_index = size_index
        self.shape("square")

        # Disk width calculation
        width = MIN_DISK_WIDTH + size_index * DISK_WIDTH_STEP
        stretch_x = width / 20.0   # scale horizontally
        stretch_y = DISK_HEIGHT / 20.0  # scale vertically

        self.shapesize(stretch_y, stretch_x)  # height, width
        self.color("black", color)
        self.penup()
        self.speed("fastest")
        self.showturtle()

    def move_to(self, x, y):
        # Animate: lift -> move -> drop
        curr_x, curr_y = self.position()
        self.goto(curr_x, BASE_Y + 200)   # lift up
        self.goto(x, BASE_Y + 200)        # slide across
        self.goto(x, y)                   # drop down

# ---------------- Peg Class ----------------
class Peg:
    def __init__(self, x):
        self.x = x
        self.disks = []

    def push(self, disk):
        self.disks.append(disk)

    def pop(self):
        return self.disks.pop()

    def height(self):
        return len(self.disks)

# ---------------- Drawing ----------------
def draw_scene():
    pen = turtle.Turtle(visible=False)
    pen.pensize(3)

    # Draw base
    pen.penup()
    pen.goto(-SCREEN_WIDTH // 2 + 40, BASE_Y - 10)
    pen.pendown()
    pen.forward(SCREEN_WIDTH - 80)

    # Draw pegs
    for x in PEG_X:
        pen.penup()
        pen.goto(x, BASE_Y - 10)
        pen.setheading(90)
        pen.pendown()
        pen.forward(250)

# ---------------- Hanoi Logic ----------------
def hanoi(n, source, target, auxiliary, moves):
    if n == 0:
        return
    hanoi(n-1, source, auxiliary, target, moves)
    disk = source.pop()
    target.push(disk)
    moves.append((disk, target))
    hanoi(n-1, auxiliary, target, source, moves)

def animate(moves):
    move_counter = 1
    for disk, peg in moves:
        x = peg.x
        y = BASE_Y + (peg.height() - 1) * DISK_HEIGHT
        disk.move_to(x, y)
        screen.update()
        print(f"Move {move_counter}: Disk {disk.size_index+1} → Peg {PEG_X.index(peg.x)+1}")
        move_counter += 1
        time.sleep(ANIMATION_DELAY)

# ---------------- Main ----------------
if __name__ == "__main__":
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.title("Tower of Hanoi - Turtle Animation")
    screen.tracer(0, 0)

    try:
        n = int(screen.numinput("Disks", "Enter number of disks (3–8 recommended):", 4, 1, 10))
    except:
        n = 4

    draw_scene()

    # Create pegs
    pegs = [Peg(x) for x in PEG_X]

    # Disk colors (cycled if more disks than colors)
    colors = ["red", "blue", "green", "orange", "purple", "yellow", "pink", "cyan", "brown", "magenta"]

    # Create disks on first peg
    for i in range(n-1, -1, -1):  # largest at bottom
        d = Disk(i, colors[i % len(colors)])
        pegs[0].push(d)
        d.goto(pegs[0].x, BASE_Y + (pegs[0].height()-1) * DISK_HEIGHT)

    screen.update()

    # Solve and animate
    moves = []
    hanoi(n, pegs[0], pegs[2], pegs[1], moves)
    animate(moves)

    screen.tracer(1)
    turtle.done()
