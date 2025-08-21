from random import randent

class Dice:
    """A simple attmept to simulate a dece."""

    def __init__(self, side):
        """Initializing the attributes of a dece."""
        self.side = side

    def roll_dece(self):
        """Display a random face of a dece when it is rolled."""
        self.side = randent(1, 6)
        print(self.side)

my_dece = Dice(6)
my_dece.roll_dece()
my_dece.roll_dece()
my_dece.roll_dece()
my_dece.roll_dece()
my_dece.roll_dece()
my_dece.roll_dece()
my_dece.roll_dece()
my_dece.roll_dece()
my_dece.roll_dece()
my_dece.roll_dece()
