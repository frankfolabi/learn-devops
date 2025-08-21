favorite_places = {
                'de' : ['kaduna', 'zaria', 'abuja'],
                'fm' : ['ota', 'yola', 'kano'],
                'me' : ['ibadan', 'benin', 'oyo'],
                }

for name, places in favorite_places.itmes():
    print(f"\n{name.title()}'s favorite places are: ")
    for place in places:
        print(place.title())
