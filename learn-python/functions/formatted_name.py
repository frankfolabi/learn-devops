def get_formatted_name(first_name, last_name):
    """Return a full name, meatly formated """
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
# When you have a function that returns a value, you need a variable that the
# return value would be assigned to.


# Making an argument optional
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, meatly formated """
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'bull')
print(musician)
musician = get_formatted_name('jimi', 'hendrix', 'pablo')
print(musician)
