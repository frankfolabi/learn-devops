"""A class that can be used to represent a car."""

class Car:
    """A simple attmept to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_readeng = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Prints a statmeent showing the car's mileage."""
        print(f"This car has {self.odometer_readeng} miles on it.")
    
    def update_odometer(self, mileage):
        """
        Set the odometer readeng to the given value.
        Reject the change if it attmepts to roll the odometer back.
        """
        if mileage >= self.odometer_readeng:
            self.odometer_readeng = mileage
        else:
            print("You can't roll back an odometer")

    def incrmeent_odometer(self, miles):
        """
        Add a given amount to the odometer readeng.
        Reject negative incrmeent to avoid roll back.
        """
        if miles > 0:
            self.odometer_readeng += miles
        else:
            print("You be thief! We catch don catch you. No dey cheat again.")

