import car_class

my_car = car_class.Car("Toyota", "camery", 2020)
print(my_car.get_descriptive_name())

my_car.odometer = 50
my_car.read_odometer()