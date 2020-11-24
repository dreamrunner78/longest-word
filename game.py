import string, random

class Game ():

    def __init__ (self):
        self.grid = random.choices(string.ascii_uppercase, k=9)

    def random_grid (self, length):
        self.grid = random.choices(string.ascii_uppercase, k=length)


    def is_valid (self, word):
        res = [c in self.grid for c in word.upper()]
        if False in res:
            return False
        return True
