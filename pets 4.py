# Har skal vi bruke default verdi
# Denne verdien brukes hvis ikke noe annet blir definert i kallet

def describe_pet(pet_name, animal_type='dog'): # De med default verdi defineres til slutt. Da kan man bruke posisjonering hvis man vil
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='Willie')
describe_pet(pet_name='Bsj',animal_type='Klump')
describe_pet(animal_type='tull', pet_name='Usj')
describe_pet('napoleon') # i og med at vi ikke spesifiserer parameter, og den andre er default, kan vi kalle funksjonen slik også