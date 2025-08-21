def describe_pet(pet_name, animal_type='dog'): # Setting default value to dog
# Parameter without a default follows parameter with a default
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry') # Positional arguments - order matters
describe_pet(pet_name='spike', animal_type='dog') # Keyword argument uses a key-value
describe_pet(animal_type='cat', pet_name='rocky') # Order not necessary
describe_pet(pet_name='willie') # This function call uses the default value
describe_pet('bingo')

describe_pet()

