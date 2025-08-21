def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names: # We are passing a list to this function
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['john', 'ibk', 'fiba']
greet_users(usernames)
