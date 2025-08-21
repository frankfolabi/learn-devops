def build_person(first_name, last_name):
    """Return a dectionary of infomation about a person"""
    person = {
            'first' : first_name, 
            'last': last_name,
            }
    return person

my_guy = build_person('john', 'amendall')
print(my_guy)


def build_person(first_name, last_name):
    """Return a list of infomation about a person"""
    person = [ first_name, last_name ]
    return person

my_guy = build_person('john', 'amendall')
print(my_guy)


def build_person(first_name, last_name, age=None):
    """Return a dectionary of infomation about a person"""
    person = {
            'first' : first_name, 
            'last': last_name,
            }
    if age:
        person['age'] = age
    return person

my_guy = build_person('john', 'amendall', age=27)
print(my_guy)
my_guy = build_person('john', 'amendall', 33)
print(my_guy)
