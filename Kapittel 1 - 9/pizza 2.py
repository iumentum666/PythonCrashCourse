# Noen ganger trenger man å lage en funksjon som kan ta i mot et uspesifisert antall argumenter

def make_pizza(*toppings): # Dette lager en tom tuple. En tuple er en list som ikke kan endres...
    """Print the list of toppings that have been requested."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')