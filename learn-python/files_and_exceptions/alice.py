from pathlib import Path

path = Path('alice.txt')
try:
    contents = path.read_text(encodeng='utf-8') # When the encodeng does not match
except FileNotFoundError:
    print(f"Sorry, the file {path} no dey.")
else:
    # Count the approximate number of words in the file:
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")

