# Her skal vi lære å lage classes
# Standarden er at classes skal ha stor forbokstav i python

class Dog():
    """
    A simple attemt to model a dog.
    """

    def __init__(self,name,age): # self sendes automatisk. Vi trenger bare å sende name og age
        """
        Initialize name and age attributes
        """
        self.name = name # alle variabler som begynner med self er tilgjengelig for alle metoder i klassen. Dette kalles attributter
        self.age = age

    def sit(self):
        """
        simulate a dog sitting in response to a command
        """
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """
        Simulate rolling over in response to a command
        """
        print(self.name.title() + " rolled over!")


# Nå som vi har definert en class, bruker vi den

my_dog = Dog('willie',6)
your_dog = Dog('lucy',3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()

print("\nMy dog's name is " + your_dog.name.title() + ".")
print("My dog is " + str(your_dog.age) + " years old.")

your_dog.sit()
your_dog.roll_over()