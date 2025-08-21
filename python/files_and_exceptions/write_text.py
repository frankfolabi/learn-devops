from pathlib import Path

path = Path('programming.txt')
path.write_text("I love Python. It's simple to learn.")

contents = "The past two weeks crash course on Python has been great."
contents += "I have learnt a lot more about Python."
contents += "I wish other books are like this too in breaking down concepts."

path.write_text(contents)
