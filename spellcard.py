from tkinter import *
from tkinter import ttk

ELEMENTS = ["f", "a", "w", "e"]


class Spellcard:
    def add_element(self, element, increase):
        self.contents[element] += increase

    def add_buttons(self):
        ttk.Label(self.frame, text=f"f: {self.contents['f']}").grid(column=0, row=0)
        ttk.Button(
            self.frame,
            text="+",
            command=self.add_element("f", 1),
        ).grid(column=1, row=0)

    def __init__(self, parent, col):
        self.contents = {"f": 0, "a": 0, "w": 0, "e": 0}

        self.frame = ttk.Frame(parent, padding=10)
        self.frame.grid(row=0, column=col)

        self.add_buttons()

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
