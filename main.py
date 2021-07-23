from spellcard import *

elements = ["f", "a", "w", "e"]

spells = []
for i in range(5):
    spells.append(SpellCard())

playing = True

while playing:
    for spell in spells:
        spell.print_card()
    command = input("Enter Command: ")
    if not command:
        playing = False
    else:
        card = int(command[0])
        element = command[1]
        spells[card].add_element(element)
