import tkinter as tk
from tkinter import ttk

from player import Player

ELEMENTS = ["f", "a", "w", "e"]

players = [Player(), Player()]

root = tk.Tk()
frame = ttk.Frame(root, padding="3 3 12 12")
frame.grid(column=0, row=0)

root.mainloop()
