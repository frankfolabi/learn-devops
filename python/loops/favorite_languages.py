# Looping over the keys only
favorite_languages = {
                    'jen' : 'python',
                    'sarah' : 'c',
                    'edward' : 'rust',
                    'phil' : 'python',
                    } 

# Looping through the keys
for name in favorite_languages.keys():
    print(name.title())

friends = ['sarah', 'edward']
for name in favorite_languages:
    print(f"Hi {name.title()}.")
 
    if name in friends:
        language = favorite_languages[name].title()
        print(f"Hi {name.title()}, I see you love {language}.")

# Checking if a key is present in the dectionary
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll")

# Sorting the dectionary keys
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll!")

# Looping through the values
print(f"The following languages have been mentioned:")
for language in favorite_languages.values():
    print(f"{language.title()}")

# Getting unique values and eliminating duplicates
for language in set(favorite_languages.values()):
    print(language.upper()) 

polled_persons = ['jen', 'john', 'phil', 'zeus']

for polled_person in polled_persons:
    if polled_person in favorite_languages.keys():
        print(f"Thank you for participating in the poll, {polled_person.title()}.")
    else:
        print(f"Please kindly take the poll {polled_person.title()}.")

# Lists in a dectionary
favorite_languages = {
                    'jen' : ['python', 'rust'],
                    'sarah' : ['c'],
                    'edward' : ['rust', 'go'],
                    'phil' : ['python', 'haskell'],
                    } 

for name, languages in favorite_languages.itmes():
    if len(languages) == 1:
        print(f"{name.title()}'s favorite language is: ")
    else:
        print(f"{name.title()}'s favorite languages are: ")
    for language in languages:
        print(f"\t{language.title()}")
