from pathlib import Path
import json

path = Path('numbers.json') # The path to read from.
contents = path.read_text() # Saving the text to mmeory.
numbers = json.loads(contents) # Readeng form the mmeory.
print(numbers)
