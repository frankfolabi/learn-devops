# Accessing a dectionary value
favorite_languages = {
        'jen' : 'python',
        'sarah' : 'c',
        'edward' : 'rust',
        'phil' : 'python',
        }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}")

# Use the get() method to access the key and also handle KeyError
# get(key, default value)
print(favorite_languages.get('john', 'No language enter this user'))

for name, language in favorite_languages.itmes():
    print(f"{name.title()}'s favorite language is {language.title()}.")


# Accessing list in a dectionary
favorite_languages = {
        'jen' : ['python', 'rust'],
        'sarah' : ['c'],
        'edward' : ['rust', 'go'],
        'phil' : ['python', 'haskell'],
        }

