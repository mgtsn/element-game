from tkinter import *
from tkinter import ttk


class ElementButton:
    def _increase(self):
        self.value += 1
        self.label.config(text=self.value)

    def __init__(self, parent, element):
        self.value = 0
        self.frame = ttk.Frame(parent)

        self.label = ttk.Label(self.frame, text=self.value)
        self.label.grid(column=0, row=0)

        self.button = ttk.Button(
            self.frame, text=element, command=lambda: self._increase()
        )
        self.button.grid(column=0, row=1)
