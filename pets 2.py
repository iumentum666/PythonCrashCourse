# Dette er et eksempel på positional arguments
# Hver verdi i kallet må matches med en verdi i parameteret
# Dette gjøres enkelt og greit med plasseringen i kallet og i definisjonen av funksjonen

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# Man kan kalle funksjonen så mange ganger man vil
describe_pet('hamster', 'harry')
describe_pet('cat', 'napoleon')