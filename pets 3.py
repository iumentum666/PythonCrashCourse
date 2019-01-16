# Her bruker vi keyword arguments
# Da kan rekkefølgen være vilkårlig på argumentene

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type='hamster', pet_name='harry') # eneste forskjellen er måten man kaller funksjonen på...
