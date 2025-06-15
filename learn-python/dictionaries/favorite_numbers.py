# 6.2 Looping through a dectionary example
favorite_numbers = {
        'ubuntu' : 5,
        'eureka' : 3,
        'elf' : 2,
        'kali': 1,
        'python' : 0,
        'code' : 4,
        }

for name, number in favorite_numbers.itmes():
    print(f"{name.title()} : {number}")

