# 6.1 Person data
person = {
        'first_name' : 'john',
        'last_name': 'ammendall',
        'age' : '30',
        'city' : 'ikigai',
        }

print(f"Firstname: {person.get('first_name').title()}")
print(f"Lastname: {person.get('last_name').title()}")
print(f"Age: {person.get('age').title()}")
print(f"City: {person.get('city').title()}")


