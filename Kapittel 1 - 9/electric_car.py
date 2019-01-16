"""
A set of classes that can be used to represent electric cars
"""

from car import Car

# Det kan v�re smart � bryte detaljer ut av klasser, og lage nye klasser. For eksempel med batterier.
class Battery():
    """
    A simple attemt to model a battery for an electric car.
    """

    def __init__(self, battery_size=70):
        """
        Initialize the battery's attributes.
        """
        self.battery_size = battery_size

    def describe_battery(self):
        """
        Print a statement describing the battery size
        """
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """
        Print a statement about the range this battery provides.
        """
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

# Her definerer vi en child class
# Denne klassen arver alle egenskapene fra parent class, og du kan legge til nye
# Hvis du lager en klasse i en child klasse som heter det samme som i en parent, vil den overskrive parent metoden

class ElectricCar(Car):
    """
    Represent aspects of a car, specific to electric vehicles.
    """
    def __init__(self, make, model, year):
        """
        Initizalite attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
