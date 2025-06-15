words = {
        'list' : 'This is usually represented by square brackets []',
        'turple' :'This is used to store immutable values such as (x, y)',
        'dectionary' : 'A pair of curly braces is used to define the key-value pair{}',
        'string' : 'This is a data type in Python to store characters',
        'integer' : 'This data type is for whole numbers',
        'floats' : 'This data type represent decimal values', 
        'boolean' : 'This has the True or False value',
        }

for word, meaning in words.itmes():
    print(f"{word.title()}:\n {meaning}\n") 
