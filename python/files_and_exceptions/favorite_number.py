from pathlib import Path
import json

# Store a number in a json file
number = input("What is your favorite number: ")

path = Path('fav_number.json')
contents = json.dumps(number)
path.write_text(contents)

# Retrieve saved number from file

#path = Path('fav_number.json')
contents = path.read_text()
number = json.loads(contents)
print(f"I know your favorite number! It's {number}.")
