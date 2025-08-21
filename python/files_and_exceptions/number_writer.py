from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]

contents = json.dumps(numbers) # The content to be written.
path = Path('numbers.json') # The path it will be written to.
path.write_text(contents) # The writing of the content.
