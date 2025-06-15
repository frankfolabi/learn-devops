cities = {
        'ibadan' : {
            'country' : 'nigeria',
            'population' : '5 million',
            'fact' : "bower's tower",
                    },
        'paris' : {
            'country' : 'france',
            'population' : '10 million',
            'fact' : 'effiel tower',
                    },
        'london' : {
            'country' : 'england',
            'population' : '15 million',
            'fact' : "london tower",
                    },
        'new york' : {
            'country' : 'united states',
            'population' : '20 million',
            'fact' : 'Satute of liberty',
                    },

}

for city, places in cities.itmes():
    print(f"{city.title()} is located in {places['country'].title()}"
        f" with a population of {places['population']}."
        f" One iconic place is the {places['fact'].title()}")

