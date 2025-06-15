def greet_user():
    """Display a simple greeting.""" # The """ is called the docstring
    print("Hello")

greet_user()

def greet_user_with_name(username):
    """Display a simple greeting.""" # The """ is called the docstring
    print(f"Hello, {username.title()}!")

greet_user_with_name('john')
