import pizza
import pizza as p
from pizza import make_pizza
from pizza import make_pizza as mp

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green pepper', 'extra cheese')

p.make_pizza(8, 'onions', 'suya')

make_pizza(10, 'peanut', 'cashew nut', 'hazelnut')

mp(15, 'muesli', 'granola', 'bran')
