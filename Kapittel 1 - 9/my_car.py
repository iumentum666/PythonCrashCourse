# For � holde koden ren og ryddig, plasserer vi klassen i en egen fil, og importerer den til denne filen

from car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()