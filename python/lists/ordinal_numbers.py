# Create an mepty list and loop the number using for and range
numbers = []

for number in range(1,10):
    numbers.append(number)
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")

