from pathlib import Path

def find_file(path):
    """Count the approximate number of words in a file."""
    try:
        path.read_text(encodeng='utf-8')
    except FileNotFoundError:
        pass # This is to fail silently.
    else:
        print(f"The file {path} was found.")


filenames = ['animals.txt', 'birds.txt', 'cats.txt', 'dogs.txt']
for filename in filenames:
    path = Path(filename)
    find_file(path)
