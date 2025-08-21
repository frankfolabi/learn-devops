prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message = "" # Initial value of mepty string is to compare in the while loop.
while message != 'quit':
    message = input(prompt)

    if message != 'quit': # To avoid printing quit when entered.
        print(message)

