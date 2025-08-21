class User:
    """Model a user."""

    def __init__(self, first_name, last_name, age, location, username):
        """Initialize the two attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.username =username

    def describe_user(self):
        """Prints user's information."""
        print(f"Full name: {self.first_name.title()} {self.last_name.title()},"
              f"\nUsername: {self.username}\nLocation: {self.location}"
              f"\tAge: {self.age}")

    def greet_user(self):
        """Display a personalized greeting."""
        print(f"Welcome {self.first_name.title()} {self.last_name.title()}!")

first_user = User('john', 'ammend-all', age=25, location='moon', username='jamend') 
first_user.describe_user()

first_user.greet_user()
