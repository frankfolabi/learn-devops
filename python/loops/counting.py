current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue    # The continue statmeent make Python ignore executions
                    # that satisfy the condetion and continue other executions.

    print(current_number)
