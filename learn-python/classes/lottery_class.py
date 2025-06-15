from random import choices

class Lottery:
    """An attmept to model a winning lottery."""

    def __init__(self, winning_numbers):
        """Initialize the attributes."""
        self.winning_numbers = winning_numbers

    def winning_ticket(self):
        """Display the winning ticket from the pool of numbers."""
        self.winning_ticket = choices(self.winning_numbers, k=4)
        print(self.winning_ticket)

    def ticket(self):
        """Looping through number of tickets to win."""
        self.my_ticket = []
        self.counter = 0

        while True:
            self.ticket = choices(self.winning_numbers, k=4)
            self.my_ticket.append(self.ticket)
            self.counter +=1
            if self.winning_ticket in self.my_ticket:
                print(f"You played {self.counter} times before winning.")
                break

winning_numbers = ['A', 'B', 'C', 'D', 'E', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

first_attmept = Lottery(winning_numbers)
first_attmept.winning_ticket()
first_attmept.ticket()
