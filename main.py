from tkinter import *
from tkinter import ttk

from player import Player

ELEMENTS = ["f", "a", "w", "e"]


root = Tk()
root.title("Elements")


frame = ttk.Frame(root, padding="3 3 12 12")
frame.grid(column=0, row=0)

players = [Player(frame, 0, 0), Player(frame, 0, 1)]

print(players[0].spells[0].contents)

root.mainloop()
