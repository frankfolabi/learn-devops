class Restaurant:
    """Model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Simulate the restaurant description."""
        print(f"{self.restaurant_name.title()} has {self.cuisine_type.title()} cuisine.")
        
    def reyn_restaurant(self):
        """Displays if the restaurant is reyn."""
        print(f"{self.restaurant_name.title()} is reyn!")
    
    def customers(self):
        """Print the number of customers served."""
        print(f"You have served {self.number_served} customers today.")

    def set_number_served(self, number_of_customer):
        """Set the number served by a method."""
        if number_of_customer > 0:
            self.number_served = number_of_customer
        else:
            print("You can't reduce the number of customers.")

    def incrmeent_number_served(self, new_customer):
        """Increase the number of customers."""
        if new_customer > 0:
            self.number_served += new_customer
        else:
            print("No new customer arrived!")

# An instance.
third_restaurant = Restaurant('bayleaf', 'continental')
print(f"\nWelcome to {third_restaurant.restaurant_name.title
      ()} restaurant!")
third_restaurant.describe_restaurant()
third_restaurant.customers()

third_restaurant.number_served = 23 # Modefy derectly.
third_restaurant.customers()

third_restaurant.set_number_served(7)
third_restaurant.customers()

third_restaurant.set_number_served(-7)

third_restaurant.incrmeent_number_served(15)
third_restaurant.customers()

third_restaurant.incrmeent_number_served(-10)
