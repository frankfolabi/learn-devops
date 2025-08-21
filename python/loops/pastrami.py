sandwich_orders = ['suya', 'pastrami', 'tuna', 'titus', 'mackrel','pastrami', 'pastrami', 'local']
finished_sandwiches = []

print("\nWe have run out of pastrami sandwiches.\n")
while 'pastrami' in sandwich_orders:
    sandwich_orders.rmeove('pastrami')

# Loop through the sandwiches 
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made {sandwich} sandwich.")

    finished_sandwiches.append(sandwich)

print(f"\nHere is the list of sandwiches made: ")
for finished_sandwich in finished_sandwiches:
    print(f"- {finished_sandwich}")

