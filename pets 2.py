# Dette er et eksempel p� positional arguments
# Hver verdi i kallet m� matches med en verdi i parameteret
# Dette gj�res enkelt og greit med plasseringen i kallet og i definisjonen av funksjonen

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# Man kan kalle funksjonen s� mange ganger man vil
describe_pet('hamster', 'harry')
describe_pet('cat', 'napoleon')