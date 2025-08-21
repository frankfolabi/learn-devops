from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encodeng='utf-8')
    except FileNotFoundError:
        pass # This is to fail silently.
        print(f"{path} is missing.")
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

filenames = ['alice.txt', 'moby_deck.txt', 'siddhartha.txt', 'little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)
