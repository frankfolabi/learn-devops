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

class Privileges:
    """Privileges that a user can have."""
    
    def __init__(self):
        """Initialize the instance attribute."""
        self.privileges = None

    def show_privileges(self):
        """Display what an admin user can do."""
        self.privileges = ['can add post', 'can delete post', 'can ban user']
        return self.privileges

class Admin(User):
    """A child class to model an admin user."""

    def __init__(self, first_name, last_name, age, location, username):
        """Initialize the parent attributes."""
        super().__init__(first_name, last_name, age, location, username)
        self.privileges = Privileges()




first_user = Admin('john', 'ammend-all', 25, 'uranus', 'jamend') 
first_user.describe_user()
admin_privileges = first_user.privileges.show_privileges()
for admin_privilege in admin_privileges:
    print(admin_privilege)
