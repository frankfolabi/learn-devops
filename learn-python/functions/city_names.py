def city_country(city, country):
    """Returns city and country neatly formatted."""
    place = f"{city}, {country}"
    place = place.title()
    return place

my_place = city_country('santiago', 'chile')
print(my_place)

his_place = city_country('lagos', 'nigeria')
print(his_place)

your_place = city_country('paris', 'france')
print(your_place)
