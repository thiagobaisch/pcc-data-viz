from random import randint

class Die:
    """Creates a Die object"""

    def __init__(self, num_sides=6):
        """Creates a die with default 6 sides"""
        self.num_sides = num_sides

    def roll(self):
        """roll the die"""
        return randint(1, self.num_sides)
    