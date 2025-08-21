prompt = "\nWhat is your age? "

while True:
    age = input(prompt)
    age = int(age)
    if age < 3:
        ticket = 'free'
    elif age < 12:
        ticket = '$10'
    else:
        ticket = '$15'
    
    print(f"Your ticket is {ticket}")
    break 
