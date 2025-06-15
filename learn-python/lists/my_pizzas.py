my_pizzas = ['cheese', 'chicken', 'pepperoni']
friends_pizzas = my_pizzas[:]
my_pizzas.append('meat')
friends_pizzas.append('hawaii')

print("My pizzas are: ")
for my_pizza in my_pizzas:
    print(my_pizza)

print("\nMy friends pizzas are: ")
for friends_pizza in friends_pizzas:
    print(f"\t{friends_pizza}")
