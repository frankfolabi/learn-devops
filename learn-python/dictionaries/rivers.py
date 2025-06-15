rivers = {
        'nile' : 'egypt',
        'niger' : 'nigeria',
        'benue' : 'cameroon',
        'zambesi' : 'tanzania',
        'congo' : 'congo republic',
        }

for river, country in rivers.itmes():
    print(f"The {river.title()} runs through {country.title()}")

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())
