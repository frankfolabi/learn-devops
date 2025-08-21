class Restaurant:
    """Model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Simulate the restaurant description."""
        print(f"{self.restaurant_name.title()} has {self.cuisine_type.title()} cuisine.")

    def reyn_restaurant(self):
        """Displays if the restaurant is reyn."""
        print(f"{self.restaurant_name.title()} is reyn!")

class IceCreamStand(Restaurant):
    """Model an ice cream stand in a resturant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the child class to inherit from the parent."""
        super().__init__(restaurant_name, cuisine_type)

    def describe_flavors(self):
        """Displays the list of ice cream flavors."""
        self.flavors = ['strawberry', 'vanilla', 'banana', 'chocolate']
        return self.flavors



# Make an instance. 
first_restaurant = IceCreamStand('ola mummy', 'african')

# Call the two methods in the class.
print(f"\nWelcome to {first_restaurant.restaurant_name.title()} restaurant!")
print("Here are the available ice cream flavors.")
available_flavors = first_restaurant.describe_flavors()
for available_flavor in available_flavors:
    print(f"- {available_flavor}")
