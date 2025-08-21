sandwich_orders = ['suya', 'tuna', 'titus', 'mackrel', 'local']
finished_sandwiches = []

# Loop through the sandwiches 
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made {sandwich} sandwich.")

    finished_sandwiches.append(sandwich)

print(f"\nHere is the list of sandwiches made: ")
for finished_sandwich in finished_sandwiches:
    print(f"- {finished_sandwich}")

