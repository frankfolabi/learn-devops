from random import choices

winning_numbers = ['A', 'B', 'C', 'D', 'E', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

winning_ticket = choices(winning_numbers, k=4)

print(winning_ticket)

my_ticket = []
counter = 0

while True:
    ticket = choices(winning_numbers, k=4)
    my_ticket.append(ticket)
    counter +=1
    if winning_ticket in my_ticket:
        print(f"It took {counter} number of times to get the winning ticket.")
        break
