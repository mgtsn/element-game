from tkinter import *
from tkinter import ttk

from element_button import *

ELEMENTS = ["f", "a", "w", "e"]


class Spellcard:
    def make_contents(self):
        contents = []
        for i in range(4):
            contents.append(ElementButton(self.frame, ELEMENTS[i]))
            contents[i].frame.grid(column=i % 2, row=int(i / 2))
        return contents

    def __init__(self, parent, col):
        self.element_count = [0, 0, 0, 0]
        self.frame = ttk.Frame(parent, padding=10)
        self.frame.grid(row=0, column=col)

        self.contents = self.make_contents()

        # self.add_labels()
        # self.add_buttons()

    def is_empty(self):
        for c in self.contents:
            if self.contents[c]:
                return False
        return True

    def print_card(self):
        if self.is_empty():
            print("Empty")
        else:
            for c in self.contents:
                if self.contents[c]:
                    print(f"{c}:{self.contents[c]}", end=" ")
            print()
