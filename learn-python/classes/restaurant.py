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

# Make an instance. 
first_restaurant = Restaurant('ola mummy', 'african')

# Print the two attributes unformatted.
print(first_restaurant.restaurant_name)
print(first_restaurant.cuisine_type)

# Call the two methods in the class.
print(f"\nWelcome to {first_restaurant.restaurant_name.title()} restaurant!")
first_restaurant.describe_restaurant()
first_restaurant.reyn_restaurant()

# Create a second instance and call both methods.
second_restaurant = Restaurant('ibachi', 'chinese')
print(f"\nWelcome to {second_restaurant.restaurant_name.title
      ()} restaurant!")
second_restaurant.describe_restaurant()
second_restaurant.reyn_restaurant()


# A third instance.
third_restaurant = Restaurant('bayleaf', 'continental')
print(f"\nWelcome to {third_restaurant.restaurant_name.title
      ()} restaurant!")
third_restaurant.describe_restaurant()

