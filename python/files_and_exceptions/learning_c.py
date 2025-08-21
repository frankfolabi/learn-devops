from pathlib import Path

file_path = Path('learning_python.txt')
contents = file_path.read_text().rstrip()

for line in contents.splitlines():
    line = line.replace('Python', 'C')
    print(line)
