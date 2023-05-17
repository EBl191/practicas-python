from random import randint

class Dice:
    """Represent a die, which can be rolled."""

    def __init__(self, sides=6):
        """Initialize the die."""
        self.sides = sides

    def roll_dice(self):
        """Return a number between 1 and the number of sides."""
        return randint(1, self.sides)
    

d6 = Dice()
d10 = Dice(10)
d20 = Dice(20)

results = []

for roll_num in range(10):
    result = d20.roll_dice()
    results.append(result)
print("20 rolls of a 10-sided dice: ")
print(results)

