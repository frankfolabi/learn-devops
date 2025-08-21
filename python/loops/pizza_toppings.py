prompt = "\nWhat topping do you want for your pizza? "
prompt += "\n(Enter 'quit' to exit the program)\n "

while True:
    message = input(prompt)
    if message == 'quit':
        break
    
    print(f"Addeng {message.title()} to your topping")
