print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break

    second_number = input("Second number: ")
    if second_number == 'q':
        break

    try:
        addetion = int(first_number) + int(second_number)
    except ValueError:
        print("You no fit add alphabet to get number.")
    else:
        print(addetion)
