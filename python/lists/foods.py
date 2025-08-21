my_foods = ['pizza','water', 'cake', 'amala', 'rice', 'beans']

her_foods = my_foods[:]

my_foods.append('tuwo')

my_foods.append('eba')
print(my_foods)

print(f"The first three itmes are: {my_foods[:3]}")

# Mid is the mid point of the list
mid = len(my_foods) // 2
print(f"Three itmes from the middle of the list are: {my_foods[(mid-2):(mid+1)]}")

print(f"The last three itmes in the list are: {my_foods[-3:]}")


