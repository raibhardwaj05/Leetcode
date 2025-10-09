from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

# ----------------- Database Connection -----------------
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Tanay@Rai1",
    database="TowerOfHanoi"
)
cursor = conn.cursor()

# ----------------- Main Window -----------------
r = Tk()
r.title("Tower Of Hanoi")
r.geometry("1000x600")
r.minsize(1000, 600)
r.configure(bg="royalblue")

# ----------------- Leaderboard Frame -----------------
leaderboard = Frame(r, bg="darkblue", borderwidth=5)
leaderboard.pack(side="right", fill="both", padx=30, pady=50)

Label(leaderboard, text="       Leaderboard       ", font="Arial 25 bold", bg="silver").pack(fill=X, pady=10)

columns = ("Rank", "Player Name", "Score")
tree = ttk.Treeview(leaderboard, columns=columns, show="headings", height=15)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100, anchor="center")

tree.pack(fill="both", expand=True, pady=10)

# Treeview styling
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview",
                background="darkblue",
                foreground="white",
                rowheight=25,
                fieldbackground="darkblue")
style.configure("Treeview.Heading",
                background="silver",
                foreground="black",
                font=("Arial", 12, "bold"))
style.map("Treeview",
          background=[("selected", "gold"), ("!selected", "darkblue")],
          foreground=[("selected", "black"), ("!selected", "white")])

# ----------------- Main Window Frame -----------------
window = Frame(r, bg="darkblue", borderwidth=5)
window.pack(side="left", fill="both", expand=True, padx=30, pady=50)

# Home Section
home = Frame(window, bg="cyan", borderwidth=5)
home.pack(side="top", fill="x", pady=10)
Label(home, text="HOME", font="Arial 15 bold", bg="cyan").pack(pady=2)

# Player Type Section
playertype = Frame(window, bg="darkblue", borderwidth=5)
playertype.pack(side="top", pady=20)

player = StringVar()
player.set("new")

new = Radiobutton(playertype, text="New Player",
                  bg="silver", fg="black",
                  variable=player, value="new",
                  indicatoron=0, width=15,
                  selectcolor="gold", font=("Arial", 14, "bold"))
new.grid(row=0, column=0, padx=20, pady=15)

existing = Radiobutton(playertype, text="Existing Player",
                       bg="silver", fg="black",
                       variable=player, value="exist",
                       indicatoron=0, width=15,
                       selectcolor="gold", font=("Arial", 14, "bold"))
existing.grid(row=0, column=1, padx=20, pady=15)

# Name Entry Section
name_frame = Frame(window, bg="darkblue")
name_frame.pack(side="top", pady=20)
Label(name_frame, text="Enter Name:", bg="darkblue", fg="white",
      font=("Arial", 13, "bold")).grid(row=0, column=0, padx=5, pady=10, sticky="e")
entry = Entry(name_frame, width=30, font=("Arial", 14))
entry.grid(row=0, column=1, padx=5, pady=15, sticky="w")

# Buttons
start_btn = Button(window, text="Start Game", font=("Arial", 14, "bold"), bg="gold", fg="darkblue")
start_btn.pack(pady=15)
quit_btn = Button(window, text="Quit Game", font=("Arial", 14, "bold"), bg="gold", fg="darkblue", command=r.destroy)
quit_btn.pack(pady=10)

# ----------------- Leaderboard Functions -----------------
def update_leaderboard(highlight_name=None):
    """Fetch data from DB and update Treeview, optionally highlight a player"""
    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("SELECT PlayerName, Score FROM leaderboard ORDER BY Score DESC")
    results = cursor.fetchall()

    for rank, (player_name, score) in enumerate(results, start=1):
        tree.insert("", "end", values=(rank, player_name, score))

    if highlight_name:
        for item in tree.get_children():
            if tree.item(item, "values")[1] == highlight_name:
                tree.selection_set(item)
                tree.see(item)
                break

def start_game():
    pname = entry.get().strip()
    if not pname:
        messagebox.showwarning("Input Error", "Please enter a name.")
        return

    if player.get() == "new":
        # Check for duplicates
        cursor.execute("SELECT PlayerName FROM leaderboard WHERE PlayerName=%s", (pname,))
        if cursor.fetchone():
            messagebox.showinfo("Duplicate Entry", "Player already exists. Please select existing player.")
            return

        # Insert new player
        cursor.execute("INSERT INTO leaderboard (PlayerName, Score) VALUES (%s, %s)", (pname, 0))
        conn.commit()
        update_leaderboard(highlight_name=pname)
        entry.delete(0, END)
        messagebox.showinfo("Success", f"New player '{pname}' added and highlighted.")

    else:  # Existing Player
        cursor.execute("SELECT Score FROM leaderboard WHERE PlayerName=%s", (pname,))
        result = cursor.fetchone()
        if result:
            update_leaderboard(highlight_name=pname)
            entry.delete(0, END)
            messagebox.showinfo("Player Found", f"Player '{pname}' found with score {result[0]}.")
        else:
            messagebox.showerror("No Results", f"No player named '{pname}' found. Please check the name or select 'New Player'.")

# Attach function to button
start_btn.config(command=start_game)

# Populate leaderboard initially
update_leaderboard()

r.mainloop()
