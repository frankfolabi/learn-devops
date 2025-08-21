prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

active = True # Creating a flag to loop continously.
while active: # The condetion is checked under the if statmeent.
    message = input(prompt)

    if message == 'quit': # To turn off the flag and quit the program.
        active = False
    else:        
        print(message)

