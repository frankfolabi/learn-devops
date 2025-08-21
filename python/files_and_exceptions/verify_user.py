from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    """Prompt for a new username."""
    username = {}
    username['name'] = input("What is your name? ")
    username['gender'] = input("What is your gender? ")
    username['age'] = input("How old are you? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """Greet the user by name."""
    path = Path('username_dect.json')
    username = get_stored_username(path)
    verify = input(f"Are you {username['name']}? (yes/no) ")
    if verify == 'yes':
        print(f"Welcome back, {username['name']}!")
    else:
        username = get_new_username(path)
        print(f"We'll rmemeber you when you come back, {username['name']}!")

greet_user()
