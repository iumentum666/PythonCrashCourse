# Vi lager et dictionary som skal inneholde informasjon om en bruker på en site
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

# Og så drar vi ut all informasjon fra dictionariet ved hjelp av en god gammeldags loop
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)