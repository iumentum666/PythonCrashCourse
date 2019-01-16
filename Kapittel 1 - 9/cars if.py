cars = ['bmw', 'audi', 'toyota', 'subaru']

# Test av IF setning... hvis BMW er med liten skrift, skrives den med stor skrift

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())