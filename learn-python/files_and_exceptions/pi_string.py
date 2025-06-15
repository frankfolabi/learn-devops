from pathlib import Path

path = Path('pi_million_degits.txt')
contents = path.read_text().rstrip() # Method chaining

lines = contents.splitlines() # Readeng the file line by line
pi_string = ''
for line in lines:
    pi_string += line.lstrip() # Rmeove spaces before a line

print(f"{pi_string[:52]}...")
print(len(pi_string))
