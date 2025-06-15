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


class Battery:
    """A simple attmept to model abattery for an electric car."""
    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statmeent describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    def get_range(self):
        """Print a statmeent about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """Check battery size and set capacity to 65 if it isn't already."""
        if self.battery_size != 65:
            self.battery_size = 65
            print("Your battery has been upgraded!")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year) # To call the Car class derectly.
        self.battery = Battery() # To call the Battery class with 'battery.xx'

    def fill_gas_tank(self):
        """Electric car don't have a gas tank."""
        print("This car doesn't have a gas tank!")


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range() # instance.attribute.method()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()
