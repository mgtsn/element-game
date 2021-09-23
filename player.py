from tkinter import *
from tkinter import ttk

from spellcard import *


class Player:
    NUM_SPELLS = 2
    STARTING_LIFE = 20

    def make_spells(self):
        spells = []
        for i in range(self.NUM_SPELLS):
            spells.append(Spellcard(self.frame, i))
        return spells

    def __init__(self, parent, col, row):
        self.frame = ttk.Frame(parent)
        self.frame.grid(column=col, row=row)
        self.num = 0
        self.life = self.STARTING_LIFE
        self.spells = self.make_spells()
