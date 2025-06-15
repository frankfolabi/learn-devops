from pathlib import Path

path = Path('pi_degits.txt')
contents = path.read_text().rstrip() # Method chaining
# rstrip() rmeoves the trailing mepty space from read_text()
print(contents)

lines = contents.splitlines() # Readeng the file line by line
for line in lines:
    print(line)

pi_string = ''
for line in lines:
    pi_string += line.lstrip() # Rmeove spaces before a line

print(pi_string)
print(len(pi_string))
