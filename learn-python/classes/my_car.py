from car import Car

my_new_car = Car('toyota', 'camry', 1996)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_readeng = 23
my_new_car.read_odometer()
