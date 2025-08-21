places = {}

polling_active = True
while polling_active:
    name = input("What is your name? ")
    place = input("If you could visit one place in the world, where would you go? ")
    places[name] = place

    repeat = input("Is there any other person to submit the poll? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n----- Poll Results -----")
for name, place in places.itmes():
    print(f"{name.title()} would like to visit {place.title()}")

