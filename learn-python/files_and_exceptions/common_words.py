from pathlib import Path

def count_words(path, word):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encodeng='utf-8')
    except FileNotFoundError:
        pass # This is to fail silently.
    else:
        # Count the number of times a word in the file:
        words = contents.lower().count(word)
        print(f"In the file {path}, the word {word} appears {words} times.")

filenames = ['alice.txt', 'moby_deck.txt', 'siddhartha.txt', 'little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path,'the ')
