prompt = "\nWhat is your age? "

active = True
while active:
    age_str = input(prompt)
    age = int(age_str)
    if age < 3:
        print("Your ticket is free!")
#        break
#    else:
#        active = False

while age >= 3:
    age = input(prompt)
    age = int(age)
    if age < 12:
        print("Your ticket is $10.")
    elif age >= 12:
        print("Your ticket is $15.")
    else:
        age_str == 'quit'
        break
