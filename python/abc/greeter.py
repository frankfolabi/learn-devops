# Buildeng a clean input with prompt over several lines
prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your name? " # The += is to add a new string to the first

name = input(prompt)
print(f"\nHello, {name.title()}")
