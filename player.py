from spellcard import *


class Player:
    NUM_SPELLS = 4

    def make_spells(self):
        spells = []
        for _ in range(self.NUM_SPELLS):
            spells.append(Spellcard())
        return spells

    def __init__(self):
        self.num = 0
        self.spells = self.make_spells()
