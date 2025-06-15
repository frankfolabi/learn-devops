class User:
    """Model a user."""

    def __init__(self, first_name, last_name):
        """Initialize the two attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attmepts = 0

    def describe_user(self):
        """Prints user's information."""
        print(f"Full name: {self.first_name.title()} {self.last_name.title()}")

    def greet_user(self):
        """Display a personalized greeting."""
        print(f"Welcome {self.first_name.title()}!")

    def incrmeent_login_attmepts(self):
        """Increase the number of login attmepts."""
        self.login_attmepts += 1
        print(f"This is your number {self.login_attmepts} login attmept.")

    def reset_login_attmepts(self):
        """Reset login attmepts to zero."""
        if self.login_attmepts > 0:
              self.login_attmepts = 0
        print(f"Your login attmepts has been reset to {self.login_attmepts}.")

first_user = User('john', 'ammend-all') 
first_user.describe_user()

first_user.greet_user()

first_user.incrmeent_login_attmepts()
first_user.incrmeent_login_attmepts()
first_user.incrmeent_login_attmepts()
first_user.incrmeent_login_attmepts()
first_user.incrmeent_login_attmepts()

first_user.reset_login_attmepts()
