class SpellCard:
    def __init__(self):
        self.contents = {"f": 0, "a": 0, "w": 0, "e": 0}

    def is_empty(self):
        for c in self.contents:
            if self.contents[c]:
                return False
        return True

    def add_element(self, element):
        self.contents[element] += 1

    def print_card(self):
        if self.is_empty():
            print("Empty")
        else:
            for c in self.contents:
                if self.contents[c]:
                    print(f"{c}:{self.contents[c]}", end=" ")
            print()
