from pathlib import Path

file_path = Path('learning_python.txt')
contents = file_path.read_text().rstrip()
print(contents)

lines = contents.splitlines()
for line in lines:
    print(line)
